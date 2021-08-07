# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.connector import Connector
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str

# noinspection PySetFunctionToLiteral
class OneLogin_API_Model_Connector_Test(unittest.TestCase):

    connector_v2_payload = {"id": 114099, "name": "Amazon Connect", "auth_method": 2, "allows_new_parameters": False, "icon_url": "https://cdn-shadow.onlgn.net/images/icons/square/amazonConnect/old_original.png"}

    def getTestConnectorsV2(self):
        test_connector = Connector({})
        test_connector.id = 114099
        test_connector.name = "Amazon Connect"
        test_connector.auth_method = 2
        test_connector.allows_new_parameters = False
        test_connector.icon_url = "https://cdn-shadow.onlgn.net/images/icons/square/amazonConnect/old_original.png"
        return test_connector

    def testConnector(self):
        """
        Tests the constructor method of the Connector class
        Build a Connector object and check if all the expected attributes exist
        as described in the Connector Resource of the OneLogin API
        """
        connector = Connector(data={})
        expected_attributes = ['id', 'name', "auth_method", "allows_new_parameters", "icon_url"]

        for attr in expected_attributes:
            self.assertTrue(hasattr(connector, attr), "Connector has no attribute '{}'".format(attr))

    def testConnectorV2Payload(self):
        connector = Connector(self.connector_v2_payload);
        self.assertEqual(unicode(connector), unicode(self.getTestConnectorsV2()))
