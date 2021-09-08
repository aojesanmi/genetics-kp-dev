# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.log_level import LogLevel
from openapi_server.models.message import Message
from openapi_server.models.schema2 import Schema2
import re
from openapi_server import util

from openapi_server.models.log_level import LogLevel  # noqa: E501
from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.schema2 import Schema2  # noqa: E501
import re  # noqa: E501

class AsyncQuery(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, callback=None, message=None, log_level=None, workflow=None):  # noqa: E501
        """AsyncQuery - a model defined in OpenAPI

        :param callback: The callback of this AsyncQuery.  # noqa: E501
        :type callback: str
        :param message: The message of this AsyncQuery.  # noqa: E501
        :type message: Message
        :param log_level: The log_level of this AsyncQuery.  # noqa: E501
        :type log_level: LogLevel
        :param workflow: The workflow of this AsyncQuery.  # noqa: E501
        :type workflow: List[Schema2]
        """
        self.openapi_types = {
            'callback': str,
            'message': Message,
            'log_level': LogLevel,
            'workflow': List[Schema2]
        }

        self.attribute_map = {
            'callback': 'callback',
            'message': 'message',
            'log_level': 'log_level',
            'workflow': 'workflow'
        }

        self._callback = callback
        self._message = message
        self._log_level = log_level
        self._workflow = workflow

    @classmethod
    def from_dict(cls, dikt) -> 'AsyncQuery':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AsyncQuery of this AsyncQuery.  # noqa: E501
        :rtype: AsyncQuery
        """
        return util.deserialize_model(dikt, cls)

    @property
    def callback(self):
        """Gets the callback of this AsyncQuery.

        Upon completion, this server will send a POST request to the callback URL with `Content-Type: application/json` header and request body containing a JSON-encoded `Response` object. The server MAY POST `Response` objects before work is fully complete to provide interim results with a Response.status value of 'Running'. If a POST operation to the callback URL does not succeed, the server SHOULD retry the POST at least once.  # noqa: E501

        :return: The callback of this AsyncQuery.
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this AsyncQuery.

        Upon completion, this server will send a POST request to the callback URL with `Content-Type: application/json` header and request body containing a JSON-encoded `Response` object. The server MAY POST `Response` objects before work is fully complete to provide interim results with a Response.status value of 'Running'. If a POST operation to the callback URL does not succeed, the server SHOULD retry the POST at least once.  # noqa: E501

        :param callback: The callback of this AsyncQuery.
        :type callback: str
        """
        if callback is None:
            raise ValueError("Invalid value for `callback`, must not be `None`")  # noqa: E501
        if callback is not None and not re.search(r'^https?:\/\/', callback):  # noqa: E501
            raise ValueError("Invalid value for `callback`, must be a follow pattern or equal to `/^https?:\/\//`")  # noqa: E501

        self._callback = callback

    @property
    def message(self):
        """Gets the message of this AsyncQuery.


        :return: The message of this AsyncQuery.
        :rtype: Message
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AsyncQuery.


        :param message: The message of this AsyncQuery.
        :type message: Message
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def log_level(self):
        """Gets the log_level of this AsyncQuery.

        The least critical level of logs to return  # noqa: E501

        :return: The log_level of this AsyncQuery.
        :rtype: LogLevel
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this AsyncQuery.

        The least critical level of logs to return  # noqa: E501

        :param log_level: The log_level of this AsyncQuery.
        :type log_level: LogLevel
        """

        self._log_level = log_level

    @property
    def workflow(self):
        """Gets the workflow of this AsyncQuery.


        :return: The workflow of this AsyncQuery.
        :rtype: List[Schema2]
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this AsyncQuery.


        :param workflow: The workflow of this AsyncQuery.
        :type workflow: List[Schema2]
        """

        self._workflow = workflow
