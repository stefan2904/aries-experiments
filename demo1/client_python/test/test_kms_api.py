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
from swagger_client.api.kms_api import KmsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestKmsApi(unittest.TestCase):
    """KmsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.kms_api.KmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_key_set(self):
        """Test case for create_key_set

        Create key set.  # noqa: E501
        """
        pass

    def test_import_key(self):
        """Test case for import_key

        Import key.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
