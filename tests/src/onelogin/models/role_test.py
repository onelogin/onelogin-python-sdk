# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.role import Role
import unittest


class OneLogin_API_Model_Role_Test(unittest.TestCase):

    roles_v1_payload = {"id": 1111, "name": "C-Executive"}

    role_v1_payload = {"id": 123456, "name": "Employee"}

    roles_v2_payload = {"id": 285779, "name": "Default", "admins": [59305875], "apps": [1110783, 1105211], "users": [138442511]}

    role_v2_payload =  {"id": 452448,"name": "New Role", "admins": [], "apps": [], "users": [59305875, 60308064]}

    def getTestRolesV1(self):
        test_role = Role({})
        test_role.id = 1111
        test_role.name = "C-Executive"
        return test_role

    def getTestRoleV1(self):
        test_role = Role({})
        test_role.id = 123456
        test_role.name = "Employee"
        return test_role

    def getTestRolesV2(self):
        test_role = Role({})
        test_role.id = 285779
        test_role.name = "Default"
        test_role.admins = [59305875]
        test_role.apps = [1110783, 1105211]
        test_role.users = [138442511]
        return test_role

    def getTestRoleV2(self):
        test_role = Role({})
        test_role.id = 452448
        test_role.name = "New Role"
        test_role.admins = []
        test_role.apps = []
        test_role.users = [59305875, 60308064]
        return test_role

    def testRole(self):
        """
        Tests the constructor method of the Role class
        Build a Role object and check if all the expected attributes exist
        as described in the Role Resource of the OneLogin API
        """
        role = Role({})
        expected_attributes = ['id', 'name', 'admins', 'users', 'apps']
        for attr in expected_attributes:
            self.assertTrue(hasattr(role, attr), "Role has no attribute '{}'".format(attr))

    def testGetAdminIds(self):
        role = self.getTestRolesV1()
        self.assertIsNone(role.get_admin_ids())

        role = self.getTestRolesV2()
        self.assertEqual([59305875], role.get_admin_ids())

        role = self.getTestRoleV2()
        self.assertEqual([], role.get_admin_ids())

    def testGetUserIds(self):
        role = self.getTestRolesV1()
        self.assertIsNone(role.get_user_ids())

        role = self.getTestRolesV2()
        self.assertEqual([138442511], role.get_user_ids())

        role = self.getTestRoleV2()
        self.assertEqual([59305875, 60308064], role.get_user_ids())

    def testGetAppIds(self):
        role = self.getTestRolesV1()
        self.assertIsNone(role.get_app_ids())

        role = self.getTestRolesV2()
        self.assertEqual([1110783, 1105211], role.get_app_ids())

        role = self.getTestRoleV2()
        self.assertEqual([], role.get_app_ids())

    def testRolesV1Payload(self):
        role = Role(self.roles_v1_payload)
        expected_role = self.getTestRolesV1()
        self.assertEqual(role.__dict__, expected_role.__dict__)

    def testRoleV1Payload(self):
        role = Role(self.role_v1_payload)
        expected_role = self.getTestRoleV1()
        self.assertEqual(role.__dict__, expected_role.__dict__)

    def testRolesV2Payload(self):
        role = Role(self.roles_v2_payload)
        expected_role = self.getTestRolesV2()
        self.assertEqual(role.__dict__, expected_role.__dict__)

    def testRoleV2Payload(self):
        role = Role(self.role_v2_payload)
        expected_role = self.getTestRoleV2()
        self.assertEqual(role.__dict__, expected_role.__dict__)