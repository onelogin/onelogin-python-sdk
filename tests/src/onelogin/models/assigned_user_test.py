# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.assigned_user import AssignedUser
import unittest
import datetime
from dateutil.tz import tzutc

import sys
if sys.version_info[0] >= 3:
    unicode = str

# noinspection PySetFunctionToLiteral
class OneLogin_API_AssignedUser_Test(unittest.TestCase):

    role_users_v2_payload = {"id": 345, "name": "Joe User", "username": "joe.user@example.com","added_by": {"id":678, "name:": "Susan Boss"}, "added_at": "2019-12-27T00:00:00Z", "assigned": True}

    def getTestRoleUsersAppV2(self):
        test_assigned_user = AssignedUser(data={})
        test_assigned_user.added_at = datetime.datetime(2019, 12, 27, 0, 0, tzinfo=tzutc())
        test_assigned_user.added_by = {'name:': 'Susan Boss', 'id': 678}
        test_assigned_user.assigned = True
        test_assigned_user.email = None
        test_assigned_user.id = 345
        test_assigned_user.name = "Joe User"
        test_assigned_user.username = "joe.user@example.com"
        return test_assigned_user

    def testRoleUser(self):
        """
        Tests the constructor method of the AssignedUser class
        Build a AssignedUser object and check if all the expected attributes exist
        as described in the AssignedUser Resource of the OneLogin API
        """
        assigned_user = AssignedUser(data={})
        expected_attributes = ['id', 'name', 'username', 'email', 'added_by', 'added_at', 'assigned']

        for attr in expected_attributes:
            self.assertTrue(hasattr(assigned_user, attr), "AssignedUser has no attribute '{}'".format(attr))

    def testGetAddedBy(self):
        assigned_user = AssignedUser(self.role_users_v2_payload);
        self.assertEqual(assigned_user.get_added_by(), {'name:': 'Susan Boss', 'id': 678})

    def testRoleUsersV2Payload(self):
        assigned_user = AssignedUser(self.role_users_v2_payload);
        expected_assigned_user = self.getTestRoleUsersAppV2()
        self.assertEqual(assigned_user.added_by, expected_assigned_user.added_by)
        assigned_user.added_by = expected_assigned_user.added_by = {}
        self.assertEqual(unicode(assigned_user), unicode(expected_assigned_user))
