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
from onelogin.models.list_conditions200_response_inner import ListConditions200ResponseInner  # noqa: E501
from onelogin.rest import ApiException

class TestListConditions200ResponseInner(unittest.TestCase):
    """ListConditions200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConditions200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConditions200ResponseInner`
        """
        model = onelogin.models.list_conditions200_response_inner.ListConditions200ResponseInner()  # noqa: E501
        if include_optional :
            return ListConditions200ResponseInner(
                name = 'MemberOf', 
                value = 'member_of'
            )
        else :
            return ListConditions200ResponseInner(
        )
        """

    def testListConditions200ResponseInner(self):
        """Test ListConditions200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
