# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.

import unittest

from onelogin.api.models.embed_app import EmbedApp

class OneLogin_API_Models_EmbedApp_Test(unittest.TestCase):

    app_data = {
        'id': '1234',
        'icon': 'https://some.img',
        'name': 'Demo App',
        'provisioned': '0',
        'extension_required': '1',
        'personal': '0',
        'login_id': '5678'
    }

    app_data_truthy_values = {
        'id': '1234',
        'icon': 'https://some.img',
        'name': 'Demo App',
        'provisioned': '1',
        'extension_required': 'true',
        'personal': '1',
        'login_id': '5678'
    }

    app_data_falsey_values = {
        'id': '1234',
        'icon': 'https://some.img',
        'name': 'Demo App',
        'provisioned': '0',
        'extension_required': 'false',
        'personal': '0',
        'login_id': '5678'
    }

    def testEmbedAppInitialization(self):
        embed_app = EmbedApp(self.app_data)

        self.assertEqual(1234, embed_app.id)
        self.assertEqual('https://some.img', embed_app.icon)
        self.assertEqual('Demo App', embed_app.name)
        self.assertEqual(False, embed_app.provisioned)
        self.assertEqual(True, embed_app.extension_required)
        self.assertEqual(False, embed_app.personal)
        self.assertEqual(5678, embed_app.login_id)

    def testEmbedAppInitializationTruthyValues(self):
        embed_app = EmbedApp(self.app_data_truthy_values)

        self.assertEqual(True, embed_app.provisioned)
        self.assertEqual(True, embed_app.extension_required)
        self.assertEqual(True, embed_app.personal)

    def testEmbedAppInitializationFalseyValues(self):
        embed_app = EmbedApp(self.app_data_falsey_values)

        self.assertEqual(False, embed_app.provisioned)
        self.assertEqual(False, embed_app.extension_required)
        self.assertEqual(False, embed_app.personal)
