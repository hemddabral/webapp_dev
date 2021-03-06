# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AppDNN(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, dnn_name: str=None, dnn_uuid: str=None):  # noqa: E501
        """AppDNN - a model defined in Swagger

        :param dnn_name: The dnn_name of this AppDNN.  # noqa: E501
        :type dnn_name: str
        :param dnn_uuid: The dnn_uuid of this AppDNN.  # noqa: E501
        :type dnn_uuid: str
        """
        self.swagger_types = {
            'dnn_name': str,
            'dnn_uuid': str
        }

        self.attribute_map = {
            'dnn_name': 'dnn_name',
            'dnn_uuid': 'dnn_uuid'
        }
        self._dnn_name = dnn_name
        self._dnn_uuid = dnn_uuid

    @classmethod
    def from_dict(cls, dikt) -> 'AppDNN':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppDNN of this AppDNN.  # noqa: E501
        :rtype: AppDNN
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dnn_name(self) -> str:
        """Gets the dnn_name of this AppDNN.


        :return: The dnn_name of this AppDNN.
        :rtype: str
        """
        return self._dnn_name

    @dnn_name.setter
    def dnn_name(self, dnn_name: str):
        """Sets the dnn_name of this AppDNN.


        :param dnn_name: The dnn_name of this AppDNN.
        :type dnn_name: str
        """
        if dnn_name is None:
            raise ValueError("Invalid value for `dnn_name`, must not be `None`")  # noqa: E501

        self._dnn_name = dnn_name

    @property
    def dnn_uuid(self) -> str:
        """Gets the dnn_uuid of this AppDNN.


        :return: The dnn_uuid of this AppDNN.
        :rtype: str
        """
        return self._dnn_uuid

    @dnn_uuid.setter
    def dnn_uuid(self, dnn_uuid: str):
        """Sets the dnn_uuid of this AppDNN.


        :param dnn_uuid: The dnn_uuid of this AppDNN.
        :type dnn_uuid: str
        """
        if dnn_uuid is None:
            raise ValueError("Invalid value for `dnn_uuid`, must not be `None`")  # noqa: E501

        self._dnn_uuid = dnn_uuid
