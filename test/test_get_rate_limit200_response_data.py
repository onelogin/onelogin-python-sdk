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
from openapi_client.models.get_rate_limit200_response_data import GetRateLimit200ResponseData  # noqa: E501
from openapi_client.rest import ApiException

class TestGetRateLimit200ResponseData(unittest.TestCase):
    """GetRateLimit200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRateLimit200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRateLimit200ResponseData`
        """
        model = openapi_client.models.get_rate_limit200_response_data.GetRateLimit200ResponseData()  # noqa: E501
        if include_optional :
            return GetRateLimit200ResponseData(
                x_rate_limit_limit = 5000, 
                x_rate_limit_remaining = 4988, 
                x_rate_limit_reset = 832
            )
        else :
            return GetRateLimit200ResponseData(
        )
        """

    def testGetRateLimit200ResponseData(self):
        """Test GetRateLimit200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
