# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.otp_device import OTP_Device
import unittest
import datetime
from dateutil.tz import tzutc

import sys
if sys.version_info[0] >= 3:
    unicode = str

class OneLogin_API_Model_OTP_Device_Test(unittest.TestCase):

    enroll_factor_v1_payload = {"active": False, "default": True, "state_token": "f2402de2b446abd86ea5aa1f79b3fa72b4befacd", "auth_factor_name": "OneLogin SMS", "phone_number": "+1xxxxxxxxxx", "type_display_name": "OneLogin SMS", "needs_trigger": True, "user_display_name": "Rich's Phone", "id": 525509}

    enroll_factor_v2_payload = {"id": "36c6cf4c-a315-46ce-81f9-a91a475488cf", "status": "pending", "auth_factor_name": "OneLogin", "type_display_name": "OneLogin Protect", "user_display_name": "OneLogin Protect", "factor_data": {"verification_token": "01-1912451", "totp_url": "otpauth://totp/bsimons:brandon.simons%2Badmin%40onelogin.com?secret=01-1912451"}}

    enroll_factor_v2_payload2 = {"id": "500b41d2-4c6d-4fb3-928b-44d8c0afa19b", "status": "pending", "auth_factor_name": "OneLogin Voice", "type_display_name": "OneLogin Voice", "user_display_name": "OneLogin Voice", "expires_at": "2020-07-21T18:11:54Z", "factor_data": {"verification_token": "144613"}}

    enrolled_factors_v1_payload = {"type_display_name": "OneLogin Protect", "active": True, "user_display_name": "OneLogin Protect", "default": False, "auth_factor_name": "OneLogin Protect", "id": 526532, "needs_trigger": False}

    enrolled_factors_v2_payload = {"device_id": "3920373", "user_display_name": "OneLogin Voice", "type_display_name": "OneLogin Voice", "auth_factor_name": "OneLogin Voice", "default": False}

    def getTestEnrollFactorV1(self):
        test_otp_device = OTP_Device({})
        test_otp_device.active = False
        test_otp_device.auth_factor_name = "OneLogin SMS"
        test_otp_device.default = True
        test_otp_device.id = "525509"
        test_otp_device.needs_trigger = True
        test_otp_device.phone_number = "+1xxxxxxxxxx"
        test_otp_device.state_token = "f2402de2b446abd86ea5aa1f79b3fa72b4befacd"
        test_otp_device.type_display_name = "OneLogin SMS"
        test_otp_device.user_display_name = "Rich's Phone"
        return test_otp_device

    def getTestEnrollFactorV2(self):
        test_otp_device = OTP_Device({})
        test_otp_device.auth_factor_name = "OneLogin"
        test_otp_device.default = False
        test_otp_device.factor_data = {'verification_token': '01-1912451', 'totp_url': 'otpauth://totp/bsimons:brandon.simons%2Badmin%40onelogin.com?secret=01-1912451'}
        test_otp_device.id = "36c6cf4c-a315-46ce-81f9-a91a475488cf"
        test_otp_device.status = "pending"
        test_otp_device.type_display_name = "OneLogin Protect"
        test_otp_device.user_display_name = "OneLogin Protect"
        return test_otp_device

    def getTestEnrollFactorV2_2(self):
        test_otp_device = OTP_Device({})
        test_otp_device.auth_factor_name = "OneLogin Voice"
        test_otp_device.default = False
        test_otp_device.expires_at = datetime.datetime(2020, 7, 21, 18, 11, 54, tzinfo=tzutc())
        test_otp_device.factor_data = {'verification_token': '144613'}
        test_otp_device.id = "500b41d2-4c6d-4fb3-928b-44d8c0afa19b"
        test_otp_device.status = "pending"
        test_otp_device.type_display_name = "OneLogin Voice"
        test_otp_device.user_display_name = "OneLogin Voice"
        return test_otp_device

    def getTestEnrolledFactorsV1(self):
        test_otp_device = OTP_Device({})
        test_otp_device.active = True
        test_otp_device.auth_factor_name = "OneLogin Protect"
        test_otp_device.default = False
        test_otp_device.id = "526532"
        test_otp_device.needs_trigger = False
        test_otp_device.type_display_name = "OneLogin Protect"
        test_otp_device.user_display_name = "OneLogin Protect"

        return test_otp_device

    def getTestEnrolledFactorsV2(self):
        test_otp_device = OTP_Device({})
        test_otp_device.auth_factor_name = "OneLogin Voice"
        test_otp_device.default = False
        test_otp_device.id = "3920373"
        test_otp_device.type_display_name = "OneLogin Voice"
        test_otp_device.user_display_name = "OneLogin Voice"
        return test_otp_device

    def testOTP_Device(self):
        """
        Tests the constructor method of the OTP_Device class
        Build a OTP_Device object and check if all the expected attributes exist
        as described in the OTP_Device Resource of the OneLogin API
        """
        otp_device = OTP_Device(data={})
        expected_attributes = ['id', 'auth_factor_name', 'type_display_name', 'user_display_name', 'default']
        for attr in expected_attributes:
            self.assertTrue(hasattr(otp_device, attr), "OTP_Device has no attribute '{}'".format(attr))

    def testEnrollFactorV1Payload(self):
        otp_device = OTP_Device(self.enroll_factor_v1_payload);
        expected_otp_device = self.getTestEnrollFactorV1()
        self.assertEqual(otp_device.__dict__, expected_otp_device.__dict__)

    def testEnrollFactorV2Payload(self):
        otp_device = OTP_Device(self.enroll_factor_v2_payload);
        self.assertEqual(unicode(otp_device), unicode(self.getTestEnrollFactorV2()))

    def testEnrollFactorV2_2Payload(self):
        otp_device = OTP_Device(self.enroll_factor_v2_payload2);
        self.assertEqual(unicode(otp_device), unicode(self.getTestEnrollFactorV2_2()))

    def testEnrolledFactorsV1Payload(self):
        otp_device = OTP_Device(self.enrolled_factors_v1_payload);
        self.assertEqual(unicode(otp_device), unicode(self.getTestEnrolledFactorsV1()))

    def testEnrolledFactorsV2Payload(self):
        otp_device = OTP_Device(self.enrolled_factors_v2_payload);
        self.assertEqual(unicode(otp_device), unicode(self.getTestEnrolledFactorsV2()))
