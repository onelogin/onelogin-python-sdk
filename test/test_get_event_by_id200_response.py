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
from openapi_client.models.get_event_by_id200_response import GetEventById200Response  # noqa: E501
from openapi_client.rest import ApiException

class TestGetEventById200Response(unittest.TestCase):
    """GetEventById200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEventById200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEventById200Response`
        """
        model = openapi_client.models.get_event_by_id200_response.GetEventById200Response()  # noqa: E501
        if include_optional :
            return GetEventById200Response(
                status = {"error":false,"code":200,"type":"success","message":"success"}, 
                data = openapi_client.models.get_events_200_response_data_inner.getEvents_200_response_data_inner(
                    account_id = 56, 
                    actor_system = '', 
                    actor_user_id = 56, 
                    actor_user_name = '', 
                    adc_id = 56, 
                    app_name = '', 
                    app_id = 56, 
                    assumed_by_superadmin_or_reseller = 56, 
                    assuming_acting_user_id = 56, 
                    certificate_id = 56, 
                    client_id = '', 
                    created_at = '', 
                    custom_message = '', 
                    directory_sync_run_id = 56, 
                    error_description = '', 
                    event_type_id = 1, 
                    group_name = '', 
                    group_id = 56, 
                    id = 56, 
                    ipaddr = '', 
                    mapping_id = 56, 
                    notes = '', 
                    object_id = 56, 
                    otp_device_id = 56, 
                    otp_device_name = '', 
                    param = '', 
                    policy_id = 56, 
                    policy_name = '', 
                    policy_type = '', 
                    privilege_id = 56, 
                    proxy_ip = '', 
                    radius_config_id = 56, 
                    resolved_at = '', 
                    resource_type_id = 56, 
                    risk_cookie_id = '', 
                    risk_reasons = '', 
                    risk_score = 56, 
                    role_id = 56, 
                    role_name = '', 
                    service_directory_id = 56, 
                    solved = True, 
                    trusted_idp_id = 56, 
                    user_field_id = 56, 
                    user_id = 56, 
                    user_name = '', )
            )
        else :
            return GetEventById200Response(
        )
        """

    def testGetEventById200Response(self):
        """Test GetEventById200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
