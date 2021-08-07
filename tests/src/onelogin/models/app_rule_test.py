# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.app_rule import AppRule
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str


class OneLogin_API_Model_AppRule_Test(unittest.TestCase):

    app_rules_v2_payload = {"id": 196673, "name": "My first rule", "match": "all", "enabled": True, "position": 1, "conditions": [{"source": "last_login", "operator": ">", "value": "90"}],"actions": [{"action": "set_status","value": ["2"]}]}
    
    app_rule_v2_payload = {"id": 196670, "name": "My First rule", "match": "all", "enabled": True, "position": 1, "conditions": [{"source": "has_role", "operator": "ri", "value": "909876"}],"actions": [{"action": "set_groups", "value": ["member_of"], "expression": ".*"}]}

    def getTestAppRulesV2(self):
        test_app_rule = AppRule({})
        test_app_rule.actions = [{'action': 'set_status', 'value': ['2']}]
        test_app_rule.conditions = [{'value': '90', 'operator': '>', 'source': 'last_login'}]
        test_app_rule.enabled = True
        test_app_rule.id = 196673
        test_app_rule.match = "all"
        test_app_rule.name = "My first rule"
        test_app_rule.position = 1
        return test_app_rule

    def getTestAppRuleV2(self):
        test_app_rule = AppRule({})
        test_app_rule.actions = [{'action': 'set_groups', 'expression': '.*', 'value': ['member_of']}]
        test_app_rule.conditions = [{'source': 'has_role', 'operator': 'ri', 'value': '909876'}]
        test_app_rule.enabled = True
        test_app_rule.id = 196670
        test_app_rule.match = "all"
        test_app_rule.name = "My First rule"
        test_app_rule.position = 1
        return test_app_rule

    def testAppRuleAttributes(self):
        """
        Tests the constructor method of the AppRule class
        Build a AppRule object and check if all the expected attributes exist
        as described in the AppRule Resource of the OneLogin API
        """
        app_rule = AppRule(data={})
        expected_attributes = ["id", "name", "match", "enabled", "position", "conditions", "actions"]

        for attr in expected_attributes:
            self.assertTrue(hasattr(app_rule, attr), "AppRule has no attribute '{}'".format(attr))


    def testAppRulesV2Payload(self):
        app_rule = AppRule(self.app_rules_v2_payload);
        expected_app_rule = self.getTestAppRulesV2()
        self.assertEqual(app_rule.actions,expected_app_rule.actions)
        app_rule.actions = expected_app_rule.actions = []
        self.assertEqual(app_rule.conditions,expected_app_rule.conditions)
        app_rule.conditions = expected_app_rule.conditions = []
        self.assertEqual(unicode(app_rule), unicode(expected_app_rule))   

    def testAppRuleV2Payload(self):
        app_rule = AppRule(self.app_rule_v2_payload);
        expected_app_rule = self.getTestAppRuleV2()
        self.assertEqual(app_rule.actions,expected_app_rule.actions)
        app_rule.actions = expected_app_rule.actions = []
        self.assertEqual(app_rule.conditions,expected_app_rule.conditions)
        app_rule.conditions = expected_app_rule.conditions = []
        self.assertEqual(unicode(app_rule), unicode(expected_app_rule))   
