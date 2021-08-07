# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.device import Device
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str


class OneLogin_API_Model_Device_Test(unittest.TestCase):

    def testDevice(self):
        """
        Tests the constructor method of the Device class
        Build a Device object and check if all the expected attributes exist
        as described in the Device Resource of the OneLogin API
        """
        device = Device(data={})
        expected_attributes = ['id', 'type', "duo_api_hostname", "duo_sig_request"]

        for attr in expected_attributes:
            self.assertTrue(hasattr(device, attr), "Device has no attribute '{}'".format(attr))
