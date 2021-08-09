# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.assigned_admin import AssignedAdmin
import unittest
import datetime
from dateutil.tz import tzutc

import sys
if sys.version_info[0] >= 3:
    unicode = str

# noinspection PySetFunctionToLiteral
class OneLogin_API_AssignedAdmin_Test(unittest.TestCase):

    role_admins_v2_payload = {"id": 345, "name": "Joe User", "username": "joe.user@example.com","added_by": {"id":678, "name:": "Susan Boss"}, "added_at": "2019-12-27T00:00:00Z", "assigned": True}

    def getTestRoleAdminsAppV2(self):
        test_assigned_admin = AssignedAdmin(data={})
        test_assigned_admin.added_at = datetime.datetime(2019, 12, 27, 0, 0, tzinfo=tzutc())
        test_assigned_admin.added_by = {'name:': 'Susan Boss', 'id': 678}
        test_assigned_admin.assigned = True
        test_assigned_admin.email = None
        test_assigned_admin.id = 345
        test_assigned_admin.name = "Joe User"
        test_assigned_admin.username = "joe.user@example.com"
        return test_assigned_admin

    def testRoleAdmin(self):
        """
        Tests the constructor method of the AssignedAdmin class
        Build a AssignedAdmin object and check if all the expected attributes exist
        as described in the AssignedAdmin Resource of the OneLogin API
        """
        assigned_admin = AssignedAdmin(data={})
        expected_attributes = ['id', 'name', 'username', 'email', 'added_by', 'added_at', 'assigned']

        for attr in expected_attributes:
            self.assertTrue(hasattr(assigned_admin, attr), "AssignedAdmin has no attribute '{}'".format(attr))

    def testGetAddedBy(self):
        assigned_admin = AssignedAdmin(self.role_admins_v2_payload);
        self.assertEqual(assigned_admin.get_added_by(), {'name:': 'Susan Boss', 'id': 678})

    def testRoleUsersV2Payload(self):
        assigned_admin = AssignedAdmin(self.role_admins_v2_payload);
        expected_assigned_admin = self.getTestRoleAdminsAppV2()
        self.assertEqual(assigned_admin.added_by, expected_assigned_admin.added_by)
        assigned_admin.added_by = expected_assigned_admin.added_by = {}
        self.assertEqual(unicode(assigned_admin), unicode(expected_assigned_admin))
