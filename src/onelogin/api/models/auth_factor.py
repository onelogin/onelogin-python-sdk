#!/usr/bin/python


class AuthFactor(object):
    def __init__(self, data):
        self.name = data.get('name', '')
        self.id = data.get('factor_id', None)
