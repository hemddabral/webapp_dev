# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, dnn_model_name: str=None, app_code: str=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param dnn_model_name: The dnn_model_name of this Body.  # noqa: E501
        :type dnn_model_name: str
        :param app_code: The app_code of this Body.  # noqa: E501
        :type app_code: str
        """
        self.swagger_types = {
            'dnn_model_name': str,
            'app_code': str
        }

        self.attribute_map = {
            'dnn_model_name': 'dnn_model_name',
            'app_code': 'app_code'
        }
        self._dnn_model_name = dnn_model_name
        self._app_code = app_code

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dnn_model_name(self) -> str:
        """Gets the dnn_model_name of this Body.

        DNN model for the demo, required for mapping demo input.  # noqa: E501

        :return: The dnn_model_name of this Body.
        :rtype: str
        """
        return self._dnn_model_name

    @dnn_model_name.setter
    def dnn_model_name(self, dnn_model_name: str):
        """Sets the dnn_model_name of this Body.

        DNN model for the demo, required for mapping demo input.  # noqa: E501

        :param dnn_model_name: The dnn_model_name of this Body.
        :type dnn_model_name: str
        """
        if dnn_model_name is None:
            raise ValueError("Invalid value for `dnn_model_name`, must not be `None`")  # noqa: E501

        self._dnn_model_name = dnn_model_name

    @property
    def app_code(self) -> str:
        """Gets the app_code of this Body.

        source code for this application, should be in one file only  # noqa: E501

        :return: The app_code of this Body.
        :rtype: str
        """
        return self._app_code

    @app_code.setter
    def app_code(self, app_code: str):
        """Sets the app_code of this Body.

        source code for this application, should be in one file only  # noqa: E501

        :param app_code: The app_code of this Body.
        :type app_code: str
        """

        self._app_code = app_code
