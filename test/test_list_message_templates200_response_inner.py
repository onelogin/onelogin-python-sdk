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
from onelogin.models.list_message_templates200_response_inner import ListMessageTemplates200ResponseInner  # noqa: E501
from onelogin.rest import ApiException

class TestListMessageTemplates200ResponseInner(unittest.TestCase):
    """ListMessageTemplates200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListMessageTemplates200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListMessageTemplates200ResponseInner`
        """
        model = onelogin.models.list_message_templates200_response_inner.ListMessageTemplates200ResponseInner()  # noqa: E501
        if include_optional :
            return ListMessageTemplates200ResponseInner(
                id = 912, 
                enabled = True, 
                name = 'ACME'
            )
        else :
            return ListMessageTemplates200ResponseInner(
        )
        """

    def testListMessageTemplates200ResponseInner(self):
        """Test ListMessageTemplates200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
