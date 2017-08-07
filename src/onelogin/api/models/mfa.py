#!/usr/bin/python

from .device import Device
from .user import User


class MFA(object):
    def __init__(self, data):
        self.state_token = data.get('state_token', '')
        self.callback_url = data.get('callback_url', '')
        self.user = None
        if data['user']:
            self.user = User(data['user'])
        self.devices = []
        if data['devices']:
            for device in data['devices']:
                self.devices.append(Device(device))
