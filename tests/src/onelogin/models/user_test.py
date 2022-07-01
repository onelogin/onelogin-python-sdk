# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.user import User, UserData, UserMetadata
import unittest
import datetime
from dateutil.tz import tzutc

# noinspection PySetFunctionToLiteral
class OneLogin_API_User_Test(unittest.TestCase):

    users_v1_payload = {
        "activated_at": "2019-12-02T17:16:03.432Z",
        "created_at": "2019-12-02T17:15:44.371Z",
        "email":"hazel.zhang@onelogin.com",
        "username":"hzhang",
        "firstname":"Hazel",
        "group_id": 1,
        "id": 63899829,
        "invalid_login_attempts": 0,
        "invitation_sent_at": None,
        "last_login": "2019-12-02T17:30:48.624Z",
        "lastname":"Zhang",
        "locked_until": None,
        "comment": "x",
        "openid_name":"hazel.zhang",
        "locale_code": "es",
        "preferred_locale_code": "es",
        "password_changed_at": "2019-12-02T17:16:03.514Z",
        "phone": "",
        "status": 1,
        "updated_at": "2019-12-02T17:30:48.647Z",
        "distinguished_name": None,
        "external_id": None,
        "directory_id": None,
        "member_of": None,
        "samaccountname": None,
        "userprincipalname": None,
        "manager_ad_id": None,
        "manager_user_id": None,
        "role_id": [
           77777,
           111111
        ],
        "company": "OneLogin",
        "department": "Finance",
        "title": "Captain",
        "state": 1,
        "trusted_idp_id": None
    }

    user_v1_payload = {
        "activated_at": "2019-12-02T17:16:03.432Z",
        "created_at": "2019-12-02T17:15:44.371Z",
        "email":"hazel.zhang@onelogin.com",
        "username":"hzhang",
        "firstname":"Hazel",
        "group_id": 1,
        "id": 63899829,
        "invalid_login_attempts": 0,
        "invitation_sent_at": None,
        "last_login": "2019-12-02T17:30:48.624Z",
        "lastname":"Zhang",
        "locked_until": None,
        "comment": "x",
        "openid_name":"hazel.zhang",
        "locale_code": "es",
        "preferred_locale_code": "es",
        "password_changed_at": "2019-12-02T17:16:03.514Z",
        "phone": "",
        "status": 1,
        "updated_at": "2019-12-02T17:30:48.647Z",
        "distinguished_name": None,
        "external_id": None,
        "directory_id": None,
        "member_of": None,
        "samaccountname": None,
        "userprincipalname": None,
        "manager_ad_id": None,
        "manager_user_id": None,
        "role_id": [
           77777,
           111111
        ],
        "company": "OneLogin",
        "department": "Finance",
        "title": "Captain",
        "state": 1,
        "trusted_idp_id": None
    }

    users_v2_payload = {
        "activated_at": None,
        "distinguished_name": None,
        "external_id": None,
        "firstname": "Mike",
        "last_login": None,
        "lastname": "Tester",
        "directory_id": None,
        "invitation_sent_at": None,
        "member_of": None,
        "updated_at": "2019-08-22T18:43:55.188Z",
        "created_at": "2019-08-22T18:43:55.188Z",
        "id": 56781966,
        "invalid_login_attempts": 0,
        "locked_until": None,
        "username": None,
        "email": "mike.tester@onelogin.com",
        "phone": None,
        "state": 1,
        "group_id": None,
        "password_changed_at": "2019-08-22T18:43:55.172Z",
        "status": 1,
        "samaccountname": None
    }

    user_v2_payload = {
        "activated_at": "2017-12-12T23:59:28.665Z",
        "distinguished_name": None,
        "external_id": None,
        "firstname": "Kelly",
        "last_login": "2020-06-03T19:59:21.382Z",
        "lastname": "Slater",
        "company": "WSL",
        "directory_id": None,
        "invitation_sent_at": None,
        "member_of": None,
        "updated_at": "2020-07-09T03:08:52.774Z",
        "preferred_locale_code": None,
        "created_at": "2017-12-12T23:57:56.781Z",
        "userprincipalname": None,
        "trusted_idp_id": None,
        "comment": "",
        "title": "Surfer",
        "role_ids": [
            199848,
            272445
        ],
        "department": "Waves",
        "id": 36216766,
        "custom_attributes": {
            "employeenumber": None,
            "food": "chicken"
        },
        "invalid_login_attempts": 0,
        "manager_user_id": None,
        "locked_until": "2020-07-08T21:59:56.811Z",
        "username": "kellyslater",
        "manager_ad_id": None,
        "email": "kelly+preprod@onelogin.com",
        "phone": "+64272001122",
        "state": 1,
        "group_id": None,
        "password_changed_at": "2019-08-22T18:44:26.542Z",
        "status": 3,
        "samaccountname": None
    }

    dry_run_mapping_user = {
      "id": 2,
      "firstname": "Mike",
      "lastname": "tester",
      "username": "miketester",
      "email": "miketester@onelogin.com"
    }

    def getTestUserV1(self):
        test_user = User({})
        test_user.activated_at=datetime.datetime(2019, 12, 2, 17, 16, 3, 432000, tzinfo=tzutc())
        test_user.comment="x"
        test_user.company="OneLogin"
        test_user.created_at=datetime.datetime(2019, 12, 2, 17, 15, 44, 371000, tzinfo=tzutc())
        test_user.custom_attributes={}
        test_user.department="Finance"
        test_user.directory_id=None
        test_user.distinguished_name=None
        test_user.email="hazel.zhang@onelogin.com"
        test_user.external_id=None
        test_user.firstname="Hazel"
        test_user.group_id=1
        test_user.id=63899829
        test_user.invalid_login_attempts=0
        test_user.invitation_sent_at=None
        test_user.last_login=datetime.datetime(2019, 12, 2, 17, 30, 48, 624000, tzinfo=tzutc())
        test_user.lastname="Zhang"
        test_user.locale_code="es"
        test_user.locked_until=None
        test_user.manager_ad_id=None
        test_user.manager_user_id=None
        test_user.member_of=None
        test_user.openid_name="hazel.zhang"
        test_user.password_changed_at=datetime.datetime(2019, 12, 2, 17, 16, 3, 514000, tzinfo=tzutc())
        test_user.phone=""
        test_user.role_ids=[77777, 111111]
        test_user.samaccountname=None
        test_user.state=1
        test_user.status=1
        test_user.title="Captain"
        test_user.trusted_idp_id=None
        test_user.updated_at=datetime.datetime(2019, 12, 2, 17, 30, 48, 647000, tzinfo=tzutc())
        test_user.username="hzhang"
        test_user.userprincipalname=None
        return test_user

    def getTestUsersV2(self):
        test_user = User({})
        test_user.activated_at = None
        test_user.comment = ""
        test_user.company = ""
        test_user.custom_attributes = {}
        test_user.department = ""
        test_user.directory_id = None
        test_user.distinguished_name = None
        test_user.email = "mike.tester@onelogin.com"
        test_user.external_id = None
        test_user.firstname = "Mike"
        test_user.group_id = None
        test_user.id = 56781966
        test_user.invalid_login_attempts = 0
        test_user.invitation_sent_at = None
        test_user.last_login = None
        test_user.lastname = "Tester"
        test_user.locale_code = ""
        test_user.locked_until = None
        test_user.manager_ad_id = None
        test_user.manager_user_id = None
        test_user.member_of = None
        test_user.openid_name = ""
        test_user.phone = None
        test_user.role_ids = []
        test_user.samaccountname = None
        test_user.state = 1
        test_user.status = 1
        test_user.title = ""
        test_user.trusted_idp_id = None
        test_user.username = None
        test_user.userprincipalname = ""
        test_user.created_at = datetime.datetime(2019, 8, 22, 18, 43, 55, 188000, tzinfo=tzutc())
        test_user.updated_at = datetime.datetime(2019, 8, 22, 18, 43, 55, 188000, tzinfo=tzutc())
        test_user.password_changed_at = datetime.datetime(2019, 8, 22, 18, 43, 55, 172000, tzinfo=tzutc())
        return test_user

    def getTestUserV2(self):
        test_user = User({})
        test_user.activated_at = datetime.datetime(2017, 12, 12, 23, 59, 28, 665000, tzinfo=tzutc())
        test_user.comment = ""
        test_user.company = "WSL"
        test_user.created_at = datetime.datetime(2017, 12, 12, 23, 57, 56, 781000, tzinfo=tzutc())
        test_user.custom_attributes = {'employeenumber': None, 'food': 'chicken'}
        test_user.department = "Waves"
        test_user.directory_id = None
        test_user.distinguished_name = None
        test_user.email = "kelly+preprod@onelogin.com"
        test_user.external_id = None
        test_user.firstname = "Kelly"
        test_user.group_id = None
        test_user.id = 36216766
        test_user.invalid_login_attempts = 0
        test_user.invitation_sent_at = None
        test_user.last_login = datetime.datetime(2020, 6, 3, 19, 59, 21, 382000, tzinfo=tzutc())
        test_user.lastname = "Slater"
        test_user.locale_code = ""
        test_user.locked_until = datetime.datetime(2020, 7, 8, 21, 59, 56, 811000, tzinfo=tzutc())
        test_user.manager_ad_id = None
        test_user.manager_user_id = None
        test_user.member_of = None
        test_user.openid_name = ""
        test_user.password_changed_at = datetime.datetime(2019, 8, 22, 18, 44, 26, 542000, tzinfo=tzutc())
        test_user.phone = "+64272001122"
        test_user.role_ids = [199848, 272445]
        test_user.samaccountname = None
        test_user.state = 1
        test_user.status = 3
        test_user.title = "Surfer"
        test_user.trusted_idp_id = None
        test_user.updated_at = datetime.datetime(2020, 7, 9, 3, 8, 52, 774000, tzinfo=tzutc())
        test_user.username = "kellyslater"
        test_user.userprincipalname = None
        return test_user

    def getTestUserDryRun(self):
        test_user = User({})
        test_user.id = 2
        test_user.username = "miketester"
        test_user.email = "miketester@onelogin.com"
        test_user.firstname = "Mike"
        test_user.lastname = "tester"
        return test_user

    def getUserData(self):
        test_user_data = UserData()
        test_user_data.company = ""
        test_user_data.department = ""
        test_user_data.directory_id = None
        test_user_data.distinguished_name = None
        test_user_data.email = "mike.tester@onelogin.com"
        test_user_data.external_id = None
        test_user_data.firstname = "Mike"
        test_user_data.id = 56781966
        test_user_data.lastname = "Tester"
        test_user_data.locale_code = ""
        test_user_data.manager_ad_id = None
        test_user_data.manager_user_id = None
        test_user_data.member_of = None
        test_user_data.openid_name = ""
        test_user_data.phone = None
        test_user_data.samaccountname = None
        test_user_data.state = 1
        test_user_data.status = 1
        test_user_data.trusted_idp_id = None
        test_user_data.username = None
        test_user_data.userprincipalname = ""
        return test_user_data

    def getUserMetaData(self):
        test_user_metadata = UserMetadata()
        test_user_metadata.comment = ""
        test_user_metadata.created_at = datetime.datetime(2019, 8, 22, 18, 43, 55, 188000, tzinfo=tzutc())
        test_user_metadata.id = 56781966
        test_user_metadata.invalid_login_attempts = 0
        test_user_metadata.invitation_sent_at = None
        test_user_metadata.last_login = None
        test_user_metadata.locked_until = None
        test_user_metadata.password_changed_at = datetime.datetime(2019, 8, 22, 18, 43, 55, 172000, tzinfo=tzutc())
        test_user_metadata.updated_at = datetime.datetime(2019, 8, 22, 18, 43, 55, 188000, tzinfo=tzutc())
        return test_user_metadata

