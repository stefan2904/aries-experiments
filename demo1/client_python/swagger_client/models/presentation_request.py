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


class PresentationRequest(object):
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
        'challenge': 'str',
        'created': 'datetime',
        'did': 'str',
        'domain': 'str',
        'presentation': 'object',
        'signature_type': 'str',
        'skip_verify': 'bool',
        'verifiable_credential': 'list[object]',
        'verification_method': 'str'
    }

    attribute_map = {
        'challenge': 'challenge',
        'created': 'created',
        'did': 'did',
        'domain': 'domain',
        'presentation': 'presentation',
        'signature_type': 'signatureType',
        'skip_verify': 'skipVerify',
        'verifiable_credential': 'verifiableCredential',
        'verification_method': 'verificationMethod'
    }

    def __init__(self, challenge=None, created=None, did=None, domain=None, presentation=None, signature_type=None, skip_verify=None, verifiable_credential=None, verification_method=None):  # noqa: E501
        """PresentationRequest - a model defined in Swagger"""  # noqa: E501

        self._challenge = None
        self._created = None
        self._did = None
        self._domain = None
        self._presentation = None
        self._signature_type = None
        self._skip_verify = None
        self._verifiable_credential = None
        self._verification_method = None
        self.discriminator = None

        if challenge is not None:
            self.challenge = challenge
        if created is not None:
            self.created = created
        if did is not None:
            self.did = did
        if domain is not None:
            self.domain = domain
        if presentation is not None:
            self.presentation = presentation
        if signature_type is not None:
            self.signature_type = signature_type
        if skip_verify is not None:
            self.skip_verify = skip_verify
        if verifiable_credential is not None:
            self.verifiable_credential = verifiable_credential
        if verification_method is not None:
            self.verification_method = verification_method

    @property
    def challenge(self):
        """Gets the challenge of this PresentationRequest.  # noqa: E501

        Challenge is a random or pseudo-random value option authentication  # noqa: E501

        :return: The challenge of this PresentationRequest.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this PresentationRequest.

        Challenge is a random or pseudo-random value option authentication  # noqa: E501

        :param challenge: The challenge of this PresentationRequest.  # noqa: E501
        :type: str
        """

        self._challenge = challenge

    @property
    def created(self):
        """Gets the created of this PresentationRequest.  # noqa: E501

        Created date of the proof. If omitted current system time will be used.  # noqa: E501

        :return: The created of this PresentationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PresentationRequest.

        Created date of the proof. If omitted current system time will be used.  # noqa: E501

        :param created: The created of this PresentationRequest.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def did(self):
        """Gets the did of this PresentationRequest.  # noqa: E501


        :return: The did of this PresentationRequest.  # noqa: E501
        :rtype: str
        """
        return self._did

    @did.setter
    def did(self, did):
        """Sets the did of this PresentationRequest.


        :param did: The did of this PresentationRequest.  # noqa: E501
        :type: str
        """

        self._did = did

    @property
    def domain(self):
        """Gets the domain of this PresentationRequest.  # noqa: E501

        Domain is operational domain of a digital proof.  # noqa: E501

        :return: The domain of this PresentationRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PresentationRequest.

        Domain is operational domain of a digital proof.  # noqa: E501

        :param domain: The domain of this PresentationRequest.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def presentation(self):
        """Gets the presentation of this PresentationRequest.  # noqa: E501


        :return: The presentation of this PresentationRequest.  # noqa: E501
        :rtype: object
        """
        return self._presentation

    @presentation.setter
    def presentation(self, presentation):
        """Sets the presentation of this PresentationRequest.


        :param presentation: The presentation of this PresentationRequest.  # noqa: E501
        :type: object
        """

        self._presentation = presentation

    @property
    def signature_type(self):
        """Gets the signature_type of this PresentationRequest.  # noqa: E501

        SignatureType signature type used for signing  # noqa: E501

        :return: The signature_type of this PresentationRequest.  # noqa: E501
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this PresentationRequest.

        SignatureType signature type used for signing  # noqa: E501

        :param signature_type: The signature_type of this PresentationRequest.  # noqa: E501
        :type: str
        """

        self._signature_type = signature_type

    @property
    def skip_verify(self):
        """Gets the skip_verify of this PresentationRequest.  # noqa: E501

        SkipVerify can be used to skip verification of `VerifiableCredentials` provided.  # noqa: E501

        :return: The skip_verify of this PresentationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._skip_verify

    @skip_verify.setter
    def skip_verify(self, skip_verify):
        """Sets the skip_verify of this PresentationRequest.

        SkipVerify can be used to skip verification of `VerifiableCredentials` provided.  # noqa: E501

        :param skip_verify: The skip_verify of this PresentationRequest.  # noqa: E501
        :type: bool
        """

        self._skip_verify = skip_verify

    @property
    def verifiable_credential(self):
        """Gets the verifiable_credential of this PresentationRequest.  # noqa: E501


        :return: The verifiable_credential of this PresentationRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._verifiable_credential

    @verifiable_credential.setter
    def verifiable_credential(self, verifiable_credential):
        """Sets the verifiable_credential of this PresentationRequest.


        :param verifiable_credential: The verifiable_credential of this PresentationRequest.  # noqa: E501
        :type: list[object]
        """

        self._verifiable_credential = verifiable_credential

    @property
    def verification_method(self):
        """Gets the verification_method of this PresentationRequest.  # noqa: E501

        VerificationMethod is the URI of the verificationMethod used for the proof.  # noqa: E501

        :return: The verification_method of this PresentationRequest.  # noqa: E501
        :rtype: str
        """
        return self._verification_method

    @verification_method.setter
    def verification_method(self, verification_method):
        """Sets the verification_method of this PresentationRequest.

        VerificationMethod is the URI of the verificationMethod used for the proof.  # noqa: E501

        :param verification_method: The verification_method of this PresentationRequest.  # noqa: E501
        :type: str
        """

        self._verification_method = verification_method

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
        if issubclass(PresentationRequest, dict):
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
        if not isinstance(other, PresentationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other