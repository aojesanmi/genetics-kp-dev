import json
import requests 
from urllib.error import HTTPError
from openapi_server.dcc.disease_utils import get_disease_descendants
import logging 
import sys 
import pymysql
import os

# logging
# logging.setLevel('INFO')
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logging.basicConfig(level=logging.INFO, format=f'[%(asctime)s] - %(levelname)s - %(name)s %(threadName)s : %(message)s')
handler = logging.StreamHandler(sys.stdout)

def get_logger(name): 
    # get the logger
    logger = logging.getLogger(name)
    # logger.addHandler(handler)

    # return
    return logger 

# get logger
logger = get_logger(__name__)

# constants
# DB settings
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWD = os.environ.get('DB_PASSWD')
DB_SCHEMA = os.environ.get('DB_SCHEMA')

# url settings
TRAN_URL_NORMALIZER=os.environ.get('TRAN_URL_NORMALIZER')

# node types
node_gene ='biolink:Gene'
node_disease = 'biolink:Disease'
node_phenotype = 'biolink:PhenotypicFeature'
node_pathway = 'biolink:Pathway'

# edge types
edge_gene_disease = 'biolink:gene_associated_with_condition'
edge_disease_gene = 'biolink:condition_associated_with_gene'
edge_pathway_disease = 'biolink:genetic_association'
edge_disease_pathway = 'biolink:genetic_association'

# attribute types
attribute_pvalue = 'biolink:p_value'
attribute_probability = 'biolink:probability'
attribute_classification = 'biolink:classification'
attribute_score_translator = 'biolink:score'

# list of accepted edge types
accepted_edge_types = [edge_gene_disease, edge_disease_gene, edge_pathway_disease, edge_disease_pathway]

# input type translation map
type_translation_input = {
        # predicates
        'biolink:genetic_association': 'associated',

        # categories
        'biolink:Gene': 'gene',
        'biolink:Disease': 'disease',
        'biolink:PhenotypicFeature': 'phenotypic_feature',
        'biolink:Pathway': 'pathway',
    }

# reverse the type translation map for output
type_translation_output = dict((value, key) for key, value in type_translation_input.items())

# input curie translation map
curie_translation_input = {
        # compounds (biolink: molepro)
        'PUBCHEM.COMPOUND': 'CID',
        'CHEMBL.COMPOUND': 'ChEMBL',
        'DRUGBANK': 'DrugBank',
        'KEGG': 'KEGG.COMPOUND',
    }

# reverse the curie translation map for output
curie_translation_output = dict((value, key) for key, value in curie_translation_input.items())


def translate_type(input_type, is_input=True):
    """ translates the predicates and categories if necessary to/from biolink/molepro """
    result = input_type
    map={}
    if is_input:
        map = type_translation_input
    else:
        map = type_translation_output

    # only translate if necessary
    if input_type in map:
        result = map[input_type]

    # log
    # print("utils.translate_type: returning {} for input {}".format(result, input_type))

    # return
    return result

def translate_curie(input_curie, is_input=True):
    """ translates the curie prefix if necessary to/from biolink/molepro """
    result = input_curie
    map={}
    if is_input:
        map = curie_translation_input
    else:
        map = curie_translation_output

    # split the curie into prefix and value
    if input_curie:
        split_curie = input_curie.split(":")

        if len(split_curie) == 2:
            prefix = split_curie[0]
            value = split_curie[1]

            # if prefix needs to be translated, translate, else leave alone
            if prefix in map:
                result = map[prefix] + ":" + value

    # log
    logger.info("utils.translate_curie: returning {} for input {}".format(result, input_curie))

    # return
    return result

def migrate_transformer_chains(inFile, outFile):
    with open(inFile) as f:
        json_obj = json.load(f)
    for chain in json_obj:
        chain['subject'] = translate_type(chain['subject'], False)
        chain['predicate'] = translate_type(chain['predicate'], False)
        chain['object'] = translate_type(chain['object'], False)
        print(chain['subject'],chain['predicate'],chain['object'],'\n')
    with open(outFile, 'w') as json_file:
        json.dump(json_obj, json_file, indent=4, separators=(',', ': ')) # save to file with prettifying

def get_db_curie_synonyms(curie_input, prefix_list=None, type_name='', log=False):
    ''' will call database cache and return the curie name and a list of only the matching prefixes from the prefix list provided '''
    list_result = []

    # get the db connection
    cnx = pymysql.connect(host=DB_HOST, port=3306, database=DB_SCHEMA, user=DB_USER, password=DB_PASSWD)
    cursor = cnx.cursor()

    # query
    sql_select = "select distinct node_synonym_id from translator_cache.comb_cache_curie where node_curie_id = %s"
    cursor.execute(sql_select, curie_input)

    # get the data
    results = cursor.fetchall()
    if results and len(results) > 0:
        logger.info("found DATABASE curie synonyms results for: {} of size: {}".format(curie_input, len(results)))
        for row in results:
            list_result.append(row[0])

    # close db connection
    cursor.close()
    cnx.close()

    # return
    return list_result

