#!/usr/bin/python


class Device(object):
    def __init__(self, data):
        self.id = data.get('device_id', None)
        self.type = data.get('device_type', '')
