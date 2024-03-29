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
from onelogin.models.get_mfa_factors200_response_data_auth_factors_inner import GetMFAFactors200ResponseDataAuthFactorsInner  # noqa: E501
from onelogin.rest import ApiException

class TestGetMFAFactors200ResponseDataAuthFactorsInner(unittest.TestCase):
    """GetMFAFactors200ResponseDataAuthFactorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetMFAFactors200ResponseDataAuthFactorsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMFAFactors200ResponseDataAuthFactorsInner`
        """
        model = onelogin.models.get_mfa_factors200_response_data_auth_factors_inner.GetMFAFactors200ResponseDataAuthFactorsInner()  # noqa: E501
        if include_optional :
            return GetMFAFactors200ResponseDataAuthFactorsInner(
                name = 'Onelogin SMS', 
                factor_id = 16282
            )
        else :
            return GetMFAFactors200ResponseDataAuthFactorsInner(
        )
        """

    def testGetMFAFactors200ResponseDataAuthFactorsInner(self):
        """Test GetMFAFactors200ResponseDataAuthFactorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
