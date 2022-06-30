# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.risk_score_insights import RiskScoreInsights
import unittest

class OneLogin_API_Model_RiskScoreInsights_Test(unittest.TestCase):

    risk_score_insights_v2_payload = {"scores": {"minimal": 50, "low": 165, "medium": 30, "high": 17, "very_high": 9}, "total": 271}

    def getTestRiskScoreInsightsV1(self):
        test_risk_score_insights = RiskScoreInsights({})
        test_risk_score_insights.scores = {"minimal": 50, "low": 165, "medium": 30, "high": 17, "very_high": 9}
        test_risk_score_insights.total = 271
        return test_risk_score_insights

    def testRiskScoreInsights(self):
        """
        Tests the constructor method of the RiskScoreInsights class
        Build a RiskScoreInsights object and check if all the expected attributes exist
        as described in the RiskScoreInsights Resource of the OneLogin API
        """
        risk_score_insights = RiskScoreInsights({})
        expected_attributes = ['scores', 'total']
        for attr in expected_attributes:
            self.assertTrue(hasattr(risk_score_insights, attr), "RiskScoreInsights has no attribute '{}'".format(attr))

    def testRiskScoreInsightsV1Payload(self):
        risk_score_insights = RiskScoreInsights(self.risk_score_insights_v2_payload);
        expected_risk_score_insights = self.getTestRiskScoreInsightsV1()
        self.assertEqual(risk_score_insights.__dict__, expected_risk_score_insights.__dict__)
