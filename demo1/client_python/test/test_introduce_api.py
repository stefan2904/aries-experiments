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
from swagger_client.api.introduce_api import IntroduceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIntroduceApi(unittest.TestCase):
    """IntroduceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.introduce_api.IntroduceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_introduce_accept_problem_report(self):
        """Test case for introduce_accept_problem_report

        Accepts a problem report.  # noqa: E501
        """
        pass

    def test_introduce_accept_proposal(self):
        """Test case for introduce_accept_proposal

        Accepts a proposal.  # noqa: E501
        """
        pass

    def test_introduce_accept_proposal_with_oob_request(self):
        """Test case for introduce_accept_proposal_with_oob_request

        Accepts a proposal with OOBRequest.  # noqa: E501
        """
        pass

    def test_introduce_accept_request_with_public_oob_request(self):
        """Test case for introduce_accept_request_with_public_oob_request

        Accept a request with public OOBRequest.  # noqa: E501
        """
        pass

    def test_introduce_accept_request_with_recipients(self):
        """Test case for introduce_accept_request_with_recipients

        Accept a request with recipients.  # noqa: E501
        """
        pass

    def test_introduce_actions(self):
        """Test case for introduce_actions

        Returns pending actions that have not yet to be executed or cancelled.  # noqa: E501
        """
        pass

    def test_introduce_decline_proposal(self):
        """Test case for introduce_decline_proposal

        Declines a proposal.  # noqa: E501
        """
        pass

    def test_introduce_decline_request(self):
        """Test case for introduce_decline_request

        Declines a request.  # noqa: E501
        """
        pass

    def test_introduce_send_proposal(self):
        """Test case for introduce_send_proposal

        Sends a proposal.  # noqa: E501
        """
        pass

    def test_introduce_send_proposal_with_oob_request(self):
        """Test case for introduce_send_proposal_with_oob_request

        Sends a proposal with OOBRequest.  # noqa: E501
        """
        pass

    def test_introduce_send_request(self):
        """Test case for introduce_send_request

        Sends a request.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
