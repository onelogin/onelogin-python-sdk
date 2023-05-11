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
from onelogin.models.scope import Scope  # noqa: E501
from onelogin.rest import ApiException

class TestScope(unittest.TestCase):
    """Scope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Scope
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Scope`
        """
        model = onelogin.models.scope.Scope()  # noqa: E501
        if include_optional :
            return Scope(
                id = 25, 
                value = 'read:contacts', 
                description = 'Read some contacts'
            )
        else :
            return Scope(
        )
        """

    def testScope(self):
        """Test Scope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
