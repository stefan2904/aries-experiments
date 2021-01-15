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


class IssuecredentialpiidacceptrequestIssueCredential(object):
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
        'credentialsattach': 'list[Attachment]',
        'formats': 'list[Format]'
    }

    attribute_map = {
        'type': '@type',
        'comment': 'comment',
        'credentialsattach': 'credentials~attach',
        'formats': 'formats'
    }

    def __init__(self, type=None, comment=None, credentialsattach=None, formats=None):  # noqa: E501
        """IssuecredentialpiidacceptrequestIssueCredential - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._comment = None
        self._credentialsattach = None
        self._formats = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if comment is not None:
            self.comment = comment
        if credentialsattach is not None:
            self.credentialsattach = credentialsattach
        if formats is not None:
            self.formats = formats

    @property
    def type(self):
        """Gets the type of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501


        :return: The type of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IssuecredentialpiidacceptrequestIssueCredential.


        :param type: The type of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501

        Comment is an optional field that provides human readable information about this Credential Offer, so the offer can be evaluated by human judgment. TODO: Should follow DIDComm conventions for l10n. [Issue #1300].  # noqa: E501

        :return: The comment of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this IssuecredentialpiidacceptrequestIssueCredential.

        Comment is an optional field that provides human readable information about this Credential Offer, so the offer can be evaluated by human judgment. TODO: Should follow DIDComm conventions for l10n. [Issue #1300].  # noqa: E501

        :param comment: The comment of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def credentialsattach(self):
        """Gets the credentialsattach of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501

        CredentialsAttach is a slice of attachments containing the issued credentials.  # noqa: E501

        :return: The credentialsattach of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._credentialsattach

    @credentialsattach.setter
    def credentialsattach(self, credentialsattach):
        """Sets the credentialsattach of this IssuecredentialpiidacceptrequestIssueCredential.

        CredentialsAttach is a slice of attachments containing the issued credentials.  # noqa: E501

        :param credentialsattach: The credentialsattach of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501
        :type: list[Attachment]
        """

        self._credentialsattach = credentialsattach

    @property
    def formats(self):
        """Gets the formats of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501

        Formats contains an entry for each credentials~attach array entry, providing the the value of the attachment @id and the verifiable credential format and version of the attachment.  # noqa: E501

        :return: The formats of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501
        :rtype: list[Format]
        """
        return self._formats

    @formats.setter
    def formats(self, formats):
        """Sets the formats of this IssuecredentialpiidacceptrequestIssueCredential.

        Formats contains an entry for each credentials~attach array entry, providing the the value of the attachment @id and the verifiable credential format and version of the attachment.  # noqa: E501

        :param formats: The formats of this IssuecredentialpiidacceptrequestIssueCredential.  # noqa: E501
        :type: list[Format]
        """

        self._formats = formats

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
        if issubclass(IssuecredentialpiidacceptrequestIssueCredential, dict):
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
        if not isinstance(other, IssuecredentialpiidacceptrequestIssueCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other