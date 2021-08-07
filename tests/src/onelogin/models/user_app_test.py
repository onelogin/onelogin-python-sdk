# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.user_app import UserApp
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str

# noinspection PySetFunctionToLiteral
class OneLogin_API_UserApp_Test(unittest.TestCase):

    user_apps_v1_payload = {"id": 436448, "name": "AWS DynamoDB Multi Role Production", "icon": "https://image.com/mobile_50.png?1421095823", "provisioned": "unknown", "extension": False, "login_id": 66666666, "personal": False}

    user_apps_v2_payload = {"id": 1127385, "icon_url": "/images/missing_connector_icon/square/mobile_50.png", "extension": False, "login_id": 415930448, "name": "OIDC Basic", "provisioning_status": "enabled", "provisioning_state": "unknown", "provisioning_enabled": False}

    def getTestUserAppV1(self):
        test_user_app = UserApp(data={})
        test_user_app.connector_id = None
        test_user_app.extension = False
        test_user_app.icon_url = "https://image.com/mobile_50.png?1421095823"
        test_user_app.id = 436448
        test_user_app.login_id = 66666666
        test_user_app.name = "AWS DynamoDB Multi Role Production"
        test_user_app.personal = False
        test_user_app.provisioned = False
        return test_user_app

    def getTestUserAppV2(self):
        test_user_app = UserApp(data={})
        test_user_app.connector_id = None
        test_user_app.extension = False
        test_user_app.icon_url = "/images/missing_connector_icon/square/mobile_50.png"
        test_user_app.id = 1127385
        test_user_app.login_id = 415930448
        test_user_app.name = "OIDC Basic"
        test_user_app.provisioning_enabled = False
        test_user_app.provisioning_state = "unknown"
        test_user_app.provisioning_status = "enabled"
        return test_user_app

    def testUserAppAttributes(self):
        """
        Tests the constructor method of the UserApp class
        Build a UserApp object and check if all the expected attributes exist
        as described in the UserApp Resource of the OneLogin API
        """
        user_app = UserApp(data={})
        expected_attributes = ['connector_id', 'icon_url', 'name', 'extension', 'login_id', 'id']

        for attr in expected_attributes:
            self.assertTrue(hasattr(user_app, attr), "UserApp has no attribute '{}'".format(attr))

    def testUserAppsV1Payload(self):
        user_app = UserApp(self.user_apps_v1_payload);
        self.assertEqual(unicode(user_app), unicode(self.getTestUserAppV1()))

    def testUserAppsV2Payload(self):
        user_app = UserApp(self.user_apps_v2_payload);
        expected_user_app = self.getTestUserAppV2()
        for attr in ['connector_id', 'extension', 'icon_url', 'id', 'login_id', 'name', 'provisioning_enabled', 'provisioning_state', 'provisioning_status']:
            self.assertEqual(getattr(user_app, attr), getattr(expected_user_app, attr))
