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


class StatusResponse(object):
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
        'id': 'str',
        'type': 'str',
        'duration_waited': 'int',
        'last_added_time': 'datetime',
        'last_delivered_time': 'datetime',
        'last_removed_time': 'datetime',
        'message_count': 'int',
        'total_size': 'int',
        'thread': 'Thread'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'duration_waited': 'duration_waited',
        'last_added_time': 'last_added_time',
        'last_delivered_time': 'last_delivered_time',
        'last_removed_time': 'last_removed_time',
        'message_count': 'message_count',
        'total_size': 'total_size',
        'thread': '~thread'
    }

    def __init__(self, id=None, type=None, duration_waited=None, last_added_time=None, last_delivered_time=None, last_removed_time=None, message_count=None, total_size=None, thread=None):  # noqa: E501
        """StatusResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._duration_waited = None
        self._last_added_time = None
        self._last_delivered_time = None
        self._last_removed_time = None
        self._message_count = None
        self._total_size = None
        self._thread = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if duration_waited is not None:
            self.duration_waited = duration_waited
        if last_added_time is not None:
            self.last_added_time = last_added_time
        if last_delivered_time is not None:
            self.last_delivered_time = last_delivered_time
        if last_removed_time is not None:
            self.last_removed_time = last_removed_time
        if message_count is not None:
            self.message_count = message_count
        if total_size is not None:
            self.total_size = total_size
        if thread is not None:
            self.thread = thread

    @property
    def id(self):
        """Gets the id of this StatusResponse.  # noqa: E501


        :return: The id of this StatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatusResponse.


        :param id: The id of this StatusResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this StatusResponse.  # noqa: E501


        :return: The type of this StatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StatusResponse.


        :param type: The type of this StatusResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def duration_waited(self):
        """Gets the duration_waited of this StatusResponse.  # noqa: E501


        :return: The duration_waited of this StatusResponse.  # noqa: E501
        :rtype: int
        """
        return self._duration_waited

    @duration_waited.setter
    def duration_waited(self, duration_waited):
        """Sets the duration_waited of this StatusResponse.


        :param duration_waited: The duration_waited of this StatusResponse.  # noqa: E501
        :type: int
        """

        self._duration_waited = duration_waited

    @property
    def last_added_time(self):
        """Gets the last_added_time of this StatusResponse.  # noqa: E501


        :return: The last_added_time of this StatusResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_added_time

    @last_added_time.setter
    def last_added_time(self, last_added_time):
        """Sets the last_added_time of this StatusResponse.


        :param last_added_time: The last_added_time of this StatusResponse.  # noqa: E501
        :type: datetime
        """

        self._last_added_time = last_added_time

    @property
    def last_delivered_time(self):
        """Gets the last_delivered_time of this StatusResponse.  # noqa: E501


        :return: The last_delivered_time of this StatusResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_delivered_time

    @last_delivered_time.setter
    def last_delivered_time(self, last_delivered_time):
        """Sets the last_delivered_time of this StatusResponse.


        :param last_delivered_time: The last_delivered_time of this StatusResponse.  # noqa: E501
        :type: datetime
        """

        self._last_delivered_time = last_delivered_time

    @property
    def last_removed_time(self):
        """Gets the last_removed_time of this StatusResponse.  # noqa: E501


        :return: The last_removed_time of this StatusResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_removed_time

    @last_removed_time.setter
    def last_removed_time(self, last_removed_time):
        """Sets the last_removed_time of this StatusResponse.


        :param last_removed_time: The last_removed_time of this StatusResponse.  # noqa: E501
        :type: datetime
        """

        self._last_removed_time = last_removed_time

    @property
    def message_count(self):
        """Gets the message_count of this StatusResponse.  # noqa: E501


        :return: The message_count of this StatusResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_count

    @message_count.setter
    def message_count(self, message_count):
        """Sets the message_count of this StatusResponse.


        :param message_count: The message_count of this StatusResponse.  # noqa: E501
        :type: int
        """

        self._message_count = message_count

    @property
    def total_size(self):
        """Gets the total_size of this StatusResponse.  # noqa: E501


        :return: The total_size of this StatusResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this StatusResponse.


        :param total_size: The total_size of this StatusResponse.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def thread(self):
        """Gets the thread of this StatusResponse.  # noqa: E501


        :return: The thread of this StatusResponse.  # noqa: E501
        :rtype: Thread
        """
        return self._thread

    @thread.setter
    def thread(self, thread):
        """Sets the thread of this StatusResponse.


        :param thread: The thread of this StatusResponse.  # noqa: E501
        :type: Thread
        """

        self._thread = thread

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
        if issubclass(StatusResponse, dict):
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
        if not isinstance(other, StatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other