#!/usr/bin/python

from onelogin.api.util.utils import str2int

from .base import Base


class SmartMFA(Base):
    def __init__(self, data):
        self.user_id = str2int(data.get('user_id', None))
        self.risk = data.get('risk', None)
        self.mfa = data.get('mfa', None)