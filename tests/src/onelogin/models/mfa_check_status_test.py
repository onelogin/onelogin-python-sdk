# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.mfa_check_status import MFACheckStatus
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str

class OneLogin_API_Model_MFACheckStatus_Test(unittest.TestCase):

    verify_enroll_factor_otp_v2_payload = {"id": "406fefd4-8a36-4aee-880c-f3e4a928e27d", "status": "accepted", "device_id": "3919988"}

    verify_enroll_factor_poll_v2_payload = {"id": "406fefd4-8a36-4aee-880c-f3e4a928e22d", "status": "pending", "device_id": "3919922"}

    def getTestVerifyEnrollFactorOTP_V2(self):
        test_mfa_check_status = MFACheckStatus({})
        test_mfa_check_status.id = "406fefd4-8a36-4aee-880c-f3e4a928e27d"
        test_mfa_check_status.status = "accepted"
        test_mfa_check_status.device_id = "3919988"
        return test_mfa_check_status

    def getTestVerifyEnrollFactorPull_V2(self):
        test_mfa_check_status = MFACheckStatus({})
        test_mfa_check_status.id = "406fefd4-8a36-4aee-880c-f3e4a928e22d"
        test_mfa_check_status.status = "pending"
        test_mfa_check_status.device_id = "3919922"
        return test_mfa_check_status

    def testMFACheckStatus(self):
        """
        Tests the constructor method of the MFACheckStatus class
        Build a MFACheckStatus object and check if all the expected attributes exist
        as described in the MFACheckStatus Resource of the OneLogin API
        """
        mfa_check_status = MFACheckStatus(data={})
        expected_attributes = ['id', 'status', 'device_id']
        for attr in expected_attributes:
            self.assertTrue(hasattr(mfa_check_status, attr), "MFACheckStatus has no attribute '{}'".format(attr))

    def testVerifyEnrollFactorOTPV2Payload(self):
        mfa_check_status = MFACheckStatus(self.verify_enroll_factor_otp_v2_payload);
        self.assertEqual(unicode(mfa_check_status), unicode(self.getTestVerifyEnrollFactorOTP_V2()))

    def testVerifyEnrollFactorPullV2Payload(self):
        mfa_check_status = MFACheckStatus(self.verify_enroll_factor_poll_v2_payload);
        self.assertEqual(unicode(mfa_check_status), unicode(self.getTestVerifyEnrollFactorPull_V2()))
