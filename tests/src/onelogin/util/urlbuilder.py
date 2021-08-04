# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.

import unittest
import datetime
from dateutil.tz import tzutc

from onelogin.api.util.urlbuilder import UrlBuilder
from onelogin.api.util.constants import Constants

import sys
if sys.version_info[0] >= 3:
    long = int


class OneLogin_API_Client_Util_UrlBuilder(unittest.TestCase):

    def testUrlBuilder(self):
        urlbuilder = UrlBuilder()
        self.assertEqual(urlbuilder.region, "us")
        self.assertIsNone(urlbuilder.subdomain)
        
        urlbuilder = UrlBuilder("us")
        self.assertEqual(urlbuilder.region, "us")
        self.assertIsNone(urlbuilder.subdomain)

        urlbuilder = UrlBuilder("eu")
        self.assertEqual(urlbuilder.region, "eu")
        self.assertIsNone(urlbuilder.subdomain)

        urlbuilder = UrlBuilder(None, "testsubdomain")
        self.assertEqual(urlbuilder.region, "us")
        self.assertEqual(urlbuilder.subdomain, "testsubdomain")

    def testGetUrlWithRegion(self):
        urlbuilder = UrlBuilder()

        self.assertEqual(urlbuilder.get_url(Constants.GET_RATE_URL), 'https://api.us.onelogin.com/auth/rate_limit')

        self.assertEqual(urlbuilder.get_url(Constants.GET_USERS_URL, None, None, 1), 'https://api.us.onelogin.com/api/1/users')
        self.assertEqual(urlbuilder.get_url(Constants.GET_USERS_URL, None, None, 2), 'https://api.us.onelogin.com/api/2/users')

        self.assertEqual(urlbuilder.get_url(Constants.GET_USER_URL, 101, None, 1), 'https://api.us.onelogin.com/api/1/users/101')
        self.assertEqual(urlbuilder.get_url(Constants.GET_USER_URL, 102, None, 2), 'https://api.us.onelogin.com/api/2/users/102')

        self.assertEqual(urlbuilder.get_url(Constants.GET_APP_RULE_URL, 101, 1001, 1), 'https://api.us.onelogin.com/api/1/apps/101/rules/1001')
        self.assertEqual(urlbuilder.get_url(Constants.GET_APP_RULE_URL, 102, 1002, 2), 'https://api.us.onelogin.com/api/2/apps/102/rules/1002')

    def testGetUrlWithSubdomain(self):
        urlbuilder = UrlBuilder("us", "testsubdomain")

        self.assertEqual(urlbuilder.get_url(Constants.GET_RATE_URL), 'https://testsubdomain.onelogin.com/auth/rate_limit')

        self.assertEqual(urlbuilder.get_url(Constants.GET_USERS_URL, None, None, 1), 'https://testsubdomain.onelogin.com/api/1/users')
        self.assertEqual(urlbuilder.get_url(Constants.GET_USERS_URL, None, None, 2), 'https://testsubdomain.onelogin.com/api/2/users')

        self.assertEqual(urlbuilder.get_url(Constants.GET_USER_URL, 101, None, 1), 'https://testsubdomain.onelogin.com/api/1/users/101')
        self.assertEqual(urlbuilder.get_url(Constants.GET_USER_URL, 102, None, 2), 'https://testsubdomain.onelogin.com/api/2/users/102')

        self.assertEqual(urlbuilder.get_url(Constants.GET_APP_RULE_URL, 101, 1001, 1), 'https://testsubdomain.onelogin.com/api/1/apps/101/rules/1001')
        self.assertEqual(urlbuilder.get_url(Constants.GET_APP_RULE_URL, 102, 1002, 2), 'https://testsubdomain.onelogin.com/api/2/apps/102/rules/1002')

    def testGetVersionId(self):
        urlbuilder = UrlBuilder()

        api_configuration = {}
        self.assertIsNone(urlbuilder.get_version_id(api_configuration, "GET_RATE_URL"))
        self.assertEquals(urlbuilder.get_version_id(api_configuration, "GET_USERS_URL"), 2)
        self.assertEquals(urlbuilder.get_version_id(api_configuration, "GET_EVENTS_URL"), 1)

        api_configuration = {"user": 1, "event": 1}
        self.assertIsNone(urlbuilder.get_version_id(api_configuration, "GET_RATE_URL"))
        self.assertEquals(urlbuilder.get_version_id(api_configuration, "GET_USERS_URL"), 1)
        self.assertEquals(urlbuilder.get_version_id(api_configuration, "GET_EVENTS_URL"), 1)

        api_configuration = {"user": 2, "event": 2}
        self.assertIsNone(urlbuilder.get_version_id(api_configuration, "GET_RATE_URL"))
        self.assertEquals(urlbuilder.get_version_id(api_configuration, "GET_USERS_URL"), 2)
        self.assertEquals(urlbuilder.get_version_id(api_configuration, "GET_EVENTS_URL"), 1)

    def testvalidateId(self):
        urlbuilder = UrlBuilder()

        with self.assertRaises(Exception):
            urlbuilder.validate_id(["1"])

        with self.assertRaises(Exception):
            urlbuilder.validate_id({"a": 1})

        with self.assertRaises(Exception):
            urlbuilder.validate_id(None)

        self.assertTrue(urlbuilder.validate_id("1"))
        self.assertTrue(urlbuilder.validate_id(u'1'))
        self.assertTrue(urlbuilder.validate_id(str(1)))
        self.assertTrue(urlbuilder.validate_id(int("1")))
        self.assertTrue(urlbuilder.validate_id(long("1")))
