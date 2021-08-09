# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.group import Group
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str

class OneLogin_API_Model_Group_Test(unittest.TestCase):

    groups_v1_payload = {"id": 417333, "name": "employees", "reference": None}

    group_v1_payload = {"id": 425741, "name": "group.security.policy.default", "reference": None}

    def getTestGroupsV1(self):
        test_group = Group({})
        test_group.id = 417333
        test_group.name = "employees"
        test_group.reference = None
        return test_group

    def getTestGroupV1(self):
        test_group = Group({})
        test_group.id = 425741
        test_group.name = "group.security.policy.default"
        test_group.reference = None
        return test_group

    def testGroup(self):
        """
        Tests the constructor method of the Group class
        Build a Group object and check if all the expected attributes exist
        as described in the Group Resource of the OneLogin API
        """
        group = Group(data={})
        expected_attributes = ['id', 'name', 'reference']
        for attr in expected_attributes:
            self.assertTrue(hasattr(group, attr), "Group has no attribute '{}'".format(attr))

    def testGroupsV1Payload(self):
        group = Group(self.groups_v1_payload);
        self.assertEqual(unicode(group), unicode(self.getTestGroupsV1()))

    def testGroupV1Payload(self):
        group = Group(self.group_v1_payload);
        self.assertEqual(unicode(group), unicode(self.getTestGroupV1()))
