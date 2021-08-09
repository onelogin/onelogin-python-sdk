# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.privilege import Privilege
from onelogin.api.models.statement import Statement
from onelogin.api.util.constants import Constants
import unittest


class OneLogin_API_Model_Privilege_Test(unittest.TestCase):

    privileges_v1_payload = {"id": "2c963197-bee2-4607-abc0-4786f1bfa55a", "name": "User Administrator", "description": "Can administer users", "privilege": {"Version": "2018-05-18", "Statement": [{"Effect": "Allow", "Action": ["users:ForceLogout", "users:ResetPassword","users:Unlock", "users:Get"],"Scope": ["*"]}]}}

    privilege_v1_payload = {"id": "2c963197-bee2-4607-abc0-4786f1bfa55a", "name": "User Administrator", "description": "Can administer users", "privilege": { "Version": "2018-05-18", "Statement": [{"Effect": "Allow", "Action": ["users:Delete", "users:ForceLogout", "users:ResetPassword", "users:Unlock", "users:Get"], "Scope": ["*"]}]}}

    def getTestPrivilegesV1(self):
        test_privilege = Privilege({})
        test_privilege.id = "2c963197-bee2-4607-abc0-4786f1bfa55a"
        test_privilege.name = "User Administrator"
        test_privilege.description = "Can administer users"
        statement = Statement('Allow', ['users:ForceLogout', 'users:ResetPassword', 'users:Unlock', 'users:Get'], ['*'])
        test_privilege.statements = [statement]
        test_privilege.version = "2018-05-18"
        return test_privilege

    def getTestPrivilegeV1(self):
        test_privilege = Privilege({})
        test_privilege.description = "Can administer users"
        test_privilege.id = "2c963197-bee2-4607-abc0-4786f1bfa55a"
        test_privilege.name = "User Administrator"
        statement = Statement({'Action': ['users:Delete', 'users:ForceLogout', 'users:ResetPassword', 'users:Unlock', 'users:Get'], 'Scope': ['*'], 'Effect': 'Allow'})
        test_privilege.statements = [statement]
        test_privilege.version = "2018-05-18"
        return test_privilege

    def testPrivilege(self):
        """
        Tests the constructor method of the Privilege class
        Build a Privilege object and check if all the expected attributes exist
        as described in the Privilege Resource of the OneLogin API
        """
        privilege = Privilege({})
        expected_attributes = ['id', 'name', 'description', 'statements']
        for attr in expected_attributes:
            self.assertTrue(hasattr(privilege, attr), "Privilege has no attribute '{}'".format(attr))

    def testFromDataPrivilege(self):
        privilege = Privilege({"id": "2c963197-bee2-4607-abc0-4786f1bfa55a", "name":"User Administrator", "description": "Can administer users"})
        expected_attributes = ['id', 'name', 'description', 'statements']
        for attr in expected_attributes:
            self.assertTrue(hasattr(privilege, attr), "Privilege has no attribute '{}'".format(attr))        

    def testFromValuesPrivilege(self):
        privilege = Privilege("2c963197-bee2-4607-abc0-4786f1bfa55a", "User Administrator", "2018-05-18", [{'Action': ['users:Delete', 'users:ForceLogout', 'users:ResetPassword', 'users:Unlock', 'users:Get'], 'Scope': ['*'], 'Effect': 'Allow'}])
        expected_attributes = ['id', 'name', 'description', 'version', 'statements']
        for attr in expected_attributes:
            self.assertTrue(hasattr(privilege, attr), "Privilege has no attribute '{}'".format(attr))        

    def testGetValidActions(self):
        self.assertEqual(Privilege.get_valid_actions(), Constants.VALID_ACTIONS)

    def testPrivilegesV1Payload(self):
        privilege = Privilege(self.privileges_v1_payload);
        expected_privilege = self.getTestPrivilegesV1()
        self.assertEqual(len(privilege.statements), len(expected_privilege.statements))
        for i in range(len(privilege.statements)):
            self.assertEqual(privilege.statements[i].__dict__, expected_privilege.statements[i].__dict__)
        privilege.statements = expected_privilege.statements = {}
        self.assertEqual(privilege.__dict__, expected_privilege.__dict__)

    def testPrivilegeV1Payload(self):
        privilege = Privilege(self.privilege_v1_payload);
        expected_privilege = self.getTestPrivilegeV1()
        self.assertEqual(len(privilege.statements), len(expected_privilege.statements))
        for i in range(len(privilege.statements)):
            self.assertEqual(privilege.statements[i].__dict__, expected_privilege.statements[i].__dict__)
        privilege.statements = expected_privilege.statements = {}
        self.assertEqual(privilege.__dict__, expected_privilege.__dict__)
