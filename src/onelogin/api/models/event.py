#!/usr/bin/python

from dateutil import parser

from .group import Group
from .role import Role


class Event(object):
    def __init__(self, data):
        self.id = data.get('id', None)
        self.created_at = parser.parse(data['created_at'])
        self.account_id = data.get('account_id', None)
        self.user_id = data.get('user_id', None)
        self.user_name = data.get('user_name', '')
        self.event_type_id = data.get('event_type_id', None)
        self.notes = data.get('notes', '')
        self.ipaddr = data.get('ipaddr', '')
        self.actor_user_id = data.get('actor_user_id', None)
        self.actor_user_name = data.get('actor_user_name', '')
        self.assuming_acting_user_id = data.get('assuming_acting_user_id', None)
        self.role_id = data.get('role_id', None)
        self.role_name = data.get('role_name', '')
        self.app_id = data.get('app_id', None)
        self.app_name = data.get('app_name', None)
        self.group_id = data.get('group_id', None)
        self.group_name = data.get('group_name', '')
        self.otp_device_id = data.get('otp_device_id', None)
        self.otp_device_name = data.get('otp_device_name', '')
        self.policy_id = data.get('policy_id', None)
        self.policy_name = data.get('policy_name', '')
        self.actor_system = data.get('actor_system', '')
        self.custom_message = data.get('custom_message', '')
        self.operation_name = data.get('operation_name', '')
        self.directory_sync_run_id = data.get('directory_sync_run_id', None)
        self.directory_id = data.get('directory_id', None)
        self.resolution = data.get('resolution', '')
        self.client_id = data.get('client_id', None)
        self.resource_type_id = data.get('resource_type_id', None)
        self.error_description = data.get('error_description', '')
        self.proxy_ip = data.get('proxy_ip', None)
        self.risk_score = data.get('risk_score', None)
        self.risk_reasons = data.get('risk_reasons', None)
        self.risk_cookie_id = data.get('risk_cookie_id', None)
        self.browser_fingerprint = data.get('browser_fingerprint', None)

    def get_role(self):
        role = None
        if self.role_id is not None and self.role_name:
            role = Role(self.role_id, self.role_name)
        return role

    def get_group(self):
        group = None
        if self.group_id is not None and self.group_name:
            group = Group(self.group_id, self.group_name)
        return group
