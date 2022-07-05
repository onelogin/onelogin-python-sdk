# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.session_token_info import SessionTokenInfo
from onelogin.api.models.user import User
import unittest

import datetime
from dateutil.tz import tzutc


class OneLogin_API_Model_SessionTokenInfo_Test(unittest.TestCase):

    create_session_login_v1_payload = {"status": "Authenticated", "user": {"username": "kinua", "email": "kinua.wong@company.com", "firstname": "Kinua", "id": 88888888, "lastname": "Wong"}, "return_to_url": None, "expires_at": "2016/01/07 05:56:21 +0000", "session_token": "9x8869x31134x7906x6x54474x21x18xxx90857x"}

    get_session_token_verified_v1_payload = {"return_to_url": None, "user": {"username": "jhasenfus", "email": "jennifer.hasenfus@onelogin.com", "firstname": "Jennifer", "lastname": "Hasegawa", "id": 88888889}, "status": "Authenticated", "session_token": "xxxxxxxxx8a4c07773a5454f946", "expires_at": "2016/01/26 02:21:47 +0000"}

    def getTestCreateSessionLoginV1(self):
        test_session_token_info = SessionTokenInfo({})
        test_session_token_info.expires_at = datetime.datetime(2016, 1, 7, 5, 56, 21, tzinfo=tzutc())
        test_session_token_info.return_to_url = None
        test_session_token_info.session_token = "9x8869x31134x7906x6x54474x21x18xxx90857x"
        test_session_token_info.status = "Authenticated"
        test_session_token_info.user = User({'status': None, 'username': 'kinua', 'id': 88888888, 'firstname': 'Kinua', 'custom_attributes': {}, 'lastname': 'Wong', 'email': 'kinua.wong@company.com',  'role_ids': []})
        return test_session_token_info

    def getTestGetSessionTokenVerifiedInfoV1(self):
        test_session_token_info = SessionTokenInfo({})
        test_session_token_info.expires_at = datetime.datetime(2016, 1, 26, 2, 21, 47, tzinfo=tzutc())
        test_session_token_info.return_to_url = None
        test_session_token_info.session_token = "xxxxxxxxx8a4c07773a5454f946"
        test_session_token_info.status = "Authenticated"
        test_session_token_info.user = User({'email': 'jennifer.hasenfus@onelogin.com', 'username': 'jhasenfus', 'firstname': 'Jennifer', 'lastname': 'Hasegawa', 'id': 88888889})
        return test_session_token_info

    def testSessionTokenInfo(self):
        """
        Tests the constructor method of the SessionTokenInfo class
        Build a SessionTokenInfo object and check if all the expected attributes exist
        as described in the SessionTokenInfo Resource of the OneLogin API
        """
        session_token_info = SessionTokenInfo({})
        expected_attributes = ['status', 'return_to_url', 'expires_at', 'session_token']
        for attr in expected_attributes:
            self.assertTrue(hasattr(session_token_info, attr), "SessionTokenInfo has no attribute '{}'".format(attr))

    def testCreateSessionLoginV1Payload(self):
        session_token_info = SessionTokenInfo(self.create_session_login_v1_payload)
        expected_session_token_info = self.getTestCreateSessionLoginV1()
        self.assertEqual(session_token_info.user.__dict__, expected_session_token_info.user.__dict__)
        session_token_info.user = expected_session_token_info.user = {}
        self.assertEqual(session_token_info.__dict__, expected_session_token_info.__dict__)

    def testGetSessionTokenVerifiedV1Payload(self):
        session_token_info = SessionTokenInfo(self.get_session_token_verified_v1_payload)
        expected_session_token_info = self.getTestGetSessionTokenVerifiedInfoV1()
        self.assertEqual(session_token_info.user.__dict__, expected_session_token_info.user.__dict__)
        session_token_info.user = expected_session_token_info.user = {}
        self.assertEqual(session_token_info.__dict__, expected_session_token_info.__dict__)
