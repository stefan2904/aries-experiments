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


class InlineResponse2004(object):
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
        'accept': 'str',
        'connection_id': 'str',
        'created_at': 'datetime',
        'initiator': 'str',
        'invitation_key': 'str',
        'invitation_mode': 'str',
        'my_did': 'str',
        'request_id': 'str',
        'routing_state': 'str',
        'state': 'str',
        'their_label': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'accept': 'accept',
        'connection_id': 'connection_id',
        'created_at': 'created_at',
        'initiator': 'initiator',
        'invitation_key': 'invitation_key',
        'invitation_mode': 'invitation_mode',
        'my_did': 'my_did',
        'request_id': 'request_id',
        'routing_state': 'routing_state',
        'state': 'state',
        'their_label': 'their_label',
        'updated_at': 'updated_at'
    }

    def __init__(self, accept=None, connection_id=None, created_at=None, initiator=None, invitation_key=None, invitation_mode=None, my_did=None, request_id=None, routing_state=None, state=None, their_label=None, updated_at=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger"""  # noqa: E501

        self._accept = None
        self._connection_id = None
        self._created_at = None
        self._initiator = None
        self._invitation_key = None
        self._invitation_mode = None
        self._my_did = None
        self._request_id = None
        self._routing_state = None
        self._state = None
        self._their_label = None
        self._updated_at = None
        self.discriminator = None

        if accept is not None:
            self.accept = accept
        if connection_id is not None:
            self.connection_id = connection_id
        if created_at is not None:
            self.created_at = created_at
        if initiator is not None:
            self.initiator = initiator
        if invitation_key is not None:
            self.invitation_key = invitation_key
        if invitation_mode is not None:
            self.invitation_mode = invitation_mode
        if my_did is not None:
            self.my_did = my_did
        if request_id is not None:
            self.request_id = request_id
        if routing_state is not None:
            self.routing_state = routing_state
        if state is not None:
            self.state = state
        if their_label is not None:
            self.their_label = their_label
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def accept(self):
        """Gets the accept of this InlineResponse2004.  # noqa: E501

        Connection invitation accept mode  # noqa: E501

        :return: The accept of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._accept

    @accept.setter
    def accept(self, accept):
        """Sets the accept of this InlineResponse2004.

        Connection invitation accept mode  # noqa: E501

        :param accept: The accept of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._accept = accept

    @property
    def connection_id(self):
        """Gets the connection_id of this InlineResponse2004.  # noqa: E501

        the connection ID of the connection invitation  # noqa: E501

        :return: The connection_id of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this InlineResponse2004.

        the connection ID of the connection invitation  # noqa: E501

        :param connection_id: The connection_id of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2004.  # noqa: E501

        Created time  # noqa: E501

        :return: The created_at of this InlineResponse2004.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2004.

        Created time  # noqa: E501

        :param created_at: The created_at of this InlineResponse2004.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def initiator(self):
        """Gets the initiator of this InlineResponse2004.  # noqa: E501

        Connection invitation initiator  # noqa: E501

        :return: The initiator of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this InlineResponse2004.

        Connection invitation initiator  # noqa: E501

        :param initiator: The initiator of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._initiator = initiator

    @property
    def invitation_key(self):
        """Gets the invitation_key of this InlineResponse2004.  # noqa: E501

        Invitation key  # noqa: E501

        :return: The invitation_key of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._invitation_key

    @invitation_key.setter
    def invitation_key(self, invitation_key):
        """Sets the invitation_key of this InlineResponse2004.

        Invitation key  # noqa: E501

        :param invitation_key: The invitation_key of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._invitation_key = invitation_key

    @property
    def invitation_mode(self):
        """Gets the invitation_mode of this InlineResponse2004.  # noqa: E501

        Invitation mode  # noqa: E501

        :return: The invitation_mode of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._invitation_mode

    @invitation_mode.setter
    def invitation_mode(self, invitation_mode):
        """Sets the invitation_mode of this InlineResponse2004.

        Invitation mode  # noqa: E501

        :param invitation_mode: The invitation_mode of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._invitation_mode = invitation_mode

    @property
    def my_did(self):
        """Gets the my_did of this InlineResponse2004.  # noqa: E501

        My DID  # noqa: E501

        :return: The my_did of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._my_did

    @my_did.setter
    def my_did(self, my_did):
        """Sets the my_did of this InlineResponse2004.

        My DID  # noqa: E501

        :param my_did: The my_did of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._my_did = my_did

    @property
    def request_id(self):
        """Gets the request_id of this InlineResponse2004.  # noqa: E501

        Request ID of invitation response  # noqa: E501

        :return: The request_id of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this InlineResponse2004.

        Request ID of invitation response  # noqa: E501

        :param request_id: The request_id of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def routing_state(self):
        """Gets the routing_state of this InlineResponse2004.  # noqa: E501

        Routing state of connection invitation  # noqa: E501

        :return: The routing_state of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._routing_state

    @routing_state.setter
    def routing_state(self, routing_state):
        """Sets the routing_state of this InlineResponse2004.

        Routing state of connection invitation  # noqa: E501

        :param routing_state: The routing_state of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._routing_state = routing_state

    @property
    def state(self):
        """Gets the state of this InlineResponse2004.  # noqa: E501

        State of the connection invitation  # noqa: E501

        :return: The state of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineResponse2004.

        State of the connection invitation  # noqa: E501

        :param state: The state of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def their_label(self):
        """Gets the their_label of this InlineResponse2004.  # noqa: E501

        Other party's label  # noqa: E501

        :return: The their_label of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._their_label

    @their_label.setter
    def their_label(self, their_label):
        """Sets the their_label of this InlineResponse2004.

        Other party's label  # noqa: E501

        :param their_label: The their_label of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._their_label = their_label

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineResponse2004.  # noqa: E501

        Updated time  # noqa: E501

        :return: The updated_at of this InlineResponse2004.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineResponse2004.

        Updated time  # noqa: E501

        :param updated_at: The updated_at of this InlineResponse2004.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(InlineResponse2004, dict):
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
        if not isinstance(other, InlineResponse2004):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other