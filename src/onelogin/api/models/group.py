#!/usr/bin/python


class Group(object):
    def __init__(self, data):
        self.id = data.get('id', None)
        self.name = data.get('name', '')
        self.reference = data.get('reference', '')
