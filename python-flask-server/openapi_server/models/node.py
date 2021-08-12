# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.attribute import Attribute
from openapi_server import util

from openapi_server.models.attribute import Attribute  # noqa: E501

class Node(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, categories=None, attributes=None):  # noqa: E501
        """Node - a model defined in OpenAPI

        :param name: The name of this Node.  # noqa: E501
        :type name: str
        :param categories: The categories of this Node.  # noqa: E501
        :type categories: List[str]
        :param attributes: The attributes of this Node.  # noqa: E501
        :type attributes: List[Attribute]
        """
        self.openapi_types = {
            'name': str,
            'categories': List[str],
            'attributes': List[Attribute]
        }

        self.attribute_map = {
            'name': 'name',
            'categories': 'categories',
            'attributes': 'attributes'
        }

        self._name = name
        self._categories = categories
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'Node':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Node of this Node.  # noqa: E501
        :rtype: Node
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Node.

        Formal name of the entity  # noqa: E501

        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Node.

        Formal name of the entity  # noqa: E501

        :param name: The name of this Node.
        :type name: str
        """

        self._name = name

    @property
    def categories(self):
        """Gets the categories of this Node.


        :return: The categories of this Node.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Node.


        :param categories: The categories of this Node.
        :type categories: List[str]
        """

        self._categories = categories

    @property
    def attributes(self):
        """Gets the attributes of this Node.

        A list of attributes describing the node  # noqa: E501

        :return: The attributes of this Node.
        :rtype: List[Attribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Node.

        A list of attributes describing the node  # noqa: E501

        :param attributes: The attributes of this Node.
        :type attributes: List[Attribute]
        """

        self._attributes = attributes
