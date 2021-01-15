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


class Body13(object):
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
        'invitation': 'OutofbandacceptinvitationInvitation',
        'my_label': 'str',
        'router_connections': 'str'
    }

    attribute_map = {
        'invitation': 'invitation',
        'my_label': 'my_label',
        'router_connections': 'router_connections'
    }

    def __init__(self, invitation=None, my_label=None, router_connections=None):  # noqa: E501
        """Body13 - a model defined in Swagger"""  # noqa: E501

        self._invitation = None
        self._my_label = None
        self._router_connections = None
        self.discriminator = None

        if invitation is not None:
            self.invitation = invitation
        if my_label is not None:
            self.my_label = my_label
        if router_connections is not None:
            self.router_connections = router_connections

    @property
    def invitation(self):
        """Gets the invitation of this Body13.  # noqa: E501


        :return: The invitation of this Body13.  # noqa: E501
        :rtype: OutofbandacceptinvitationInvitation
        """
        return self._invitation

    @invitation.setter
    def invitation(self, invitation):
        """Sets the invitation of this Body13.


        :param invitation: The invitation of this Body13.  # noqa: E501
        :type: OutofbandacceptinvitationInvitation
        """

        self._invitation = invitation

    @property
    def my_label(self):
        """Gets the my_label of this Body13.  # noqa: E501


        :return: The my_label of this Body13.  # noqa: E501
        :rtype: str
        """
        return self._my_label

    @my_label.setter
    def my_label(self, my_label):
        """Sets the my_label of this Body13.


        :param my_label: The my_label of this Body13.  # noqa: E501
        :type: str
        """

        self._my_label = my_label

    @property
    def router_connections(self):
        """Gets the router_connections of this Body13.  # noqa: E501


        :return: The router_connections of this Body13.  # noqa: E501
        :rtype: str
        """
        return self._router_connections

    @router_connections.setter
    def router_connections(self, router_connections):
        """Sets the router_connections of this Body13.


        :param router_connections: The router_connections of this Body13.  # noqa: E501
        :type: str
        """

        self._router_connections = router_connections

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
        if issubclass(Body13, dict):
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
        if not isinstance(other, Body13):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other