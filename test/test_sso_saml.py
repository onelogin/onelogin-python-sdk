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
from onelogin.models.sso_saml import SsoSaml  # noqa: E501
from onelogin.rest import ApiException

class TestSsoSaml(unittest.TestCase):
    """SsoSaml unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SsoSaml
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SsoSaml`
        """
        model = onelogin.models.sso_saml.SsoSaml()  # noqa: E501
        if include_optional :
            return SsoSaml(
                metadata_url = 'https://app.onelogin.com/saml/metadata/5772393d-2ad3-47d6-a64f-2339b1028291', 
                acs_url = 'https://sharkbytes.onelogin.com/trust/saml2/http-post/sso/928532', 
                sls_url = 'https://sharkbytes.onelogin.com/trust/saml2/http-redirect/slo/928532', 
                issuer = 'https://app.onelogin.com/saml/metadata/5772393d-2ad3-47d6-a64f-2339b1028291', 
                certificate = onelogin.models.sso_saml_certificate.sso_saml_certificate(
                    id = 170216, 
                    name = 'My Companies SAML Certificate', 
                    value = 'c6d814d032f000d9c03bc79727265', )
            )
        else :
            return SsoSaml(
        )
        """

    def testSsoSaml(self):
        """Test SsoSaml"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
