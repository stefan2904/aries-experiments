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
from swagger_client.api.present_proof_api import PresentProofApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPresentProofApi(unittest.TestCase):
    """PresentProofApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.present_proof_api.PresentProofApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_present_proof_accept_presentation(self):
        """Test case for present_proof_accept_presentation

        Accepts a presentation.  # noqa: E501
        """
        pass

    def test_present_proof_accept_problem_report(self):
        """Test case for present_proof_accept_problem_report

        Accepts a problem report.  # noqa: E501
        """
        pass

    def test_present_proof_accept_propose_presentation(self):
        """Test case for present_proof_accept_propose_presentation

        Accepts a propose presentation.  # noqa: E501
        """
        pass

    def test_present_proof_accept_request_presentation(self):
        """Test case for present_proof_accept_request_presentation

        Accepts a request presentation.  # noqa: E501
        """
        pass

    def test_present_proof_actions(self):
        """Test case for present_proof_actions

        Returns pending actions that have not yet to be executed or cancelled.  # noqa: E501
        """
        pass

    def test_present_proof_decline_presentation(self):
        """Test case for present_proof_decline_presentation

        Declines a presentation.  # noqa: E501
        """
        pass

    def test_present_proof_decline_propose_presentation(self):
        """Test case for present_proof_decline_propose_presentation

        Declines a propose presentation.  # noqa: E501
        """
        pass

    def test_present_proof_decline_request_presentation(self):
        """Test case for present_proof_decline_request_presentation

        Declines a request presentation.  # noqa: E501
        """
        pass

    def test_present_proof_negotiate_request_presentation(self):
        """Test case for present_proof_negotiate_request_presentation

        Is used by the Prover to counter a presentation request they received with a proposal.  # noqa: E501
        """
        pass

    def test_present_proof_send_propose_presentation(self):
        """Test case for present_proof_send_propose_presentation

        Sends a propose presentation.  # noqa: E501
        """
        pass

    def test_present_proof_send_request_presentation(self):
        """Test case for present_proof_send_request_presentation

        Sends a request presentation.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
