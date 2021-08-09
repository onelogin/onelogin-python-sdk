# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.session_token_mfa_info import SessionTokenMFAInfo
from onelogin.api.models.device import Device
from onelogin.api.models.user import User
import unittest


class OneLogin_API_Model_SessionTokenMFAInfo_Test(unittest.TestCase):

    create_session_login_v1_payload = {"user": {"email": "jennifer.hasenfus@onelogin.com", "username": "jhasenfus", "firstname": "Jennifer", "lastname": "Hasenfus", "id": 88888888}, "state_token": "xf4330878444597bd3933d4247cc1xxxxxxxxxxx", "callback_url": "https://api.us.onelogin.com/api/1/login/verify_factor", "devices": [{"device_type": "OneLogin OTP SMS", "device_id": 111111}, {"device_type": "Google Authenticator", "device_id": 444444}]}

    def getTestCreateSessionLoginV1(self):
        test_session_token_mfa_info = SessionTokenMFAInfo({})
        test_session_token_mfa_info.callback_url = "https://api.us.onelogin.com/api/1/login/verify_factor"
        test_session_token_mfa_info.state_token = "xf4330878444597bd3933d4247cc1xxxxxxxxxxx"
        test_session_token_mfa_info.devices.append(Device({'device_id': 111111, 'device_type': 'OneLogin OTP SMS'}))
        test_session_token_mfa_info.devices.append(Device({'device_id': 444444, 'device_type': 'Google Authenticator'}))
        test_session_token_mfa_info.user = User({'id': 88888888, 'username': 'jhasenfus', 'lastname': 'Hasenfus', 'firstname': 'Jennifer', 'email': 'jennifer.hasenfus@onelogin.com'})
        return test_session_token_mfa_info

    def testSessionTokenMFAInfo(self):
        """
        Tests the constructor method of the SessionTokenMFAInfo class
        Build a SessionTokenMFAInfo object and check if all the expected attributes exist
        as described in the SessionTokenMFAInfo Resource of the OneLogin API
        """
        session_token_mfa_info = SessionTokenMFAInfo({})
        expected_attributes = ['state_token', 'callback_url', 'devices']
        for attr in expected_attributes:
            self.assertTrue(hasattr(session_token_mfa_info, attr), "SessionTokenMFAInfo has no attribute '{}'".format(attr))

    def testCreateSessionLoginV1Payload(self):
        session_token_mfa_info = SessionTokenMFAInfo(self.create_session_login_v1_payload);
        expected_session_token_mfa_info = self.getTestCreateSessionLoginV1()
        self.assertEqual(len(session_token_mfa_info.devices), len(expected_session_token_mfa_info.devices))
        for i in range(len(session_token_mfa_info.devices)):
            self.assertEqual(session_token_mfa_info.devices[i].__dict__, expected_session_token_mfa_info.devices[i].__dict__)
        session_token_mfa_info.devices = expected_session_token_mfa_info.devices = []
        self.assertEqual(session_token_mfa_info.user.__dict__, expected_session_token_mfa_info.user.__dict__)
        session_token_mfa_info.user = expected_session_token_mfa_info.user = {}
        self.assertEqual(session_token_mfa_info.__dict__, expected_session_token_mfa_info.__dict__)
