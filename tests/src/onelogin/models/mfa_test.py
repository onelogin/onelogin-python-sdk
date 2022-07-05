# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.mfa import MFA
import unittest

class OneLogin_API_Model_MFA_Test(unittest.TestCase):

    def testMFA(self):
        """
        Tests the constructor method of the MFA class
        Build a MFA object and check if all the expected attributes exist
        as described in the MFA Resource of the OneLogin API
        """
        mfa = MFA(data={})
        expected_attributes = ['state_token', 'callback_url', 'user', 'devices']
        for attr in expected_attributes:
            self.assertTrue(hasattr(mfa, attr), "MFA has no attribute '{}'".format(attr))
