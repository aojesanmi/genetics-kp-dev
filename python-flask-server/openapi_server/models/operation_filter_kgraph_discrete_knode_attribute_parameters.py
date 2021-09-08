# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
# from openapi_server.models.any_type import AnyType
from openapi_server import util

# from openapi_server.models.any_type import AnyType  # noqa: E501

class OperationFilterKgraphDiscreteKnodeAttributeParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, node_attribute=None, remove_value=None, qnode_keys=None):  # noqa: E501
        """OperationFilterKgraphDiscreteKnodeAttributeParameters - a model defined in OpenAPI

        :param node_attribute: The node_attribute of this OperationFilterKgraphDiscreteKnodeAttributeParameters.  # noqa: E501
        :type node_attribute: str
        :param remove_value: The remove_value of this OperationFilterKgraphDiscreteKnodeAttributeParameters.  # noqa: E501
        :type remove_value: AnyType
        :param qnode_keys: The qnode_keys of this OperationFilterKgraphDiscreteKnodeAttributeParameters.  # noqa: E501
        :type qnode_keys: List[str]
        """
        self.openapi_types = {
            'node_attribute': str,
            'remove_value': object,
            # 'remove_value': AnyType,
            'qnode_keys': List[str]
        }

        self.attribute_map = {
            'node_attribute': 'node_attribute',
            'remove_value': 'remove_value',
            'qnode_keys': 'qnode_keys'
        }

        self._node_attribute = node_attribute
        self._remove_value = remove_value
        self._qnode_keys = qnode_keys

    @classmethod
    def from_dict(cls, dikt) -> 'OperationFilterKgraphDiscreteKnodeAttributeParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationFilterKgraphDiscreteKnodeAttribute_parameters of this OperationFilterKgraphDiscreteKnodeAttributeParameters.  # noqa: E501
        :rtype: OperationFilterKgraphDiscreteKnodeAttributeParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def node_attribute(self):
        """Gets the node_attribute of this OperationFilterKgraphDiscreteKnodeAttributeParameters.

        The name of the node attribute to filter on.  # noqa: E501

        :return: The node_attribute of this OperationFilterKgraphDiscreteKnodeAttributeParameters.
        :rtype: str
        """
        return self._node_attribute

    @node_attribute.setter
    def node_attribute(self, node_attribute):
        """Sets the node_attribute of this OperationFilterKgraphDiscreteKnodeAttributeParameters.

        The name of the node attribute to filter on.  # noqa: E501

        :param node_attribute: The node_attribute of this OperationFilterKgraphDiscreteKnodeAttributeParameters.
        :type node_attribute: str
        """
        if node_attribute is None:
            raise ValueError("Invalid value for `node_attribute`, must not be `None`")  # noqa: E501

        self._node_attribute = node_attribute

    @property
    def remove_value(self):
        """Gets the remove_value of this OperationFilterKgraphDiscreteKnodeAttributeParameters.

        The value for which all edges containing this value in the specified edge_attribute should be removed.  # noqa: E501

        :return: The remove_value of this OperationFilterKgraphDiscreteKnodeAttributeParameters.
        :rtype: AnyType
        """
        return self._remove_value

    @remove_value.setter
    def remove_value(self, remove_value):
        """Sets the remove_value of this OperationFilterKgraphDiscreteKnodeAttributeParameters.

        The value for which all edges containing this value in the specified edge_attribute should be removed.  # noqa: E501

        :param remove_value: The remove_value of this OperationFilterKgraphDiscreteKnodeAttributeParameters.
        :type remove_value: AnyType
        """
        if remove_value is None:
            raise ValueError("Invalid value for `remove_value`, must not be `None`")  # noqa: E501

        self._remove_value = remove_value

    @property
    def qnode_keys(self):
        """Gets the qnode_keys of this OperationFilterKgraphDiscreteKnodeAttributeParameters.

        This indicates if you only want to remove nodes corresponding to a specific list of qnode_keys to be removed. If not provided or empty, all nodes will be considered when filtering.  # noqa: E501

        :return: The qnode_keys of this OperationFilterKgraphDiscreteKnodeAttributeParameters.
        :rtype: List[str]
        """
        return self._qnode_keys

    @qnode_keys.setter
    def qnode_keys(self, qnode_keys):
        """Sets the qnode_keys of this OperationFilterKgraphDiscreteKnodeAttributeParameters.

        This indicates if you only want to remove nodes corresponding to a specific list of qnode_keys to be removed. If not provided or empty, all nodes will be considered when filtering.  # noqa: E501

        :param qnode_keys: The qnode_keys of this OperationFilterKgraphDiscreteKnodeAttributeParameters.
        :type qnode_keys: List[str]
        """

        self._qnode_keys = qnode_keys
