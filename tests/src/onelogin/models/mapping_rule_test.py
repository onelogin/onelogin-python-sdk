# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.mapping import Mapping
import unittest

class OneLogin_API_MappingRule_Test(unittest.TestCase):

    mappings_v2_payload = {"id": 196673, "name": "My first mapping", "match": "all", "enabled": True, "position": 1, "conditions": [{"source": "last_login", "operator": ">", "value": "90"}],"actions": [{"action": "set_status", "value": ["2"]}]}
    
    mapping_v2_payload = {"id": 196673, "name": "My first mapping", "match": "all", "enabled": True, "position": 1, "conditions": [{"source": "last_login", "operator": ">", "value": "90"}],"actions": [{"action": "set_status", "value": ["2"]}]}

    def getTestMappingsV2(self):
        test_mapping = Mapping({})
        test_mapping.actions = [{'action': 'set_status', 'value': ['2']}]
        test_mapping.conditions = [{'source': 'last_login', 'value': '90', 'operator': '>'}]
        test_mapping.enabled = True
        test_mapping.id = 196673
        test_mapping.match = "all"
        test_mapping.name = "My first mapping"
        test_mapping.position = 1
        return test_mapping

    def getTestMappingV2(self):
        test_mapping = Mapping({})
        test_mapping.actions = [{'action': 'set_status', 'value': ['2']}]
        test_mapping.conditions = [{'source': 'last_login', 'value': '90', 'operator': '>'}]
        test_mapping.enabled = True
        test_mapping.id = 196673
        test_mapping.match = "all"
        test_mapping.name = "My first mapping"
        test_mapping.position = 1
        return test_mapping

    def testMappingAttributes(self):
        """
        Tests the constructor method of the AppRule class
        Build a AppRule object and check if all the expected attributes exist
        as described in the AppRule Resource of the OneLogin API
        """
        test_mapping = Mapping(data={})
        expected_attributes = ["id", "name", "match", "enabled", "position", "conditions", "actions"]

        for attr in expected_attributes:
            self.assertTrue(hasattr(test_mapping, attr), "Mapping has no attribute '{}'".format(attr))

    def testMappingsV2Payload(self):
        mapping = Mapping(self.mappings_v2_payload)
        expected_mapping = self.getTestMappingsV2()
        self.assertEqual(mapping.actions,expected_mapping.actions)
        mapping.actions = expected_mapping.actions = []
        self.assertEqual(mapping.conditions,expected_mapping.conditions)
        mapping.conditions = expected_mapping.conditions = []
        self.assertEqual(mapping.__dict__, expected_mapping.__dict__)   

    def testMappingV2Payload(self):
        mapping = Mapping(self.mapping_v2_payload)
        expected_mapping = self.getTestMappingV2()
        self.assertEqual(mapping.actions,expected_mapping.actions)
        mapping.actions = expected_mapping.actions = []
        self.assertEqual(mapping.conditions,expected_mapping.conditions)
        mapping.conditions = expected_mapping.conditions = []
        self.assertEqual(mapping.__dict__, expected_mapping.__dict__)   
