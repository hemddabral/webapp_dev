# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CubeAIError(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: int=None, type: str=None, message: str=None):  # noqa: E501
        """CubeAIError - a model defined in Swagger

        :param code: The code of this CubeAIError.  # noqa: E501
        :type code: int
        :param type: The type of this CubeAIError.  # noqa: E501
        :type type: str
        :param message: The message of this CubeAIError.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'code': int,
            'type': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'type': 'type',
            'message': 'message'
        }
        self._code = code
        self._type = type
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'CubeAIError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CubeAIError of this CubeAIError.  # noqa: E501
        :rtype: CubeAIError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this CubeAIError.


        :return: The code of this CubeAIError.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this CubeAIError.


        :param code: The code of this CubeAIError.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def type(self) -> str:
        """Gets the type of this CubeAIError.


        :return: The type of this CubeAIError.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this CubeAIError.


        :param type: The type of this CubeAIError.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def message(self) -> str:
        """Gets the message of this CubeAIError.


        :return: The message of this CubeAIError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this CubeAIError.


        :param message: The message of this CubeAIError.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message
