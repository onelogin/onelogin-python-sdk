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
from onelogin.models.get_role_apps200_response_inner import GetRoleApps200ResponseInner  # noqa: E501
from onelogin.rest import ApiException

class TestGetRoleApps200ResponseInner(unittest.TestCase):
    """GetRoleApps200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRoleApps200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRoleApps200ResponseInner`
        """
        model = onelogin.models.get_role_apps200_response_inner.GetRoleApps200ResponseInner()  # noqa: E501
        if include_optional :
            return GetRoleApps200ResponseInner(
                id = 56, 
                name = '', 
                icon_url = ''
            )
        else :
            return GetRoleApps200ResponseInner(
        )
        """

    def testGetRoleApps200ResponseInner(self):
        """Test GetRoleApps200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
