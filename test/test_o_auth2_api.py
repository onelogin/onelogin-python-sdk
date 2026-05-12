# coding: utf-8

import unittest

import onelogin
from onelogin.api.o_auth2_api import OAuth2Api  # noqa: E501
from onelogin.rest import ApiException


class TestOAuth2Api(unittest.TestCase):
    """OAuth2Api unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.o_auth2_api.OAuth2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_token(self):
        """Test case for generate_token

        Generate Token  # noqa: E501
        """
        pass

    def test_get_rate_limit(self):
        """Test case for get_rate_limit

        Get Rate Limit  # noqa: E501
        """
        pass

    def test_revoke_tokens(self):
        """Test case for revoke_tokens

        Revoke Tokens  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
