# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.onelogin_token import OneLoginToken
import unittest
import datetime
from dateutil.tz import tzutc

import sys
if sys.version_info[0] >= 3:
    unicode = str

class OneLogin_API_Model_OneLoginToken_Test(unittest.TestCase):

    access_token_payload = {"access_token": "xx508xx63817x752xx74004x30705xx92x58349x5x78f5xx34xxxxx51", "created_at": "2015-11-11T03:36:18.714Z", "expires_in": 36000, "refresh_token": "628x9x0xx447xx4x421x517x4x474x33x2065x4x1xx523xxxxx6x7x20", "token_type": "bearer", "account_id": 555555}

    refresh_token_payload = {"access_token": "xxx", "created_at": "2015-11-11T22:46:15.961Z", "expires_in": 36000, "refresh_token": "yyy", "token_type": "bearer"}

    def getTestAccessToken(self):
        test_onelogin_token = OneLoginToken({})
        test_onelogin_token.access_token = "xx508xx63817x752xx74004x30705xx92x58349x5x78f5xx34xxxxx51"
        test_onelogin_token.account_id = 555555
        test_onelogin_token.created_at = datetime.datetime(2015, 11, 11, 3, 36, 18, 714000, tzinfo=tzutc())
        test_onelogin_token.expires_in = 36000
        test_onelogin_token.refresh_token = "628x9x0xx447xx4x421x517x4x474x33x2065x4x1xx523xxxxx6x7x20"
        test_onelogin_token.token_type = "bearer"
        return test_onelogin_token

    def getTestRefreshToken(self):
        test_onelogin_token = OneLoginToken({})
        test_onelogin_token.access_token = "xxx"
        test_onelogin_token.account_id = None
        test_onelogin_token.created_at = datetime.datetime(2015, 11, 11, 22, 46, 15, 961000, tzinfo=tzutc())
        test_onelogin_token.expires_in = 36000
        test_onelogin_token.refresh_token = "yyy"
        test_onelogin_token.token_type = "bearer"
        return test_onelogin_token

    def testOneLoginToken(self):
        """
        Tests the constructor method of the OneLoginToken class
        Build a OneLoginToken object and check if all the expected attributes exist
        as described in the OneLoginToken Resource of the OneLogin API
        """
        onelogin_token = OneLoginToken(data={})
        expected_attributes = ['access_token', 'refresh_token', 'account_id', 'token_type', 'created_at', 'expires_in']
        for attr in expected_attributes:
            self.assertTrue(hasattr(onelogin_token, attr), "OneLoginToken has no attribute '{}'".format(attr))

    def testOneLoginAccessTokenPayload(self):
        onelogin_token = OneLoginToken(self.access_token_payload);
        self.assertEqual(unicode(onelogin_token), unicode(self.getTestAccessToken()))

    def testOneLoginRefreshTokenPayload(self):
        onelogin_token = OneLoginToken(self.refresh_token_payload);
        self.assertEqual(unicode(onelogin_token), unicode(self.getTestRefreshToken()))
