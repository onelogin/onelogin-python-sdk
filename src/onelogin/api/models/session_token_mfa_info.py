#!/usr/bin/python

from .device import Device
from .base import Base
from .user import User


class SessionTokenMFAInfo(Base):
    def __init__(self, data):
        if data['user']:
            self.user = User(data['user'])  # Partial info
        self.state_token = data.get('state_token', '')
        self.callback_url = data.get('callback_url', '')
        self.devices = []
        if data['devices']:
            for device in data['devices']:
                self.devices.append(Device(device))
