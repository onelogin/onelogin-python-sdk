#!/usr/bin/python


class OTP_Device(object):
    def __init__(self, data):
        otp_device_id = data.get('id', None)
        self.id = int(otp_device_id) if otp_device_id is not None else None
        self.active = data.get('active', False)
        self.default = data.get('default', False)
        self.auth_factor_name = data.get('auth_factor_name', '')
        self.phone_number = data.get('phone_number', '')
        self.type_display_name = data.get('type_display_name', '')
        self.needs_trigger = data.get('needs_trigger', False)
        self.user_display_name = data.get('user_display_name', '')
        self.state_token = data.get('state_token', '')
