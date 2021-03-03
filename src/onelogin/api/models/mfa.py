#!/usr/bin/python

from .base import Base
from .device import Device
from .user import User


class MFA(Base):
    def __init__(self, data):
        self.state_token = str(data.get('state_token', ''))
        self.callback_url = str(data.get('callback_url', ''))
        self.user = None
        if data['user']:
            self.user = User(data['user'])
        self.devices = []
        if data['devices']:
            for device in data['devices']:
                self.devices.append(Device(device))
