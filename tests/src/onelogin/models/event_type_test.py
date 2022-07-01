# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.event_type import EventType
import unittest

# noinspection PySetFunctionToLiteral
class OneLogin_API_Model_EventType_Test(unittest.TestCase):

    event_type_v1_payload = {"name": "APP_ADDED_TO_ROLE", "description": "App %app% added to role %role%", "id": 1}

    def getTestEventTypeV1(self):
        test_event_type = EventType({})
        test_event_type.id = 1
        test_event_type.name = "APP_ADDED_TO_ROLE"
        test_event_type.description = "App %app% added to role %role%"
        return test_event_type

    def testEventType(self):
        """
        Tests the constructor method of the EventType class
        Build a EventType object and check if all the expected attributes exist
        as described in the EventType Resource of the OneLogin API
        """
        event_type = EventType(data={})
        expected_attributes = ['id', 'name', 'description']
        for attr in expected_attributes:
            self.assertTrue(hasattr(event_type, attr), "EventType has no attribute '{}'".format(attr))

    def testEventTypeV1Payload(self):
        event_type = EventType(self.event_type_v1_payload)
        self.assertEqual(event_type.__dict__, self.getTestEventTypeV1().__dict__)
