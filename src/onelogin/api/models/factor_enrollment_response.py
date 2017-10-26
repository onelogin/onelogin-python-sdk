#!/usr/bin/python


class FactorEnrollmentResponse(object):
    def __init__(self, data):
        otp_device_id = data.get('device_id', None)
        self.device_id = int(otp_device_id) if otp_device_id is not None else None
        user_id = data.get('id', None)
        self.user_id = int(user_id) if user_id is not None else None
        self.active = data.get('active', False)
        self.auth_factor_name = data.get('auth_factor_name', '')
        self.type_display_name = data.get('type_display_name', '')
        self.user_display_name = data.get('user_display_name', '')
        self.state_token = data.get('state_token', '')
