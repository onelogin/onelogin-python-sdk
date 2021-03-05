#!/usr/bin/python

from onelogin.api.util.utils import str2int, str2bool

from .base import Base


class OTP_Device(Base):
    def __init__(self, data):
        self.id = str2int(data.get('id', None))
        self.active = str2bool(data.get('active', False))
        self.default = str2bool(data.get('default', False))
        self.auth_factor_name = data.get('auth_factor_name', '')
        self.phone_number = data.get('phone_number', '')
        self.type_display_name = data.get('type_display_name', '')
        self.needs_trigger = str2bool(data.get('needs_trigger', False))
        self.user_display_name = data.get('user_display_name', '')
        self.state_token = data.get('state_token', None)
