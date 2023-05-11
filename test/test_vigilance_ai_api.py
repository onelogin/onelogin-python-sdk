# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import onelogin
from onelogin.api.vigilance_ai_api import VigilanceAIApi  # noqa: E501
from onelogin.rest import ApiException


class TestVigilanceAIApi(unittest.TestCase):
    """VigilanceAIApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.vigilance_ai_api.VigilanceAIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_risk_rule(self):
        """Test case for create_risk_rule

        Create Rule  # noqa: E501
        """
        pass

    def test_delete_risk_rule(self):
        """Test case for delete_risk_rule

        Delete Rule  # noqa: E501
        """
        pass

    def test_get_risk_rule(self):
        """Test case for get_risk_rule

        get Risk Rule  # noqa: E501
        """
        pass

    def test_get_risk_score(self):
        """Test case for get_risk_score

        Get a Risk Score  # noqa: E501
        """
        pass

    def test_get_risk_scores(self):
        """Test case for get_risk_scores

        Get Score Summary  # noqa: E501
        """
        pass

    def test_list_risk_rules(self):
        """Test case for list_risk_rules

        List Rules  # noqa: E501
        """
        pass

    def test_track_risk_event(self):
        """Test case for track_risk_event

        Track an Event  # noqa: E501
        """
        pass

    def test_update_risk_rule(self):
        """Test case for update_risk_rule

        Update Rule  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
