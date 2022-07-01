# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.risk_score import RiskScore
from onelogin.api.models.smart_mfa import SmartMFA
import unittest

class OneLogin_API_Model_SmartMFA_Test(unittest.TestCase):

    validate_user_v2_payload = {"user_id": 60254824, "risk": {"score": 93, "reasons": ["Chrome on Windows is used infrequently", "Kaohsiung City, Kaohsiung, Taiwan is a new location", "Taiwan is a new location", "Chrome on Windows has not been used before", "Accessed from a new IP address", "Accessed from a new browser session", "Infrequent access from 120.118.218.227", "Infrequent access from Kaohsiung City, Kaohsiung, Taiwan", "Infrequent access from Taiwan", "Infrequent access using Chrome on Windows", "Low trust for session", "Browser Cookie Expected"]}, "mfa": {"otp_sent": True, "state_token": "67ff7e91-ec38-467d-b7df-c0f4f61efd73"}}

    def getTestValidateUserV2(self):
        test_smart_mfa = SmartMFA({})
        test_smart_mfa.user_id = 60254824
        test_smart_mfa.risk = RiskScore({"score": 93, "triggers": ["Chrome on Windows is used infrequently", "Kaohsiung City, Kaohsiung, Taiwan is a new location", "Taiwan is a new location", "Chrome on Windows has not been used before", "Accessed from a new IP address", "Accessed from a new browser session", "Infrequent access from 120.118.218.227", "Infrequent access from Kaohsiung City, Kaohsiung, Taiwan", "Infrequent access from Taiwan", "Infrequent access using Chrome on Windows", "Low trust for session", "Browser Cookie Expected"]})
        test_smart_mfa.mfa = {"otp_sent": True, "state_token": "67ff7e91-ec38-467d-b7df-c0f4f61efd73"}
        return test_smart_mfa

    def testSmartMFA(self):
        """
        Tests the constructor method of the SmartMFA class
        Build a SmartMFA object and check if all the expected attributes exist
        as described in the SmartMFA Resource of the OneLogin API
        """
        smart_mfa = SmartMFA({})
        expected_attributes = ['user_id', 'risk', 'mfa']
        for attr in expected_attributes:
            self.assertTrue(hasattr(smart_mfa, attr), "SmartMFA has no attribute '{}'".format(attr))

    def testValidateUserV2Payload(self):
        smart_mfa = SmartMFA(self.validate_user_v2_payload)
        expected_smart_mfa = self.getTestValidateUserV2()
        self.assertEqual(smart_mfa.risk.__dict__, expected_smart_mfa.risk.__dict__)
        smart_mfa.risk = expected_smart_mfa.risk = None
        self.assertEqual(smart_mfa.mfa, expected_smart_mfa.mfa)
        smart_mfa.mfa = expected_smart_mfa.mfa = None
        self.assertEqual(smart_mfa.__dict__, expected_smart_mfa.__dict__)
