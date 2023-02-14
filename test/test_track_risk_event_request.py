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
from openapi_client.models.track_risk_event_request import TrackRiskEventRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestTrackRiskEventRequest(unittest.TestCase):
    """TrackRiskEventRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TrackRiskEventRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackRiskEventRequest`
        """
        model = openapi_client.models.track_risk_event_request.TrackRiskEventRequest()  # noqa: E501
        if include_optional :
            return TrackRiskEventRequest(
                verb = '', 
                ip = '', 
                user_agent = '', 
                user = openapi_client.models.track_risk_event_request_user.trackRiskEvent_request_user(
                    id = '', 
                    name = '', 
                    authenticated = True, ), 
                source = openapi_client.models.list_risk_rules_200_response_inner_source.listRiskRules_200_response_inner_source(
                    id = '', 
                    name = '', ), 
                session = openapi_client.models.track_risk_event_request_session.trackRiskEvent_request_session(
                    id = '', ), 
                device = openapi_client.models.track_risk_event_request_device.trackRiskEvent_request_device(
                    id = '', ), 
                fp = '', 
                published = ''
            )
        else :
            return TrackRiskEventRequest(
                verb = '',
                ip = '',
                user_agent = '',
                user = openapi_client.models.track_risk_event_request_user.trackRiskEvent_request_user(
                    id = '', 
                    name = '', 
                    authenticated = True, ),
        )
        """

    def testTrackRiskEventRequest(self):
        """Test TrackRiskEventRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
