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


class Body1(object):
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
        'recipient': 'IntroducesendproposalwithoobrequestRecipient',
        'request': 'IntroducesendproposalwithoobrequestRequest'
    }

    attribute_map = {
        'recipient': 'recipient',
        'request': 'request'
    }

    def __init__(self, recipient=None, request=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501

        self._recipient = None
        self._request = None
        self.discriminator = None

        self.recipient = recipient
        self.request = request

    @property
    def recipient(self):
        """Gets the recipient of this Body1.  # noqa: E501


        :return: The recipient of this Body1.  # noqa: E501
        :rtype: IntroducesendproposalwithoobrequestRecipient
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this Body1.


        :param recipient: The recipient of this Body1.  # noqa: E501
        :type: IntroducesendproposalwithoobrequestRecipient
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def request(self):
        """Gets the request of this Body1.  # noqa: E501


        :return: The request of this Body1.  # noqa: E501
        :rtype: IntroducesendproposalwithoobrequestRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this Body1.


        :param request: The request of this Body1.  # noqa: E501
        :type: IntroducesendproposalwithoobrequestRequest
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
