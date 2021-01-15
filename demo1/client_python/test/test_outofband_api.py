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
from swagger_client.api.outofband_api import OutofbandApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOutofbandApi(unittest.TestCase):
    """OutofbandApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.outofband_api.OutofbandApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_outofband_accept_invitation(self):
        """Test case for outofband_accept_invitation

        Accepts an invitation.  # noqa: E501
        """
        pass

    def test_outofband_accept_request(self):
        """Test case for outofband_accept_request

        Accepts a request.  # noqa: E501
        """
        pass

    def test_outofband_action_continue(self):
        """Test case for outofband_action_continue

        Allows continuing with the protocol after an action event was triggered.  # noqa: E501
        """
        pass

    def test_outofband_action_stop(self):
        """Test case for outofband_action_stop

        Stops the protocol after an action event was triggered.  # noqa: E501
        """
        pass

    def test_outofband_actions(self):
        """Test case for outofband_actions

        Returns pending actions that have not yet to be executed or cancelled.  # noqa: E501
        """
        pass

    def test_outofband_create_invitation(self):
        """Test case for outofband_create_invitation

        Creates an invitation.  # noqa: E501
        """
        pass

    def test_outofband_create_request(self):
        """Test case for outofband_create_request

        Creates a request.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()