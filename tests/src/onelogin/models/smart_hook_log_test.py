# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.smart_hook_log import SmartHookLog
import unittest

import datetime
from dateutil.tz import tzutc


class OneLogin_API_Model_SmartHookLog_Test(unittest.TestCase):

    get_hook_logs_v2_payload = {"request_id": "54dfe2d2-5124-47f6-9343-ebd33e65eb14", "correlation_id": "a915055b-2a07-4440-83c5-3f8bcad80d8f", "created_at": "2020-10-19T20:03:07.610Z", "events": ["2020-10-19T20:03:07.579Z\t8b2319a4-0d2f-44f8-917f-51afe1d36086\tINFO\t{", "  user: {", "    user_identifier: 'sam@onelogin.com',", "    policy_id: 129314", "  },", "  device: {",  "    user_agent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',", "    is_mobile: false", "  },", "  location: { ip: '114.23.220.238', country_code: 'NZ' },", "  correlation_id: 'a915055b-2a07-4440-83c5-3f8bcad80d8f',", "  request_id: '54dfe2d2-5124-47f6-9343-ebd33e65eb14'", "}", ""]}

    def getTestGetHookLogsV2(self):
        test_smart_hook_log = SmartHookLog({})
        test_smart_hook_log.request_id = "54dfe2d2-5124-47f6-9343-ebd33e65eb14"
        test_smart_hook_log.correlation_id = "a915055b-2a07-4440-83c5-3f8bcad80d8f"
        test_smart_hook_log.created_at = datetime.datetime(2020, 10, 19, 20, 3, 7, 610000, tzinfo=tzutc())
        test_smart_hook_log.events = ["2020-10-19T20:03:07.579Z\t8b2319a4-0d2f-44f8-917f-51afe1d36086\tINFO\t{", "  user: {", "    user_identifier: 'sam@onelogin.com',", "    policy_id: 129314", "  },", "  device: {",  "    user_agent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',", "    is_mobile: false", "  },", "  location: { ip: '114.23.220.238', country_code: 'NZ' },", "  correlation_id: 'a915055b-2a07-4440-83c5-3f8bcad80d8f',", "  request_id: '54dfe2d2-5124-47f6-9343-ebd33e65eb14'", "}", ""]
        return test_smart_hook_log

    def testSmartHookLog(self):
        """
        Tests the constructor method of the SmartHookLog class
        Build a SmartHookLog object and check if all the expected attributes exist
        as described in the SmartHookLog Resource of the OneLogin API
        """
        smart_hook_log = SmartHookLog({})
        expected_attributes = ['request_id', 'correlation_id', 'created_at', 'events']
        for attr in expected_attributes:
            self.assertTrue(hasattr(smart_hook_log, attr), "SmartHookLog has no attribute '{}'".format(attr))

    def testGetHookLogsV2Payload(self):
        smart_hook_log = SmartHookLog(self.get_hook_logs_v2_payload)
        expected_smart_hook_log = self.getTestGetHookLogsV2()
        self.assertEqual(smart_hook_log.__dict__, expected_smart_hook_log.__dict__)
