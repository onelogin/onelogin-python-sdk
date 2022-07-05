# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.risk_score import RiskScore
import unittest

class OneLogin_API_Model_RiskScore_Test(unittest.TestCase):

    risk_score_v2_payload = {"score": 24, "triggers": ["Accessed from a new IP address", "Infrequent access from 125.238.248.246", "Infrequent access from Auckland, Auckland, New Zealand", "Infrequent access from New Zealand", "Infrequent access using Chrome on Macintosh", "Low trust for session"], "messages": []}

    def getTestRiskScoreV1(self):
        test_risk_score = RiskScore({})
        test_risk_score.score = 24
        test_risk_score.triggers = ["Accessed from a new IP address", "Infrequent access from 125.238.248.246", "Infrequent access from Auckland, Auckland, New Zealand", "Infrequent access from New Zealand", "Infrequent access using Chrome on Macintosh", "Low trust for session"]
        test_risk_score.messages = []
        return test_risk_score

    def testRiskScore(self):
        """
        Tests the constructor method of the RiskScore class
        Build a RiskScore object and check if all the expected attributes exist
        as described in the RiskScore Resource of the OneLogin API
        """
        risk_score = RiskScore({})
        expected_attributes = ['score', 'triggers', 'messages']
        for attr in expected_attributes:
            self.assertTrue(hasattr(risk_score, attr), "RiskScore has no attribute '{}'".format(attr))

    def testRiskScoreV1Payload(self):
        risk_score = RiskScore(self.risk_score_v2_payload)
        expected_risk_score = self.getTestRiskScoreV1()
        self.assertEqual(risk_score.__dict__, expected_risk_score.__dict__)
