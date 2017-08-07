#!/usr/bin/python


class Role(object):
    def __init__(self, data):
        self.id = data.get('id', None)
        self.name = data.get('name', '')
