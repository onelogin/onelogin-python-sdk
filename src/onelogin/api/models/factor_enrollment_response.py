#!/usr/bin/python

from onelogin.api.util.utils import str2bool, str2int
from .base import Base


class FactorEnrollmentResponse(Base):
    def __init__(self, data):
        self.device_id = str2int(data.get('device_id', None))
        self.user_id = str2int(data.get('id', None))
        self.active = str2bool(data.get('active', False))
        self.auth_factor_name = data.get('auth_factor_name', '')
        self.type_display_name = data.get('type_display_name', '')
        self.user_display_name = data.get('user_display_name', '')
        self.state_token = data.get('state_token', '')
