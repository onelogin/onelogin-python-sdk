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
from openapi_client.models.get_user_apps200_response_inner import GetUserApps200ResponseInner  # noqa: E501
from openapi_client.rest import ApiException

class TestGetUserApps200ResponseInner(unittest.TestCase):
    """GetUserApps200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetUserApps200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserApps200ResponseInner`
        """
        model = openapi_client.models.get_user_apps200_response_inner.GetUserApps200ResponseInner()  # noqa: E501
        if include_optional :
            return GetUserApps200ResponseInner(
                id = 56, 
                icon_url = '', 
                extension = True, 
                login_id = 56, 
                name = '', 
                provisioning_status = 'enabling', 
                provisioning_state = 'unknown', 
                provisioning_enabled = True
            )
        else :
            return GetUserApps200ResponseInner(
        )
        """

    def testGetUserApps200ResponseInner(self):
        """Test GetUserApps200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
