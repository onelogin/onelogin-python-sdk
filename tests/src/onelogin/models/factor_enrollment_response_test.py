# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.factor_enrollment_response import FactorEnrollmentResponse
import unittest

import datetime
from dateutil.tz import tzutc

# noinspection PySetFunctionToLiteral
class OneLogin_API_Model_FactorEnrollmentResponse_Test(unittest.TestCase):

    factor_enrollment_response_v1_payload = {"user_display_name": "Rich's Phone", "active": False, "state_token": "98e008497066bc2763c52342996e06358aab2e32", "state_token_expires_at": "2019-10-25T16:29:42Z", "auth_factor_name": "OneLogin SMS", "type_display_name": "OneLogin SMS", "id": 35510511, "device_id": 525509}

    factor_enrollment_response_v2_payload =   {"user_display_name": "OneLogin SMS", "id": "afc1a96d-2006-452a-a484-b2d084b00d76", "auth_factor_name": "SMS", "type_display_name": "OneLogin SMS", "user_id": "64515901", "device_id": "3920371", "expires_at": "2020-07-21T20:26:44Z" }

    factor_enrollment_response_v2_payload2 =   {"user_display_name": "OneLogin Voice", "id": "906621ef-0a42-4032-ae34-673d439f8326", "auth_factor_name": "OneLogin Voice", "type_display_name": "OneLogin Voice", "user_id": "87654321", "device_id": "1234567", "expires_at": "2021-01-27T20:34:05Z", "factor_data": {"verification_token": "123456"}}

    def getTestFactorEnrollmentResponseV1(self):
        test_factor_enrollment_response = FactorEnrollmentResponse({})
        test_factor_enrollment_response.active = False
        test_factor_enrollment_response.auth_factor_name = "OneLogin SMS"
        test_factor_enrollment_response.device_id = "525509"
        test_factor_enrollment_response.expires_at = datetime.datetime(2019, 10, 25, 16, 29, 42, tzinfo=tzutc())
        test_factor_enrollment_response.state_token = "98e008497066bc2763c52342996e06358aab2e32"
        test_factor_enrollment_response.type_display_name = "OneLogin SMS"
        test_factor_enrollment_response.user_display_name = "Rich's Phone"
        test_factor_enrollment_response.user_id = 35510511
        return test_factor_enrollment_response

    def getTestFactorEnrollmentResponseV2(self):
        test_factor_enrollment_response = FactorEnrollmentResponse({})
        test_factor_enrollment_response.auth_factor_name = "SMS"
        test_factor_enrollment_response.device_id = "3920371"
        test_factor_enrollment_response.expires_at = datetime.datetime(2020, 7, 21, 20, 26, 44, tzinfo=tzutc())
        test_factor_enrollment_response.id = "afc1a96d-2006-452a-a484-b2d084b00d76"
        test_factor_enrollment_response.type_display_name = "OneLogin SMS"
        test_factor_enrollment_response.user_display_name = "OneLogin SMS"
        test_factor_enrollment_response.user_id = 64515901
        return test_factor_enrollment_response

    def getTestFactorEnrollmentResponseV2_2(self):
        test_factor_enrollment_response = FactorEnrollmentResponse({})
        test_factor_enrollment_response.auth_factor_name = "OneLogin Voice"
        test_factor_enrollment_response.device_id = "1234567"
        test_factor_enrollment_response.expires_at = datetime.datetime(2021, 1, 27, 20, 34, 5, tzinfo=tzutc())
        test_factor_enrollment_response.factor_data = {'verification_token': '123456'}
        test_factor_enrollment_response.id = "906621ef-0a42-4032-ae34-673d439f8326"
        test_factor_enrollment_response.type_display_name = "OneLogin Voice"
        test_factor_enrollment_response.user_display_name = "OneLogin Voice"
        test_factor_enrollment_response.user_id = 87654321
        return test_factor_enrollment_response

    def testFactorEnrollmentResponse(self):
        """
        Tests the constructor method of the FactorEnrollmentResponse class
        Build a FactorEnrollmentResponse object and check if all the expected attributes exist
        as described in the FactorEnrollmentResponse Resource of the OneLogin API
        """
        factor_enrollment_response = FactorEnrollmentResponse(data={})
        expected_attributes = ['user_id', 'device_id', 'auth_factor_name', 'type_display_name', 'user_display_name', 'expires_at']
        for attr in expected_attributes:
            self.assertTrue(hasattr(factor_enrollment_response, attr), "FactorEnrollmentResponse has no attribute '{}'".format(attr))

    def testFactorEnrollmentResponseV1Payload(self):
        factor_enrollment_response = FactorEnrollmentResponse(self.factor_enrollment_response_v1_payload)
        self.assertEqual(factor_enrollment_response.__dict__, self.getTestFactorEnrollmentResponseV1().__dict__)

    def testFactorEnrollmentResponseV2Payload(self):
        factor_enrollment_response = FactorEnrollmentResponse(self.factor_enrollment_response_v2_payload)
        self.assertEqual(factor_enrollment_response.__dict__, self.getTestFactorEnrollmentResponseV2().__dict__)

    def testFactorEnrollmentResponseV2_2Payload(self):
        factor_enrollment_response = FactorEnrollmentResponse(self.factor_enrollment_response_v2_payload2)
        self.assertEqual(factor_enrollment_response.__dict__, self.getTestFactorEnrollmentResponseV2_2().__dict__)
