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
from onelogin.models.rate_limit import RateLimit  # noqa: E501
from onelogin.rest import ApiException

class TestRateLimit(unittest.TestCase):
    """RateLimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RateLimit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RateLimit`
        """
        model = onelogin.models.rate_limit.RateLimit()  # noqa: E501
        if include_optional :
            return RateLimit(
                x_rate_limit_limit = 5000, 
                x_rate_limit_remaining = 4988, 
                x_rate_limit_reset = 832
            )
        else :
            return RateLimit(
        )
        """

    def testRateLimit(self):
        """Test RateLimit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