# for att in dir(user):
#   print("test_user.%s = %s" % (att, getattr(user, att)))

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
            'role_ids', 'samaccountname', 'comment', 'state', 'status', 'updated_at', 'username', 'userprincipalname'
        ]

        for attr in expected_attributes:
            self.assertTrue(hasattr(user, attr), "User has no attribute '{}'".format(attr))

    def testUsersV1Payload(self):
        user = User(self.users_v1_payload)
        self.assertEqual(user.__dict__, self.getTestUserV1().__dict__)

    def testUserV1Payload(self):
        user = User(self.user_v1_payload)
        self.assertEqual(user.__dict__, self.getTestUserV1().__dict__)

    def testUsersV2Payload(self):
        user = User(self.users_v2_payload)
        self.assertEqual(user.__dict__, self.getTestUsersV2().__dict__)

    def testUserV2Payload(self):
        user = User(self.user_v2_payload)
        self.assertEqual(user.__dict__, self.getTestUserV2().__dict__)

    def testDryRunMapping(self):
        user = User(self.dry_run_mapping_user)
        self.assertEqual(user.__dict__, self.getTestUserDryRun().__dict__)

    def testGetRoleIds(self):
        user = User(self.users_v1_payload)
        self.assertEqual(user.get_role_ids(), [77777, 111111])

        user = User(self.users_v2_payload)
        self.assertEqual(user.get_role_ids(), [])

    def testGetGroupId(self):
        user = User(self.users_v1_payload)
        self.assertEqual(user.get_group_id(), 1)

        user = User(self.users_v2_payload)
        self.assertEqual(user.get_group_id(), None)

    def testGetCustomAttributes(self):
        user = User(self.users_v2_payload)
        self.assertEqual(user.get_custom_attributes(), {})

        user = User(self.user_v2_payload)
        self.assertEqual(user.get_custom_attributes(), {'employeenumber': None, 'food': 'chicken'})

    def testGetCustomAttribute(self):
        user = User(self.users_v2_payload)
        self.assertIsNone(user.get_custom_attribute('employeenumber'))

        user = User(self.user_v2_payload)
        self.assertIsNone(user.get_custom_attribute('social_id'))
        self.assertIsNone(user.get_custom_attribute('employeenumber'))
        self.assertEqual(user.get_custom_attribute('food'), 'chicken')

    def testGetUserData(self):
        user = User(self.users_v2_payload)
        user_data = user.get_user_data()
        self.assertTrue(isinstance(user_data, UserData))
        expected_user_data = self.getUserData()
        for att in ["company", "department", "directory_id", "distinguished_name", "email", 
            "external_id", "firstname", "id", "lastname", "locale_code", "manager_ad_id", "manager_user_id", 
            "member_of", "openid_name", "phone", "samaccountname", "state", "status", "trusted_idp_id",
            "username", "userprincipalname"]:
            self.assertEqual(getattr(expected_user_data, att), getattr(user_data, att))

    def testGetUserMetadata(self):
        user = User(self.users_v2_payload)
        user_metadata = user.get_user_metadata()
        self.assertTrue(isinstance(user_metadata, UserMetadata))
        expected_user_metadata = self.getUserMetaData()
        for att in ["id", "comment", "created_at", "invalid_login_attempts", "invitation_sent_at", "last_login", "locked_until", "password_changed_at", "updated_at"]:
            self.assertEqual(getattr(expected_user_metadata, att), getattr(user_metadata, att))

    def testGetUserParams(self):
        user = User(self.users_v2_payload)
        expected_user_params = {'userprincipalname': '', 'openid_name': '', 'department': '', 'manager_ad_id': None, 'group_id': None, 'status': 1, 'locale_code': '', 'invalid_login_attempts': 0, 'phone': None, 'member_of': None, 'samaccountname': None, 'company': '', 'email': 'mike.tester@onelogin.com', 'lastname': 'Tester', 'manager_user_id': None, 'firstname': 'Mike', 'username': None, 'state': 1, 'external_id': None, 'distinguished_name': None, 'directory_id': None, 'trusted_idp_id': None}
        user_params = user.get_user_params()
        self.assertEqual(expected_user_params, user_params)
