# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import onelogin
from onelogin.models.get_risk_score200_response import GetRiskScore200Response  # noqa: E501
from onelogin.rest import ApiException

class TestGetRiskScore200Response(unittest.TestCase):
    """GetRiskScore200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRiskScore200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRiskScore200Response`
        """
        model = onelogin.models.get_risk_score200_response.GetRiskScore200Response()  # noqa: E501
        if include_optional :
            return GetRiskScore200Response(
                score = 0, 
                triggers = [
                    ''
                    ]
            )
        else :
            return GetRiskScore200Response(
        )
        """

    def testGetRiskScore200Response(self):
        """Test GetRiskScore200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
