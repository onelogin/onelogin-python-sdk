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
from onelogin.models.update_password_insecure_request import UpdatePasswordInsecureRequest  # noqa: E501
from onelogin.rest import ApiException

class TestUpdatePasswordInsecureRequest(unittest.TestCase):
    """UpdatePasswordInsecureRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdatePasswordInsecureRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdatePasswordInsecureRequest`
        """
        model = onelogin.models.update_password_insecure_request.UpdatePasswordInsecureRequest()  # noqa: E501
        if include_optional :
            return UpdatePasswordInsecureRequest(
                password = '<password>', 
                password_confirmation = '<password_confirmation>', 
                validate_policy = False
            )
        else :
            return UpdatePasswordInsecureRequest(
                password = '<password>',
                password_confirmation = '<password_confirmation>',
        )
        """

    def testUpdatePasswordInsecureRequest(self):
        """Test UpdatePasswordInsecureRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
