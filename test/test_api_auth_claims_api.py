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
from onelogin.api.api_auth_claims_api import APIAuthClaimsApi  # noqa: E501
from onelogin.rest import ApiException


class TestAPIAuthClaimsApi(unittest.TestCase):
    """APIAuthClaimsApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.api_auth_claims_api.APIAuthClaimsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_auth_claim(self):
        """Test case for create_auth_claim

        Create Api Auth Server Claim  # noqa: E501
        """
        pass

    def test_delete_auth_claim(self):
        """Test case for delete_auth_claim

        Delete Api Auth Server Claim  # noqa: E501
        """
        pass

    def test_get_authclaims(self):
        """Test case for get_authclaims

        Get Api Auth Server claims  # noqa: E501
        """
        pass

    def test_update_claim(self):
        """Test case for update_claim

        Update Api Auth Server Claim  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
