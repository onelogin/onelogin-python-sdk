# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import onelogin
from onelogin.api.multi_factor_authentication_v1_api import MultiFactorAuthenticationV1Api  # noqa: E501
from onelogin.rest import ApiException


class TestMultiFactorAuthenticationV1Api(unittest.TestCase):
    """MultiFactorAuthenticationV1Api unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.multi_factor_authentication_v1_api.MultiFactorAuthenticationV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_mfa_factors(self):
        """Test case for activate_mfa_factors

        Activate a Factor  # noqa: E501
        """
        pass

    def test_enroll_mfa_factor(self):
        """Test case for enroll_mfa_factor

        Enroll a Factor  # noqa: E501
        """
        pass

    def test_generate_mf_atoken(self):
        """Test case for generate_mf_atoken

        Generate Temp MFA Token  # noqa: E501
        """
        pass

    def test_get_enrolled_factors(self):
        """Test case for get_enrolled_factors

        Get Enrolled Factors  # noqa: E501
        """
        pass

    def test_get_mfa_factors(self):
        """Test case for get_mfa_factors

        Get Available Factors  # noqa: E501
        """
        pass

    def test_remove_mfa_factors(self):
        """Test case for remove_mfa_factors

        Remove an Enrolled Factor  # noqa: E501
        """
        pass

    def test_verify_mfa_factor(self):
        """Test case for verify_mfa_factor

        Verify a Factor  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
