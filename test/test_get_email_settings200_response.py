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
from onelogin.models.get_email_settings200_response import GetEmailSettings200Response  # noqa: E501
from onelogin.rest import ApiException

class TestGetEmailSettings200Response(unittest.TestCase):
    """GetEmailSettings200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEmailSettings200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEmailSettings200Response`
        """
        model = onelogin.models.get_email_settings200_response.GetEmailSettings200Response()  # noqa: E501
        if include_optional :
            return GetEmailSettings200Response(
                mode = 'onelogin_email', 
                address = 'smtp.sendgrid.net', 
                use_tls = True, 
                var_from = 'email@example.com', 
                domain = 'example.com', 
                user_name = 'user-name', 
                password = 'password', 
                port = 587
            )
        else :
            return GetEmailSettings200Response(
                address = 'smtp.sendgrid.net',
                var_from = 'email@example.com',
                domain = 'example.com',
        )
        """

    def testGetEmailSettings200Response(self):
        """Test GetEmailSettings200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
