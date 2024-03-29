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
from onelogin.models.get_custom_attributes200_response import GetCustomAttributes200Response  # noqa: E501
from onelogin.rest import ApiException

class TestGetCustomAttributes200Response(unittest.TestCase):
    """GetCustomAttributes200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetCustomAttributes200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCustomAttributes200Response`
        """
        model = onelogin.models.get_custom_attributes200_response.GetCustomAttributes200Response()  # noqa: E501
        if include_optional :
            return GetCustomAttributes200Response(
                status = onelogin.models.error.Error(
                    error = False, 
                    code = 200, 
                    type = 'Success', 
                    message = 'Success', ), 
                data = [["alias","branch"]]
            )
        else :
            return GetCustomAttributes200Response(
        )
        """

    def testGetCustomAttributes200Response(self):
        """Test GetCustomAttributes200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
