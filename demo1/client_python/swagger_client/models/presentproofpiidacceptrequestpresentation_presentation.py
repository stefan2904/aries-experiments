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


class PresentproofpiidacceptrequestpresentationPresentation(object):
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
        'type': 'str',
        'comment': 'str',
        'formats': 'list[Format]',
        'presentationsattach': 'list[Attachment]'
    }

    attribute_map = {
        'type': '@type',
        'comment': 'comment',
        'formats': 'formats',
        'presentationsattach': 'presentations~attach'
    }

    def __init__(self, type=None, comment=None, formats=None, presentationsattach=None):  # noqa: E501
        """PresentproofpiidacceptrequestpresentationPresentation - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._comment = None
        self._formats = None
        self._presentationsattach = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if comment is not None:
            self.comment = comment
        if formats is not None:
            self.formats = formats
        if presentationsattach is not None:
            self.presentationsattach = presentationsattach

    @property
    def type(self):
        """Gets the type of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501


        :return: The type of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PresentproofpiidacceptrequestpresentationPresentation.


        :param type: The type of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501

        Comment is a field that provides some human readable information about the proposed presentation. TODO: Should follow DIDComm conventions for l10n. [Issue #1300].  # noqa: E501

        :return: The comment of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PresentproofpiidacceptrequestpresentationPresentation.

        Comment is a field that provides some human readable information about the proposed presentation. TODO: Should follow DIDComm conventions for l10n. [Issue #1300].  # noqa: E501

        :param comment: The comment of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def formats(self):
        """Gets the formats of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501

        Formats contains an entry for each presentations~attach array entry, providing the the value of the attachment @id and the verifiable presentation format and version of the attachment.  # noqa: E501

        :return: The formats of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501
        :rtype: list[Format]
        """
        return self._formats

    @formats.setter
    def formats(self, formats):
        """Sets the formats of this PresentproofpiidacceptrequestpresentationPresentation.

        Formats contains an entry for each presentations~attach array entry, providing the the value of the attachment @id and the verifiable presentation format and version of the attachment.  # noqa: E501

        :param formats: The formats of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501
        :type: list[Format]
        """

        self._formats = formats

    @property
    def presentationsattach(self):
        """Gets the presentationsattach of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501

        PresentationsAttach an array of attachments containing the presentation in the requested format(s).  # noqa: E501

        :return: The presentationsattach of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._presentationsattach

    @presentationsattach.setter
    def presentationsattach(self, presentationsattach):
        """Sets the presentationsattach of this PresentproofpiidacceptrequestpresentationPresentation.

        PresentationsAttach an array of attachments containing the presentation in the requested format(s).  # noqa: E501

        :param presentationsattach: The presentationsattach of this PresentproofpiidacceptrequestpresentationPresentation.  # noqa: E501
        :type: list[Attachment]
        """

        self._presentationsattach = presentationsattach

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
        if issubclass(PresentproofpiidacceptrequestpresentationPresentation, dict):
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
        if not isinstance(other, PresentproofpiidacceptrequestpresentationPresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
