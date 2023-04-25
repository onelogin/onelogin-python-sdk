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
from onelogin.models.activate_mfa_factors_request import ActivateMfaFactorsRequest  # noqa: E501
from onelogin.rest import ApiException

class TestActivateMfaFactorsRequest(unittest.TestCase):
    """ActivateMfaFactorsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ActivateMfaFactorsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivateMfaFactorsRequest`
        """
        model = onelogin.models.activate_mfa_factors_request.ActivateMfaFactorsRequest()  # noqa: E501
        if include_optional :
            return ActivateMfaFactorsRequest(
                state_token_expires_in = 300, 
                numeric_sms_otp = True, 
                sms_message = 'This is a security code from ABC Co {{otp_code}}. It expires in {{expiration}} minutes.'
            )
        else :
            return ActivateMfaFactorsRequest(
        )
        """

    def testActivateMfaFactorsRequest(self):
        """Test ActivateMfaFactorsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
