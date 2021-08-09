# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.auth_factor import AuthFactor
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str

# noinspection PySetFunctionToLiteral
class OneLogin_API_AssignedAdmin_Test(unittest.TestCase):

    auth_factor_v1_payload = {"name": "OneLogin SMS", "factor_id": 16282}

    auth_factor_v2_payload = {"factor_id": 58958, "name": "OneLogin Protect", "auth_factor_name": "OneLogin"}

    def getTestAuthFactorsV1(self):
        test_auth_factor = AuthFactor({})
        test_auth_factor.id = 16282
        test_auth_factor.name = "OneLogin SMS"
        return test_auth_factor

    def getTestAuthFactorsV2(self):
        test_auth_factor = AuthFactor({})
        test_auth_factor.id = 58958
        test_auth_factor.name = "OneLogin Protect"
        test_auth_factor.auth_factor_name = "OneLogin"
        return test_auth_factor

    def testAuthFactor(self):
        """
        Tests the constructor method of the AuthFactor class
        Build a AuthFactor object and check if all the expected attributes exist
        as described in the AuthFactor Resource of the OneLogin API
        """
        auth_factor = AuthFactor(data={})
        expected_attributes = ['id', 'name']

        for attr in expected_attributes:
            self.assertTrue(hasattr(auth_factor, attr), "AuthFactor has no attribute '{}'".format(attr))

    def testAuthFactorsV1Payload(self):
        auth_factor = AuthFactor(self.auth_factor_v1_payload);
        self.assertEqual(unicode(auth_factor), unicode(self.getTestAuthFactorsV1()))

    def testAuthFactorsV2Payload(self):
        auth_factor = AuthFactor(self.auth_factor_v2_payload);
        self.assertEqual(unicode(auth_factor), unicode(self.getTestAuthFactorsV2()))
