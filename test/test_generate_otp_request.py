# coding: utf-8

import unittest
import datetime

import onelogin
from onelogin.models.generate_otp_request import GenerateOTPRequest  # noqa: E501
from onelogin.rest import ApiException

class TestGenerateOTPRequest(unittest.TestCase):
    """GenerateOTPRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateOTPRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateOTPRequest`
        """
        model = onelogin.models.generate_otp_request.GenerateOTPRequest()  # noqa: E501
        if include_optional :
            return GenerateOTPRequest(
                expires_in = 300, 
                reusable = True
            )
        else :
            return GenerateOTPRequest(
        )
        """

    def testGenerateOTPRequest(self):
        """Test GenerateOTPRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
