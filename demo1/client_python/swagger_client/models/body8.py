# coding: utf-8

"""
    (Aries Agent REST Server) of VC4SM University.

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body8(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'my_did': 'str',
        'request_credential': 'IssuecredentialsendrequestRequestCredential',
        'their_did': 'str'
    }

    attribute_map = {
        'my_did': 'my_did',
        'request_credential': 'request_credential',
        'their_did': 'their_did'
    }

    def __init__(self, my_did=None, request_credential=None, their_did=None):  # noqa: E501
        """Body8 - a model defined in Swagger"""  # noqa: E501

        self._my_did = None
        self._request_credential = None
        self._their_did = None
        self.discriminator = None

        self.my_did = my_did
        self.request_credential = request_credential
        self.their_did = their_did

    @property
    def my_did(self):
        """Gets the my_did of this Body8.  # noqa: E501

        MyDID sender's did  # noqa: E501

        :return: The my_did of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._my_did

    @my_did.setter
    def my_did(self, my_did):
        """Sets the my_did of this Body8.

        MyDID sender's did  # noqa: E501

        :param my_did: The my_did of this Body8.  # noqa: E501
        :type: str
        """
        if my_did is None:
            raise ValueError("Invalid value for `my_did`, must not be `None`")  # noqa: E501

        self._my_did = my_did

    @property
    def request_credential(self):
        """Gets the request_credential of this Body8.  # noqa: E501


        :return: The request_credential of this Body8.  # noqa: E501
        :rtype: IssuecredentialsendrequestRequestCredential
        """
        return self._request_credential

    @request_credential.setter
    def request_credential(self, request_credential):
        """Sets the request_credential of this Body8.


        :param request_credential: The request_credential of this Body8.  # noqa: E501
        :type: IssuecredentialsendrequestRequestCredential
        """
        if request_credential is None:
            raise ValueError("Invalid value for `request_credential`, must not be `None`")  # noqa: E501

        self._request_credential = request_credential

    @property
    def their_did(self):
        """Gets the their_did of this Body8.  # noqa: E501

        TheirDID receiver's did  # noqa: E501

        :return: The their_did of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._their_did

    @their_did.setter
    def their_did(self, their_did):
        """Sets the their_did of this Body8.

        TheirDID receiver's did  # noqa: E501

        :param their_did: The their_did of this Body8.  # noqa: E501
        :type: str
        """
        if their_did is None:
            raise ValueError("Invalid value for `their_did`, must not be `None`")  # noqa: E501

        self._their_did = their_did

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Body8, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body8):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other