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
    def __init__(self, deep_learning_model: str=None, quantize: str=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param deep_learning_model: The deep_learning_model of this Body.  # noqa: E501
        :type deep_learning_model: str
        :param quantize: The quantize of this Body.  # noqa: E501
        :type quantize: str
        """
        self.swagger_types = {
            'deep_learning_model': str,
            'quantize': str
        }

        self.attribute_map = {
            'deep_learning_model': 'deep_learning_model',
            'quantize': 'quantize'
        }
        self._deep_learning_model = deep_learning_model
        self._quantize = quantize

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
    def deep_learning_model(self) -> str:
        """Gets the deep_learning_model of this Body.

        The model to analyze.  # noqa: E501

        :return: The deep_learning_model of this Body.
        :rtype: str
        """
        return self._deep_learning_model

    @deep_learning_model.setter
    def deep_learning_model(self, deep_learning_model: str):
        """Sets the deep_learning_model of this Body.

        The model to analyze.  # noqa: E501

        :param deep_learning_model: The deep_learning_model of this Body.
        :type deep_learning_model: str
        """
        if deep_learning_model is None:
            raise ValueError("Invalid value for `deep_learning_model`, must not be `None`")  # noqa: E501

        self._deep_learning_model = deep_learning_model

    @property
    def quantize(self) -> str:
        """Gets the quantize of this Body.

        Specify the tensor format configuration file for a Keras model or for the configuration file to perform the Keras post-training quantization process.  # noqa: E501

        :return: The quantize of this Body.
        :rtype: str
        """
        return self._quantize

    @quantize.setter
    def quantize(self, quantize: str):
        """Sets the quantize of this Body.

        Specify the tensor format configuration file for a Keras model or for the configuration file to perform the Keras post-training quantization process.  # noqa: E501

        :param quantize: The quantize of this Body.
        :type quantize: str
        """

        self._quantize = quantize