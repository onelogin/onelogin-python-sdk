# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.app import App
from onelogin.api.models.event import Event
from onelogin.api.models.group import Group
from onelogin.api.models.otp_device import OTP_Device
from onelogin.api.models.role import Role

import unittest
import datetime
from dateutil.tz import tzutc

# noinspection PySetFunctionToLiteral
class OneLogin_API_Model_Event_Test(unittest.TestCase):

    events_v1_payload = {"id": 999999999, "created_at": "2014-12-19T02:02:39.276Z", "account_id": 55555, "user_id": 88888888, "event_type_id": 13, "notes": None, "ipaddr": "11.111.11.111", "actor_user_id": 7777777, "assuming_acting_user_id": None, "role_id": None, "app_id": None,
                         "group_id": None, "otp_device_id": None, "policy_id": None, "actor_system": "", "custom_message": None, "role_name": None, "app_name": None, "group_name": None, "actor_user_name": "Xavier Wong", "user_name": "Xavier Wong", "policy_name": None,
                         "otp_device_name": None, "operation_name": None, "directory_sync_run_id": None, "directory_id": None, "resolution": None, "client_id": None, "resource_type_id": None, "error_description": None, "proxy_ip": None, "risk_score": None, "risk_reasons": None,
                         "risk_cookie_id": None, "browser_fingerprint": None}

    event_v1_payload = {"id": 123456, "created_at": "2014-02-18T02:34:15.626Z", "account_id": 1, "user_id": 654321, "event_type_id": 8, "notes": "Initiated by OneLogin via SAML", "ipaddr": "123.456.789.0", "actor_user_id": 987654, "assuming_acting_user_id": None, "role_id": 2,
                         "app_id": 11111, "group_id": 1, "otp_device_id": 3, "policy_id": None, "actor_system": "", "custom_message": None, "role_name": "Admins", "app_name": "AppWonder", "group_name": "Group 1", "actor_user_name": "Santiago Cuong", "user_name": "Santiago Cuong",
                         "policy_name": None, "otp_device_name": "Device 3", "operation_name": None, "directory_sync_run_id": None, "directory_id": None, "resolution": None, "client_id": None, "resource_type_id": None, "error_description": None, "proxy_ip": None, "risk_score": 48,
                         "risk_reasons": "Infrequent access from 73.68.253.46 (13%)\nLow trust for session (15%)....", "risk_cookie_id": "1cc3xx9-6a0d-4643-8111-b5xx", "browser_fingerprint": "71fxxxxxxxxxxxbc184748e5a6b"}

    def getTestEventsV1(self):
        test_event = Event({})
        test_event.account_id = 55555
        test_event.actor_system = ""
        test_event.actor_user_id = 7777777
        test_event.actor_user_name = "Xavier Wong"
        test_event.app_id = None
        test_event.app_name = None
        test_event.assuming_acting_user_id = None
        test_event.browser_fingerprint = None
        test_event.client_id = None
        test_event.created_at = datetime.datetime(2014, 12, 19, 2, 2, 39, 276000, tzinfo=tzutc())
        test_event.custom_message = None
        test_event.directory_id = None
        test_event.directory_sync_run_id = None
        test_event.error_description = None
        test_event.event_type_id = 13
        test_event.group_id = None
        test_event.group_name = None
        test_event.id = 999999999
        test_event.ipaddr = "11.111.11.111"
        test_event.notes = None
        test_event.operation_name = None
        test_event.otp_device_id = None
        test_event.otp_device_name = None
        test_event.policy_id = None
        test_event.policy_name = None
        test_event.proxy_ip = None
        test_event.resolution = None
        test_event.resource_type_id = None
        test_event.risk_cookie_id = None
        test_event.risk_reasons = None
        test_event.risk_score = None
        test_event.role_id = None
        test_event.role_name = None
        test_event.user_id = 88888888
        test_event.user_name = "Xavier Wong"
        return test_event

    def getTestEventV1(self):
        test_event = Event({})
        test_event.account_id = 1
        test_event.actor_system = ""
        test_event.actor_user_id = 987654
        test_event.actor_user_name = "Santiago Cuong"
        test_event.app_id = 11111
        test_event.app_name = "AppWonder"
        test_event.assuming_acting_user_id = None
        test_event.browser_fingerprint = "71fxxxxxxxxxxxbc184748e5a6b"
        test_event.client_id = None
        test_event.created_at = datetime.datetime(2014, 2, 18, 2, 34, 15, 626000, tzinfo=tzutc())
        test_event.custom_message = None
        test_event.directory_id = None
        test_event.directory_sync_run_id = None
        test_event.error_description = None
        test_event.event_type_id = 8
        test_event.group_id = 1
        test_event.group_name = "Group 1"
        test_event.id = 123456
        test_event.ipaddr = "123.456.789.0"
        test_event.notes = "Initiated by OneLogin via SAML"
        test_event.operation_name = None
        test_event.otp_device_id = "3"
        test_event.otp_device_name = "Device 3"
        test_event.policy_id = None
        test_event.policy_name = None
        test_event.proxy_ip = None
        test_event.resolution = None
        test_event.resource_type_id = None
        test_event.risk_cookie_id = "1cc3xx9-6a0d-4643-8111-b5xx"
        test_event.risk_reasons = """Infrequent access from 73.68.253.46 (13%)
Low trust for session (15%)...."""
        test_event.risk_score = 48
        test_event.role_id = 2
        test_event.role_name = "Admins"
        test_event.user_id = 654321
        test_event.user_name = "Santiago Cuong"
        return test_event

    def testEvent(self):
        """
        Tests the constructor method of the Event class
        Build a Event object and check if all the expected attributes exist
        as described in the Event Resource of the OneLogin API
        """
        event = Event(data={})
        expected_attributes = ['account_id', 'actor_system', 'actor_user_id', 'actor_user_name', 'app_id', 'app_name', 'assuming_acting_user_id', 'browser_fingerprint', 'client_id', 'created_at', 'custom_message', 'directory_id', 'directory_sync_run_id', 'error_description', 'event_type_id', 'get_group', 'get_role', 'group_id', 'group_name', 'id', 'ipaddr', 'notes', 'operation_name', 'otp_device_id', 'otp_device_name', 'policy_id', 'policy_name', 'proxy_ip', 'resolution', 'resource_type_id', 'risk_cookie_id', 'risk_reasons', 'risk_score', 'role_id', 'role_name', 'user_id', 'user_name']
        for attr in expected_attributes:
            self.assertTrue(hasattr(event, attr), "Event has no attribute '{}'".format(attr))

    def testGroup(self):
        event = Event(self.events_v1_payload)
        group = event.get_group()
        self.assertIsNone(group)
        event = Event(self.event_v1_payload)
        group = event.get_group()
        self.assertTrue(isinstance(group, Group))
        self.assertEqual(group.id, 1)
        self.assertEqual(group.name, "Group 1")

    def testRole(self):
        event = Event(self.events_v1_payload)
        role = event.get_role()
        self.assertIsNone(role)
        event = Event(self.event_v1_payload)
        role = event.get_role()
        self.assertTrue(isinstance(role, Role))
        self.assertEqual(role.id, 2)
        self.assertEqual(role.name, "Admins")

    def testApp(self):
        event = Event(self.events_v1_payload)
        app = event.get_app()
        self.assertIsNone(app)
        event = Event(self.event_v1_payload)
        app = event.get_app()
        self.assertTrue(isinstance(app, App))
        self.assertEqual(app.id, 11111)
        self.assertEqual(app.name, "AppWonder")

    def testOTPDevice(self):
        event = Event(self.events_v1_payload)
        otp_device = event.get_otp_device()
        self.assertIsNone(otp_device)
        event = Event(self.event_v1_payload)
        otp_device = event.get_otp_device()
        self.assertTrue(isinstance(otp_device, OTP_Device))
        self.assertEqual(otp_device.id, "3")
        self.assertEqual(otp_device.auth_factor_name, "Device 3")

    def testEventsV1Payload(self):
        event = Event(self.events_v1_payload)
        self.assertEqual(event.__dict__, self.getTestEventsV1().__dict__)

    def testEventV1Payload(self):
        event = Event(self.event_v1_payload)
        self.assertEqual(event.__dict__, self.getTestEventV1().__dict__)
