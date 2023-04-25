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
from onelogin.models.request_brand import RequestBrand  # noqa: E501
from onelogin.rest import ApiException

class TestRequestBrand(unittest.TestCase):
    """RequestBrand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RequestBrand
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestBrand`
        """
        model = onelogin.models.request_brand.RequestBrand()  # noqa: E501
        if include_optional :
            return RequestBrand(
                enabled = True, 
                name = 'Acme Branding', 
                custom_support_enabled = False, 
                custom_color = '#1298b4', 
                custom_accent_color = '#b60012', 
                custom_masking_color = '#beefed', 
                custom_masking_opacity = 40, 
                enable_custom_label_for_login_screen = True, 
                custom_label_text_for_login_screen = 'ACME Username or Email', 
                login_instruction_title = 'ACME Login Instructions', 
                login_instruction = 'To login, enter your ACME Username or Email. Reach out to help.desk@acme.org if you have trouble logging in.', 
                hide_onelogin_footer = True, 
                mfa_enrollment_message = 'You must register with the OneLogin Protect app in order to login', 
                background = '/9j/4AAQSkZJRgAB...J3a+IvMu7D8T/9k=', 
                logo = 'iVBORw0KGgoAAAAN...AABJRU5ErkJggg=='
            )
        else :
            return RequestBrand(
                name = 'Acme Branding',
        )
        """

    def testRequestBrand(self):
        """Test RequestBrand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
