#!/usr/bin/python

from dateutil import parser


class User(object):

    STATE_UNAPPROVED = 0
    STATE_APPROVED = 1
    STATE_REJECTED = 2
    STATE_UNLICENSED = 3

    STATUS_UNACTIVATED = 0
    STATUS_ACTIVE = 1
    STATUS_SUSPENDED = 2
    STATUS_LOCKED = 3
    STATUS_PASSWORD_EXPIRED = 4
    STATUS_AWAITING_PASSWORD_RESET = 5

    def __init__(self, data):
        self.id = data.get('id', None)
        self.external_id = data.get('external_id', None)
        self.email = data.get('email', '')
        self.username = data.get('username', '')
        self.firstname = data.get('firstname', '')
        self.lastname = data.get('lastname', '')
        self.distinguished_name = data.get('distinguished_name', '')
        self.phone = data.get('phone', '')
        self.company = data.get('company', '')
        self.department = data.get('department', '')
        self.title = data.get('title', '')
        self.status = data.get('status', '')
        self.member_of = data.get('member_of', '')
        self.samaccountname = data.get('samaccountname', '')
        self.userprincipalname = data.get('userprincipalname', '')
        self.group_id = data.get('group_id', None)
        if self.group_id:
            self.group_id = int(self.group_id)
        self.role_ids = data.get('role_id', [])
        self.custom_attributes = data.get('custom_attributes', {})
        self.openid_name = data.get('openid_name', '')
        self.locale_code = data.get('locale_code', '')
        # self.notes = data.get('notes', None)
        self.comment = data.get('comment', '')
        self.directory_id = data.get('directory_id', None)
        self.manager_ad_id = data.get('manager_ad_id', None)
        self.trusted_idp_id = data.get('trusted_idp_id', None)
        self.manager_user_id = data.get('manager_user_id', None)

        activated_info = data.get('activated_at', None)
        self.activated_at = parser.parse(data['activated_at']) if activated_info is not None else None

        created_info = data.get('created_at', None)
        self.created_at = parser.parse(data['created_at']) if created_info is not None else None

        updated_info = data.get('updated_at', None)
        self.updated_at = parser.parse(data['updated_at']) if updated_info is not None else None

        pw_changed_info = data.get('password_changed_at', None)
        self.password_changed_at = parser.parse(data['password_changed_at']) if pw_changed_info is not None else None

        invitation_sent_info = data.get('invitation_sent_at', None)
        self.invitation_sent_at = parser.parse(data['invitation_sent_at']) if invitation_sent_info is not None else None

        self.invalid_login_attempts = data.get('invalid_login_attempts', None)

        last_login_info = data.get('last_login', None)
        self.last_login = parser.parse(data['last_login']) if last_login_info is not None else None

        locked_until_info = data.get('locked_until', None)
        self.locked_until = parser.parse(data['locked_until']) if locked_until_info is not None else None

        self.state = data.get('state', None)

    def get_role_ids(self):
        return self.role_ids

    def get_group_id(self):
        return self.group_id

    def get_user_data(self):
        user_data = UserData()
        user_data.id = self.id
        user_data.external_id = self.external_id
        user_data.email = self.email
        user_data.username = self.username
        user_data.firstname = self.firstname
        user_data.lastname = self.lastname
        user_data.distinguished_name = self.distinguished_name
        user_data.phone = self.phone
        user_data.company = self.company
        user_data.department = self.department
        user_data.status = self.status
        user_data.state = self.state
        user_data.member_of = self.member_of
        user_data.samaccountname = self.samaccountname
        user_data.userprincipalname = self.userprincipalname
        user_data.openid_name = self.openid_name
        user_data.locale_code = self.locale_code
        user_data.directory_id = self.directory_id
        user_data.manager_ad_id = self.manager_ad_id
        user_data.trusted_idp_id = self.trusted_idp_id
        user_data.manager_user_id = self.manager_user_id

    def get_user_metadata(self):
        user_metadata = UserMetadata()
        user_metadata.id = self.id
        user_metadata.activated_at = self.activated_at
        user_metadata.created_at = self.created_at
        user_metadata.updated_at = self.updated_at
        user_metadata.password_changed_at = self.password_changed_at
        user_metadata.invalid_login_attempts = self.invalid_login_attempts
        user_metadata.invitation_sent_at = self.invitation_sent_at
        user_metadata.last_login = self.last_login
        user_metadata.locked_until = self.locked_until
        user_metadata.comment = self.comment

    def get_custom_attributes(self):
        return self.custom_attributes

    def get_user_params(self):
        return {
            "external_id": self.external_id,
            "email": self.email,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "distinguished_name": self.distinguished_name,
            "phone": self.phone,
            "company": self.company,
            "department": self.department,
            "status": self.status,
            "state": self.state,
            "member_of": self.member_of,
            "samaccountname": self.samaccountname,
            "invalid_login_attempts": self.invalid_login_attempts,
            "userprincipalname": self.userprincipalname,
            "group_id": self.group_id,
            "locale_code": self.locale_code,
            # notes": self.notes,
            "openid_name": self.openid_name,
            "directory_id": self.directory_id,
            "manager_ad_id": self.manager_ad_id,
            "trusted_idp_id": self.trusted_idp_id,
            "manager_user_id": self.manager_user_id,
        }


class UserData(object):
    pass


class UserMetadata(object):
    pass
