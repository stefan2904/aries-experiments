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
from swagger_client.api.message_api import MessageApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMessageApi(unittest.TestCase):
    """MessageApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.message_api.MessageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_register_msg_svc(self):
        """Test case for register_msg_svc

        """
        pass

    def test_send_new_message(self):
        """Test case for send_new_message

        """
        pass

    def test_send_reply_message(self):
        """Test case for send_reply_message

        """
        pass

    def test_services(self):
        """Test case for services

        """
        pass

    def test_unregister_msg_svc(self):
        """Test case for unregister_msg_svc

        """
        pass


if __name__ == '__main__':
    unittest.main()
