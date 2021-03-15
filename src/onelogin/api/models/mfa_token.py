#!/usr/bin/python

from onelogin.api.util.utils import str2date

from .base import Base


class MFAToken(Base):
    def __init__(self, data):
        self.value = data.get('mfa_token', None)
        self.reusable = data.get('reusable', None)
        self.expires_at = str2date(data.get('expires_at', None))
