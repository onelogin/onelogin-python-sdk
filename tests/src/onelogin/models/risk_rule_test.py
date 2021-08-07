# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.risk_rule import RiskRule
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str


class OneLogin_API_RiskRule_Test(unittest.TestCase):

    risk_rules_v2_payload = {"id": "132456789", "name": "IP Blacklist for Guests", "description": "Blacklist for guest account users", "type": "blacklist", "target": "location.ip", "source": "guest-123", "filters": "123.123.123.123"}

    risk_rule_v2_payload = {"id": "132456789", "name": "IP Blacklist for Guests", "description": "Blacklist for guest account users", "type": "blacklist", "target": "location.ip", "source": "guest-123", "filters": "123.123.123.123"}

    def getTestRiskRulesV2(self):
        test_risk_rule = RiskRule({})
        test_risk_rule.description = "Blacklist for guest account users"
        test_risk_rule.filters = "123.123.123.123"
        test_risk_rule.id = 132456789
        test_risk_rule.name = "IP Blacklist for Guests"
        test_risk_rule.source = "guest-123"
        test_risk_rule.target = "location.ip"
        test_risk_rule.type = "blacklist"
        return test_risk_rule

    def getTestRiskRuleV2(self):
        test_risk_rule = RiskRule({})
        test_risk_rule.description = "Blacklist for guest account users"
        test_risk_rule.filters = "123.123.123.123"
        test_risk_rule.id = 132456789
        test_risk_rule.name = "IP Blacklist for Guests"
        test_risk_rule.source = "guest-123"
        test_risk_rule.target = "location.ip"
        test_risk_rule.type = "blacklist"

        return test_risk_rule

    def testRiskRuleAttributes(self):
        """
        Tests the constructor method of the RiskRule class
        Build a RiskRule object and check if all the expected attributes exist
        as described in the RiskRule Resource of the OneLogin API
        """
        risk_rule = RiskRule(data={})
        expected_attributes = ["id", "name", "description", "type", "target", "source", "filters"]

        for attr in expected_attributes:
            self.assertTrue(hasattr(risk_rule, attr), "RiskRule has no attribute '{}'".format(attr))

    def testRiskRulesV2Payload(self):
        risk_rule = RiskRule(self.risk_rules_v2_payload);
        self.assertEqual(unicode(risk_rule), unicode(self.getTestRiskRulesV2()))        

    def testRiskRuleV2Payload(self):
        risk_rule = RiskRule(self.risk_rule_v2_payload);
        self.assertEqual(unicode(risk_rule), unicode(self.getTestRiskRuleV2()))