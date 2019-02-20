#!/usr/bin/python

class MFAToken(object):
    def __init__(self, data):
        self.value = data.get('mfa_token', None)
        self.reusable = data.get('reusable', None)
        self.expires_at = data.get('expires_at', None)
