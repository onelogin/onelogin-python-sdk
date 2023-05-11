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
from onelogin.models.message_template_template_one_of import MessageTemplateTemplateOneOf  # noqa: E501
from onelogin.rest import ApiException

class TestMessageTemplateTemplateOneOf(unittest.TestCase):
    """MessageTemplateTemplateOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessageTemplateTemplateOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageTemplateTemplateOneOf`
        """
        model = onelogin.models.message_template_template_one_of.MessageTemplateTemplateOneOf()  # noqa: E501
        if include_optional :
            return MessageTemplateTemplateOneOf(
                subject = 'Email MFA App Verification Code', 
                html = '<html><head></head><body><p>Here is the code: {{otp_code}}</p></body></html>', 
                plain = 'Here is the code: {{otp_code}}'
            )
        else :
            return MessageTemplateTemplateOneOf(
                subject = 'Email MFA App Verification Code',
                html = '<html><head></head><body><p>Here is the code: {{otp_code}}</p></body></html>',
                plain = 'Here is the code: {{otp_code}}',
        )
        """

    def testMessageTemplateTemplateOneOf(self):
        """Test MessageTemplateTemplateOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
