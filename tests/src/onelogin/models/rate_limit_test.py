# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.rate_limit import RateLimit
import unittest
import datetime
from dateutil.tz import tzutc

class OneLogin_API_Model_RateLimit_Test(unittest.TestCase):

    rate_limit_v1_payload = {"X-RateLimit-Limit": 5000, "X-RateLimit-Remaining": 4988, "X-RateLimit-Reset": 832}

    def getTestRateLimitV1(self):
        test_rate_limit = RateLimit({})
        test_rate_limit.limit = 5000
        test_rate_limit.remaining = 4988
        test_rate_limit.reset = 832
        return test_rate_limit

    def testRateLimit(self):
        """
        Tests the constructor method of the RateLimit class
        Build a RateLimit object and check if all the expected attributes exist
        as described in the RateLimit Resource of the OneLogin API
        """
        rate_limit = RateLimit({})
        expected_attributes = ['limit', 'remaining', 'reset']
        for attr in expected_attributes:
            self.assertTrue(hasattr(rate_limit, attr), "RateLimit has no attribute '{}'".format(attr))

    def testRateLimitV1Payload(self):
        rate_limit = RateLimit(self.rate_limit_v1_payload);
        expected_rate_limit = self.getTestRateLimitV1()
        self.assertEqual(rate_limit.__dict__, expected_rate_limit.__dict__)
