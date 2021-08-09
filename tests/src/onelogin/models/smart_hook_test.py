# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.smart_hook import SmartHook
import unittest

import datetime
from dateutil.tz import tzutc


class OneLogin_API_Model_SmartHook_Test(unittest.TestCase):

    get_hooks_v2_payload = {"id": "d360aded-6063-4c60-8add-45f32772ff71", "type": "pre-authentication", "packages": {"ua-parser-js": "0.7.21"}, "runtime": "nodejs12.x",  "context_version": ">= 1.0.0",  "retries": 0,  "timeout": 1, "disabled": False, "status": "ready", "env_vars": ["MY_API_KEY"], "options": {"location_enabled": False, "risk_enabled": False, "mfa_device_info_enabled": False}, "created_at": "2020-10-14T01:54:59.976Z",
 "updated_at": "2020-10-16T17:28:45.970Z"}

    get_hook_v2_payload = {"id": "d360aded-6063-4c60-8add-45f32772ff71", "type": "pre-authentication", "packages": {"ua-parser-js": "0.7.21"}, "runtime": "nodejs12.x",  "context_version": ">= 1.0.0",  "retries": 0,  "timeout": 1, "disabled": False, "status": "ready", "env_vars": ["MY_API_KEY"], "options": {"location_enabled": False, "risk_enabled": False, "mfa_device_info_enabled": False}, "created_at": "2020-10-14T01:54:59.976Z",
 "updated_at": "2020-10-16T17:28:45.970Z", "conditions": [{"source": "roles", "operator": "~", "value": "123456" }]}

    def getTestGetHooksV2(self):
        test_smart_hook = SmartHook({})
        test_smart_hook.conditions = None
        test_smart_hook.context_version = ">= 1.0.0"
        test_smart_hook.created_at = datetime.datetime(2020, 10, 14, 1, 54, 59, 976000, tzinfo=tzutc())
        test_smart_hook.updated_at = datetime.datetime(2020, 10, 16, 17, 28, 45, 970000, tzinfo=tzutc())
        test_smart_hook.disabled = False
        test_smart_hook.env_vars = ['MY_API_KEY']
        test_smart_hook.function = None
        test_smart_hook.id = "d360aded-6063-4c60-8add-45f32772ff71"
        test_smart_hook.location_enabled = False
        test_smart_hook.mfa_device_info_enabled = False
        test_smart_hook.packages = {'ua-parser-js': '0.7.21'}
        test_smart_hook.retries = 0
        test_smart_hook.risk_enabled = False
        test_smart_hook.runtime = "nodejs12.x"
        test_smart_hook.status = "ready"
        test_smart_hook.timeout = 1
        test_smart_hook.type = "pre-authentication"
        return test_smart_hook

    def getTestGetHookV2(self):
        test_smart_hook = SmartHook({})
        test_smart_hook.conditions = [{"source": "roles", "operator": "~", "value": "123456" }]
        test_smart_hook.context_version = ">= 1.0.0"
        test_smart_hook.created_at = datetime.datetime(2020, 10, 14, 1, 54, 59, 976000, tzinfo=tzutc())
        test_smart_hook.updated_at = datetime.datetime(2020, 10, 16, 17, 28, 45, 970000, tzinfo=tzutc())
        test_smart_hook.disabled = False
        test_smart_hook.env_vars = ['MY_API_KEY']
        test_smart_hook.function = None
        test_smart_hook.id = "d360aded-6063-4c60-8add-45f32772ff71"
        test_smart_hook.location_enabled = False
        test_smart_hook.mfa_device_info_enabled = False
        test_smart_hook.packages = {'ua-parser-js': '0.7.21'}
        test_smart_hook.retries = 0
        test_smart_hook.risk_enabled = False
        test_smart_hook.runtime = "nodejs12.x"
        test_smart_hook.status = "ready"
        test_smart_hook.timeout = 1
        test_smart_hook.type = "pre-authentication"
        return test_smart_hook

    def testSmartHook(self):
        """
        Tests the constructor method of the SmartHook class
        Build a SmartHook object and check if all the expected attributes exist
        as described in the SmartHook Resource of the OneLogin API
        """
        smart_hook = SmartHook({})
        expected_attributes = ['id', 'type', 'packages', 'runtime', 'context_version', 'retries', 'timeout', 'disabled', 'status', 'env_vars',
                               'created_at', 'updated_at', 'function', 'conditions']
        for attr in expected_attributes:
            self.assertTrue(hasattr(smart_hook, attr), "SmartHook has no attribute '{}'".format(attr))

    def testGetHooksV2Payload(self):
        smart_hook = SmartHook(self.get_hooks_v2_payload);
        expected_smart_hook = self.getTestGetHooksV2()
        self.assertEqual(smart_hook.__dict__, expected_smart_hook.__dict__)

    def testGetHookV2Payload(self):
        smart_hook = SmartHook(self.get_hook_v2_payload);
        expected_smart_hook = self.getTestGetHookV2()
        self.assertEqual(smart_hook.__dict__, expected_smart_hook.__dict__)
