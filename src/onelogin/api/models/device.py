#!/usr/bin/python


class Device(object):
    def __init__(self, data):
        self.id = data.get('device_id', None)
        self.type = data.get('device_type', '')
        self.duo_api_hostname = data.get('duo_api_hostname', None)
        self.duo_sig_request = data.get('duo_sig_request', None)
