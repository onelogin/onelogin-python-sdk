# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.list_users200_response_inner import ListUsers200ResponseInner  # noqa: E501
from openapi_client.rest import ApiException

class TestListUsers200ResponseInner(unittest.TestCase):
    """ListUsers200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUsers200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListUsers200ResponseInner`
        """
        model = openapi_client.models.list_users200_response_inner.ListUsers200ResponseInner()  # noqa: E501
        if include_optional :
            return ListUsers200ResponseInner(
                id = 56, 
                username = '', 
                email = '', 
                firstname = '', 
                lastname = '', 
                title = '', 
                department = '', 
                company = '', 
                comment = '', 
                group_id = 56, 
                role_ids = [
                    56
                    ], 
                phone = '', 
                state = 0, 
                status = 0, 
                directory_id = 56, 
                trusted_idp_id = 56, 
                manager_ad_id = '', 
                manager_user_id = '', 
                samaccount_name = '', 
                member_of = '', 
                userprincipalname = '', 
                distinguished_name = '', 
                external_id = '', 
                activated_at = '', 
                last_login = '', 
                invitation_sent_at = '', 
                updated_at = '', 
                preferred_locale_code = '', 
                created_at = '', 
                invalid_login_attempts = 56, 
                locked_until = '', 
                password_changed_at = '', 
                password = '', 
                password_confirmation = '', 
                password_algorithm = '', 
                salt = ''
            )
        else :
            return ListUsers200ResponseInner(
        )
        """

    def testListUsers200ResponseInner(self):
        """Test ListUsers200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
