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


class PresentproofpiidnegotiaterequestpresentationProposePresentation(object):
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
        'proposalattach': 'list[Attachment]'
    }

    attribute_map = {
        'type': '@type',
        'comment': 'comment',
        'formats': 'formats',
        'proposalattach': 'proposal~attach'
    }

    def __init__(self, type=None, comment=None, formats=None, proposalattach=None):  # noqa: E501
        """PresentproofpiidnegotiaterequestpresentationProposePresentation - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._comment = None
        self._formats = None
        self._proposalattach = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if comment is not None:
            self.comment = comment
        if formats is not None:
            self.formats = formats
        if proposalattach is not None:
            self.proposalattach = proposalattach

    @property
    def type(self):
        """Gets the type of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501


        :return: The type of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PresentproofpiidnegotiaterequestpresentationProposePresentation.


        :param type: The type of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501

        Comment is a field that provides some human readable information about the proposed presentation. TODO: Should follow DIDComm conventions for l10n. [Issue #1300]  # noqa: E501

        :return: The comment of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PresentproofpiidnegotiaterequestpresentationProposePresentation.

        Comment is a field that provides some human readable information about the proposed presentation. TODO: Should follow DIDComm conventions for l10n. [Issue #1300]  # noqa: E501

        :param comment: The comment of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def formats(self):
        """Gets the formats of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501

        Formats contains an entry for each proposal~attach array entry, including an optional value of the attachment @id (if attachments are present) and the verifiable presentation format and version of the attachment.  # noqa: E501

        :return: The formats of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501
        :rtype: list[Format]
        """
        return self._formats

    @formats.setter
    def formats(self, formats):
        """Sets the formats of this PresentproofpiidnegotiaterequestpresentationProposePresentation.

        Formats contains an entry for each proposal~attach array entry, including an optional value of the attachment @id (if attachments are present) and the verifiable presentation format and version of the attachment.  # noqa: E501

        :param formats: The formats of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501
        :type: list[Format]
        """

        self._formats = formats

    @property
    def proposalattach(self):
        """Gets the proposalattach of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501

        FilterAttach is an array of attachments that further define the presentation request being proposed. This might be used to clarify which formats or format versions are wanted.  # noqa: E501

        :return: The proposalattach of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._proposalattach

    @proposalattach.setter
    def proposalattach(self, proposalattach):
        """Sets the proposalattach of this PresentproofpiidnegotiaterequestpresentationProposePresentation.

        FilterAttach is an array of attachments that further define the presentation request being proposed. This might be used to clarify which formats or format versions are wanted.  # noqa: E501

        :param proposalattach: The proposalattach of this PresentproofpiidnegotiaterequestpresentationProposePresentation.  # noqa: E501
        :type: list[Attachment]
        """

        self._proposalattach = proposalattach

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
        if issubclass(PresentproofpiidnegotiaterequestpresentationProposePresentation, dict):
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
        if not isinstance(other, PresentproofpiidnegotiaterequestpresentationProposePresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other