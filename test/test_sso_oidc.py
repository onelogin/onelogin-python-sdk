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
from onelogin.models.sso_oidc import SsoOidc  # noqa: E501
from onelogin.rest import ApiException

class TestSsoOidc(unittest.TestCase):
    """SsoOidc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SsoOidc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SsoOidc`
        """
        model = onelogin.models.sso_oidc.SsoOidc()  # noqa: E501
        if include_optional :
            return SsoOidc(
                client_id = '78d1d040-20c9-0136-5146-067351775fae92920'
            )
        else :
            return SsoOidc(
        )
        """

    def testSsoOidc(self):
        """Test SsoOidc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
