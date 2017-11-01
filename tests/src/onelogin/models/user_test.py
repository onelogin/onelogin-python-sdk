# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.user import User
import unittest


# noinspection PySetFunctionToLiteral
class OneLogin_API_User_Test(unittest.TestCase):

    def testUserAttributes(self):
        """
        Tests the constructor method of the User class
        Build a User object and check if all the expected attributes exist
        as described in the User Resource of the OneLogin API
        """
        user = User(data={})
        expected_attributes = [
            'created_at', 'custom_attributes', 'directory_id', 'distinguished_name', 'email', 'external_id',
            'firstname', 'group_id', 'id', 'invalid_login_attempts', 'invitation_sent_at', 'last_login', 'lastname',
            'locale_code', 'locked_until', 'manager_ad_id', 'member_of', 'openid_name', 'password_changed_at', 'phone',
            'role_ids', 'samaccountname', 'state', 'status', 'updated_at', 'username', 'userprincipalname'
        ]

        for attr in expected_attributes:
            self.assertTrue(hasattr(user, attr), "User has no attribute '{}'".format(attr))
