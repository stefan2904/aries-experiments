# coding: utf-8

"""
    (Aries Agent REST Server) of VC4SM University.

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.verifiable_api import VerifiableApi  # noqa: E501
from swagger_client.rest import ApiException


class TestVerifiableApi(unittest.TestCase):
    """VerifiableApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.verifiable_api.VerifiableApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_presentation_req(self):
        """Test case for generate_presentation_req

        Generates the verifiable presentation from a verifiable credential.  # noqa: E501
        """
        pass

    def test_get_credential_by_name_req(self):
        """Test case for get_credential_by_name_req

        Retrieves the verifiable credential by name.  # noqa: E501
        """
        pass

    def test_get_credential_req(self):
        """Test case for get_credential_req

        Retrieves the verifiable credential.  # noqa: E501
        """
        pass

    def test_get_credentials(self):
        """Test case for get_credentials

        Retrieves the verifiable credentials.  # noqa: E501
        """
        pass

    def test_get_presentation_req(self):
        """Test case for get_presentation_req

        Retrieves the verifiable presentation.  # noqa: E501
        """
        pass

    def test_remove_credential_by_name_req(self):
        """Test case for remove_credential_by_name_req

        Removes a verifiable credential by name.  # noqa: E501
        """
        pass

    def test_remove_presentation_by_name_req(self):
        """Test case for remove_presentation_by_name_req

        Removes a verifiable presentation by name.  # noqa: E501
        """
        pass

    def test_save_credential_req(self):
        """Test case for save_credential_req

        Saves the verifiable credential.  # noqa: E501
        """
        pass

    def test_save_presentation_req(self):
        """Test case for save_presentation_req

        Saves the verifiable presentation.  # noqa: E501
        """
        pass

    def test_sign_credential_req(self):
        """Test case for sign_credential_req

        Signs given credential.  # noqa: E501
        """
        pass

    def test_validate_credential_req(self):
        """Test case for validate_credential_req

        Validates the verifiable credential.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
