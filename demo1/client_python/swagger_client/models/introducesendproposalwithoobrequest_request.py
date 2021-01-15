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


class IntroducesendproposalwithoobrequestRequest(object):
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
        'goal': 'str',
        'goal_code': 'str',
        'label': 'str',
        'requestattach': 'list[Attachment]',
        'service': 'list[object]'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'goal': 'goal',
        'goal_code': 'goal-code',
        'label': 'label',
        'requestattach': 'request~attach',
        'service': 'service'
    }

    def __init__(self, id=None, type=None, goal=None, goal_code=None, label=None, requestattach=None, service=None):  # noqa: E501
        """IntroducesendproposalwithoobrequestRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._goal = None
        self._goal_code = None
        self._label = None
        self._requestattach = None
        self._service = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if goal is not None:
            self.goal = goal
        if goal_code is not None:
            self.goal_code = goal_code
        if label is not None:
            self.label = label
        if requestattach is not None:
            self.requestattach = requestattach
        if service is not None:
            self.service = service

    @property
    def id(self):
        """Gets the id of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501


        :return: The id of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntroducesendproposalwithoobrequestRequest.


        :param id: The id of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501


        :return: The type of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IntroducesendproposalwithoobrequestRequest.


        :param type: The type of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def goal(self):
        """Gets the goal of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501


        :return: The goal of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :rtype: str
        """
        return self._goal

    @goal.setter
    def goal(self, goal):
        """Sets the goal of this IntroducesendproposalwithoobrequestRequest.


        :param goal: The goal of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :type: str
        """

        self._goal = goal

    @property
    def goal_code(self):
        """Gets the goal_code of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501


        :return: The goal_code of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :rtype: str
        """
        return self._goal_code

    @goal_code.setter
    def goal_code(self, goal_code):
        """Sets the goal_code of this IntroducesendproposalwithoobrequestRequest.


        :param goal_code: The goal_code of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :type: str
        """

        self._goal_code = goal_code

    @property
    def label(self):
        """Gets the label of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501


        :return: The label of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this IntroducesendproposalwithoobrequestRequest.


        :param label: The label of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def requestattach(self):
        """Gets the requestattach of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501


        :return: The requestattach of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._requestattach

    @requestattach.setter
    def requestattach(self, requestattach):
        """Sets the requestattach of this IntroducesendproposalwithoobrequestRequest.


        :param requestattach: The requestattach of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :type: list[Attachment]
        """

        self._requestattach = requestattach

    @property
    def service(self):
        """Gets the service of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501


        :return: The service of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this IntroducesendproposalwithoobrequestRequest.


        :param service: The service of this IntroducesendproposalwithoobrequestRequest.  # noqa: E501
        :type: list[object]
        """

        self._service = service

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
        if issubclass(IntroducesendproposalwithoobrequestRequest, dict):
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
        if not isinstance(other, IntroducesendproposalwithoobrequestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
