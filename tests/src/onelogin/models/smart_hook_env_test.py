# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.smart_hook_env import SmartHookEnv
import unittest

import datetime
from dateutil.tz import tzutc


class OneLogin_API_Model_SmartHookEnv_Test(unittest.TestCase):

    get_hook_envs_v2_payload = {"id": "8148095e-1b63-4acc-b2de-ff3fc5f12561", "name": "MY_API_KEY", "created_at": "2020-08-28T01:10:14.043Z", "updated_at": "2020-08-28T01:10:14.043Z"}

    get_hook_env_v2_payload = {"id": "8148095e-1b63-4acc-b2de-ff3fc5f12562", "name": "MY_API_KEY2", "created_at": "2020-08-28T01:10:16.041Z", "updated_at": "2020-08-28T01:10:16.041Z"}

    def getTestGetHookEnvsV2(self):
        test_smart_hook_env = SmartHookEnv({})
        test_smart_hook_env.id = "8148095e-1b63-4acc-b2de-ff3fc5f12561"
        test_smart_hook_env.name = "MY_API_KEY"
        test_smart_hook_env.created_at = datetime.datetime(2020, 8, 28, 1, 10, 14, 43000, tzinfo=tzutc())
        test_smart_hook_env.updated_at = datetime.datetime(2020, 8, 28, 1, 10, 14, 43000, tzinfo=tzutc())
        return test_smart_hook_env

    def getTestGetHookEnvV2(self):
        test_smart_hook_env = SmartHookEnv({})
        test_smart_hook_env.id = "8148095e-1b63-4acc-b2de-ff3fc5f12562"
        test_smart_hook_env.name = "MY_API_KEY2"
        test_smart_hook_env.created_at = datetime.datetime(2020, 8, 28, 1, 10, 16, 41000, tzinfo=tzutc())
        test_smart_hook_env.updated_at = datetime.datetime(2020, 8, 28, 1, 10, 16, 41000, tzinfo=tzutc())
        return test_smart_hook_env

    def testSmartHookEnv(self):
        """
        Tests the constructor method of the SmartHookEnv class
        Build a SmartHookEnv object and check if all the expected attributes exist
        as described in the SmartHookEnv Resource of the OneLogin API
        """
        smart_hook_env = SmartHookEnv({})
        expected_attributes = ['id', 'name', 'created_at', 'updated_at']
        for attr in expected_attributes:
            self.assertTrue(hasattr(smart_hook_env, attr), "SmartHookEnv has no attribute '{}'".format(attr))

    def testGetHookEnvsV2Payload(self):
        smart_hook_env = SmartHookEnv(self.get_hook_envs_v2_payload)
        expected_smart_hook_env = self.getTestGetHookEnvsV2()
        self.assertEqual(smart_hook_env.__dict__, expected_smart_hook_env.__dict__)

    def testGetHookV2Payload(self):
        smart_hook_env = SmartHookEnv(self.get_hook_env_v2_payload)
        expected_smart_hook_env = self.getTestGetHookEnvV2()
        self.assertEqual(smart_hook_env.__dict__, expected_smart_hook_env.__dict__)
