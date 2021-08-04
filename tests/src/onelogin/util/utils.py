# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.

import unittest
import datetime
from dateutil.tz import tzutc

from onelogin.api.util.utils import str2bool, str2date, str2int


class OneLogin_API_Client_Util_Utils(unittest.TestCase):


    def testStr2Bool(self):
        self.assertIsNone(str2bool(None))

        self.assertTrue(str2bool(True))
        self.assertFalse(str2bool(False))
        self.assertTrue(str2bool("yes"))
        self.assertTrue(str2bool("true"))
        self.assertTrue(str2bool("t"))
        self.assertTrue(str2bool("1"))
        self.assertTrue(str2bool("YES"))
        self.assertTrue(str2bool("Yes"))
        self.assertTrue(str2bool("TRUE"))
        self.assertTrue(str2bool("True"))
        self.assertTrue(str2bool(1))

        self.assertFalse(str2bool("no"))
        self.assertFalse(str2bool("false"))
        self.assertFalse(str2bool("f"))
        self.assertFalse(str2bool("0"))
        self.assertFalse(str2bool(0))
        self.assertFalse(str2bool("a"))
        self.assertFalse(str2bool([0]))
        
    def testStr2Date(self):
        self.assertIsNone(str2date(None))

        self.assertEqual(str2date("2009-05-05T00:00:00.000Z"), datetime.datetime(2009, 5, 5, 0, 0, tzinfo=tzutc()))
        self.assertEqual(str2date("2015-08-21T23:12:08.495Z"), datetime.datetime(2015, 8, 21, 23, 12, 8, 495000, tzinfo=tzutc()))

    def testStr2Int(self):
        self.assertIsNone(str2int(None))

        self.assertEqual(str2int("1"), 1)
        self.assertTrue(isinstance(str2int("1"), int))

        self.assertEqual(str2int("0"), 0)
        self.assertTrue(isinstance(str2int("0"), int))