def insert_curie_synonyms(curie_id, curie_name, list_synonyms, log=False):
    ''' will insert rows into the curie cache DB '''
    # initialize
    sql_insert = "insert into translator_cache.comb_cache_curie (node_curie_id, node_name, node_synonym_id) values(%s, %s, %s)"

    # create the cursor
    cnx = pymysql.connect(host=DB_HOST, port=3306, database=DB_SCHEMA, user=DB_USER, password=DB_PASSWD)
    cursor = cnx.cursor()

    # insert the data
    for item in list_synonyms:
        cursor.execute(sql_insert, (curie_id, curie_name, item))
    cnx.commit()

    # close the connection
    cursor.close()
    cnx.close()

    # log
    logger.info("inserted DATABASE synonyms for: {} of: {}".format(curie_id, list_synonyms))


def get_curie_synonyms(curie_input, prefix_list=None, type_name='', log=False):
    ''' will call the curie normalizer and return the curie name and a list of only the matching prefixes from the prefix list provided '''
    ''' 20210729 - also added in descendant MONDO diseases '''
    # initialize
    url_normalizer = "https://nodenormalization-sri.renci.org/1.1/get_normalized_nodes?conflate=true&curie={}"
    list_result = []
    curie_name = None
    prefix_disease_list = ['MONDO', 'EFO']

    # get the normalizer url
    if TRAN_URL_NORMALIZER:
        url_normalizer = TRAN_URL_NORMALIZER + "?conflate=true&curie={}"

    # log
    if log:
        logger.info("-> get_curie_synonyms got curie {}, ontology list {} and type name {}".format(curie_input, prefix_list, type_name))

    # if provided no curie, return [None]
    if curie_input is None:
        # OLD - add in at leat None so that have one input when doing query building (as opposed top skipping query with no input)
        # return curie_name, [None]
        return curie_name, []

    # if ncbi or go, skip since that is our standard for genes/pathways
    if curie_input.split(':')[0] in ['NCBIGene', 'GO']:
        logger.info("skip normalizing standard curie: {}".format(curie_input))
        return curie_name, [curie_input]

    # look in the DB first
    list_result = get_db_curie_synonyms(curie_input)

    if len(list_result) < 1:
        # call the service
        url_call = url_normalizer.format(curie_input)
        response = requests.get(url_call)

        # if error, then return curie input as name and one element array
        if response.status_code == 404:
            curie_name = curie_input
            list_result = [curie_input]
            logger.error("ERROR: got node normalizer error for url: {}".format(url_call))

        else:
            json_response = response.json()

            # get the list of curies
            if json_response.get(curie_input):
                curie_name = json_response.get(curie_input).get('id').get('label')
                for item in json_response[curie_input]['equivalent_identifiers']:
                    list_result.append(item['identifier'])

            if log:
                logger.info("got WEB SERVICE curie synonym list result {}".format(list_result))


        # loop through, if MONDO or EFO, look for descendants
        list_new = []
        for item in list_result:
            if item.split(':')[0] in prefix_disease_list:
                if log:
                    print("looking for descendants for disease {}".format(item))

                # look for the descendants
                temp_list = get_disease_descendants(item)

                # add in results to the new list
                list_new += temp_list

        # combine result lists
        list_result += list_new

        # make sure list is unique
        list_result = list(set(list_result))

        # insert data into the cache DB
        insert_curie_synonyms(curie_input, curie_name, list_result)

    # if a prefix list provided, filter with it
    if prefix_list:
        list_new = []
        for item in list_result:
            if item.split(':')[0] in prefix_list:
                list_new.append(item)
        list_result = list_new

    # return
    # BUG? only return none if none provided
    # list_result = list_result if len(list_result) > 0 else [None]
    if log:
        logger.info("for {} input {} return name {} and ontologies {}\n".format(type_name, curie_input, curie_name, list_result))

    return curie_name, list_result

def build_pubmed_ids(publications):
    ''' will build and return the list of pubmid IDs from a comma seperated string of article ids '''
    result = None

    # split string and prepend annotation
    if publications:
        result = ['PMID:' + x.strip() for x in publications.split(',')]

    # return
    return result

if (__name__ == "__main__"):
    pass    