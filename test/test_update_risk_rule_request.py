# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.update_risk_rule_request import UpdateRiskRuleRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestUpdateRiskRuleRequest(unittest.TestCase):
    """UpdateRiskRuleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateRiskRuleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateRiskRuleRequest`
        """
        model = openapi_client.models.update_risk_rule_request.UpdateRiskRuleRequest()  # noqa: E501
        if include_optional :
            return UpdateRiskRuleRequest(
                id = ''
            )
        else :
            return UpdateRiskRuleRequest(
        )
        """

    def testUpdateRiskRuleRequest(self):
        """Test UpdateRiskRuleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
