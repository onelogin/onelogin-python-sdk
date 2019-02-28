#!/usr/bin/python


class EventType(object):
    def __init__(self, data):
        self.id = data.get('id', None)
        self.name = data.get('name', '')
        self.description = data.get('description', '')
