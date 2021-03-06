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


class Connection(object):
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
        'connection_id': 'str',
        'implicit': 'bool',
        'invitation_did': 'str',
        'invitation_id': 'str',
        'my_did': 'str',
        'namespace': 'str',
        'parent_thread_id': 'str',
        'recipient_keys': 'list[str]',
        'routing_keys': 'list[str]',
        'service_end_point': 'str',
        'state': 'str',
        'their_did': 'str',
        'their_label': 'str',
        'thread_id': 'str'
    }

    attribute_map = {
        'connection_id': 'ConnectionID',
        'implicit': 'Implicit',
        'invitation_did': 'InvitationDID',
        'invitation_id': 'InvitationID',
        'my_did': 'MyDID',
        'namespace': 'Namespace',
        'parent_thread_id': 'ParentThreadID',
        'recipient_keys': 'RecipientKeys',
        'routing_keys': 'RoutingKeys',
        'service_end_point': 'ServiceEndPoint',
        'state': 'State',
        'their_did': 'TheirDID',
        'their_label': 'TheirLabel',
        'thread_id': 'ThreadID'
    }

    def __init__(self, connection_id=None, implicit=None, invitation_did=None, invitation_id=None, my_did=None, namespace=None, parent_thread_id=None, recipient_keys=None, routing_keys=None, service_end_point=None, state=None, their_did=None, their_label=None, thread_id=None):  # noqa: E501
        """Connection - a model defined in Swagger"""  # noqa: E501

        self._connection_id = None
        self._implicit = None
        self._invitation_did = None
        self._invitation_id = None
        self._my_did = None
        self._namespace = None
        self._parent_thread_id = None
        self._recipient_keys = None
        self._routing_keys = None
        self._service_end_point = None
        self._state = None
        self._their_did = None
        self._their_label = None
        self._thread_id = None
        self.discriminator = None

        if connection_id is not None:
            self.connection_id = connection_id
        if implicit is not None:
            self.implicit = implicit
        if invitation_did is not None:
            self.invitation_did = invitation_did
        if invitation_id is not None:
            self.invitation_id = invitation_id
        if my_did is not None:
            self.my_did = my_did
        if namespace is not None:
            self.namespace = namespace
        if parent_thread_id is not None:
            self.parent_thread_id = parent_thread_id
        if recipient_keys is not None:
            self.recipient_keys = recipient_keys
        if routing_keys is not None:
            self.routing_keys = routing_keys
        if service_end_point is not None:
            self.service_end_point = service_end_point
        if state is not None:
            self.state = state
        if their_did is not None:
            self.their_did = their_did
        if their_label is not None:
            self.their_label = their_label
        if thread_id is not None:
            self.thread_id = thread_id

    @property
    def connection_id(self):
        """Gets the connection_id of this Connection.  # noqa: E501


        :return: The connection_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this Connection.


        :param connection_id: The connection_id of this Connection.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def implicit(self):
        """Gets the implicit of this Connection.  # noqa: E501


        :return: The implicit of this Connection.  # noqa: E501
        :rtype: bool
        """
        return self._implicit

    @implicit.setter
    def implicit(self, implicit):
        """Sets the implicit of this Connection.


        :param implicit: The implicit of this Connection.  # noqa: E501
        :type: bool
        """

        self._implicit = implicit

    @property
    def invitation_did(self):
        """Gets the invitation_did of this Connection.  # noqa: E501


        :return: The invitation_did of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._invitation_did

    @invitation_did.setter
    def invitation_did(self, invitation_did):
        """Sets the invitation_did of this Connection.


        :param invitation_did: The invitation_did of this Connection.  # noqa: E501
        :type: str
        """

        self._invitation_did = invitation_did

    @property
    def invitation_id(self):
        """Gets the invitation_id of this Connection.  # noqa: E501


        :return: The invitation_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._invitation_id

    @invitation_id.setter
    def invitation_id(self, invitation_id):
        """Sets the invitation_id of this Connection.


        :param invitation_id: The invitation_id of this Connection.  # noqa: E501
        :type: str
        """

        self._invitation_id = invitation_id

    @property
    def my_did(self):
        """Gets the my_did of this Connection.  # noqa: E501


        :return: The my_did of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._my_did

    @my_did.setter
    def my_did(self, my_did):
        """Sets the my_did of this Connection.


        :param my_did: The my_did of this Connection.  # noqa: E501
        :type: str
        """

        self._my_did = my_did

    @property
    def namespace(self):
        """Gets the namespace of this Connection.  # noqa: E501


        :return: The namespace of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Connection.


        :param namespace: The namespace of this Connection.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def parent_thread_id(self):
        """Gets the parent_thread_id of this Connection.  # noqa: E501


        :return: The parent_thread_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._parent_thread_id

    @parent_thread_id.setter
    def parent_thread_id(self, parent_thread_id):
        """Sets the parent_thread_id of this Connection.


        :param parent_thread_id: The parent_thread_id of this Connection.  # noqa: E501
        :type: str
        """

        self._parent_thread_id = parent_thread_id

    @property
    def recipient_keys(self):
        """Gets the recipient_keys of this Connection.  # noqa: E501


        :return: The recipient_keys of this Connection.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipient_keys

    @recipient_keys.setter
    def recipient_keys(self, recipient_keys):
        """Sets the recipient_keys of this Connection.


        :param recipient_keys: The recipient_keys of this Connection.  # noqa: E501
        :type: list[str]
        """

        self._recipient_keys = recipient_keys

    @property
    def routing_keys(self):
        """Gets the routing_keys of this Connection.  # noqa: E501


        :return: The routing_keys of this Connection.  # noqa: E501
        :rtype: list[str]
        """
        return self._routing_keys

    @routing_keys.setter
    def routing_keys(self, routing_keys):
        """Sets the routing_keys of this Connection.


        :param routing_keys: The routing_keys of this Connection.  # noqa: E501
        :type: list[str]
        """

        self._routing_keys = routing_keys

    @property
    def service_end_point(self):
        """Gets the service_end_point of this Connection.  # noqa: E501


        :return: The service_end_point of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._service_end_point

    @service_end_point.setter
    def service_end_point(self, service_end_point):
        """Sets the service_end_point of this Connection.


        :param service_end_point: The service_end_point of this Connection.  # noqa: E501
        :type: str
        """

        self._service_end_point = service_end_point

    @property
    def state(self):
        """Gets the state of this Connection.  # noqa: E501


        :return: The state of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Connection.


        :param state: The state of this Connection.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def their_did(self):
        """Gets the their_did of this Connection.  # noqa: E501


        :return: The their_did of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._their_did

    @their_did.setter
    def their_did(self, their_did):
        """Sets the their_did of this Connection.


        :param their_did: The their_did of this Connection.  # noqa: E501
        :type: str
        """

        self._their_did = their_did

    @property
    def their_label(self):
        """Gets the their_label of this Connection.  # noqa: E501


        :return: The their_label of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._their_label

    @their_label.setter
    def their_label(self, their_label):
        """Sets the their_label of this Connection.


        :param their_label: The their_label of this Connection.  # noqa: E501
        :type: str
        """

        self._their_label = their_label

    @property
    def thread_id(self):
        """Gets the thread_id of this Connection.  # noqa: E501


        :return: The thread_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this Connection.


        :param thread_id: The thread_id of this Connection.  # noqa: E501
        :type: str
        """

        self._thread_id = thread_id

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
        if issubclass(Connection, dict):
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
        if not isinstance(other, Connection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
