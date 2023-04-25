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
from onelogin.models.get_events200_response import GetEvents200Response  # noqa: E501
from onelogin.rest import ApiException

class TestGetEvents200Response(unittest.TestCase):
    """GetEvents200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEvents200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEvents200Response`
        """
        model = onelogin.models.get_events200_response.GetEvents200Response()  # noqa: E501
        if include_optional :
            return GetEvents200Response(
                status = onelogin.models.error.Error(
                    error = False, 
                    code = 200, 
                    type = 'Success', 
                    message = 'Success', ), 
                pagination = onelogin.models.get_events_200_response_pagination.getEvents_200_response_pagination(
                    before_cursor = 'null', 
                    after_cursor = 'xWNjb3VudF9pZDo6OjUzNDEzLS0jI2lkOjo6OTA0MjU3NTQ2', 
                    previous_link = 'null', 
                    next_link = 'https://your-api-subdomain.onelogin.com/api/1/events?after_cursor=xWNjb3VudF9pZDo6OjUzNDEzLS0jI2lkOjo6OTA0MjU3NTQ2', ), 
                data = [
                    onelogin.models.event.event(
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
                    ]
            )
        else :
            return GetEvents200Response(
        )
        """

    def testGetEvents200Response(self):
        """Test GetEvents200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
