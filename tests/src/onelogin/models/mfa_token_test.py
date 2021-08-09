# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.mfa_token import MFAToken
import unittest
import datetime
from dateutil.tz import tzutc

import sys
if sys.version_info[0] >= 3:
    unicode = str

class OneLogin_API_Model_MFAToken_Test(unittest.TestCase):

    mfa_token_v1_payload = {"mfa_token": "55647655", "reusable": True, "expires_at": "2019-01-16T22:16:38Z"}

    mfa_token_v2_payload = {"mfa_token": "25992782", "expires_at": "2021-07-27T23:25:50Z", "reusable": False, "device_id": "user_temp_otp_36216766"}

    def getTestMFATokenV1(self):
        test_mfa_token = MFAToken({})
        test_mfa_token.value = "55647655"
        test_mfa_token.reusable = True
        test_mfa_token.expires_at = datetime.datetime(2019, 1, 16, 22, 16, 38, tzinfo=tzutc())
        return test_mfa_token

    def getTestMFATokenV2(self):
        test_mfa_token = MFAToken({})
        test_mfa_token.value = "25992782"
        test_mfa_token.reusable = False
        test_mfa_token.expires_at = datetime.datetime(2021, 7, 27, 23, 25, 50, tzinfo=tzutc())
        test_mfa_token.device_id = "user_temp_otp_36216766"
        return test_mfa_token

    def testMFAToken(self):
        """
        Tests the constructor method of the MFAToken class
        Build a MFAToken object and check if all the expected attributes exist
        as described in the MFAToken Resource of the OneLogin API
        """
        mfa_token = MFAToken(data={})
        expected_attributes = ['value', 'reusable', 'expires_at']
        for attr in expected_attributes:
            self.assertTrue(hasattr(mfa_token, attr), "MFAToken has no attribute '{}'".format(attr))

    def testMFATokenV1Payload(self):
        mfa_token = MFAToken(self.mfa_token_v1_payload);
        self.assertEqual(unicode(mfa_token), unicode(self.getTestMFATokenV1()))

    def testMFATokenV2Payload(self):
        mfa_token = MFAToken(self.mfa_token_v2_payload);
        self.assertEqual(unicode(mfa_token), unicode(self.getTestMFATokenV2()))
