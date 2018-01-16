#!/usr/bin/python


class App(object):
    def __init__(self, data):
        app_id = data.get('id', None)
        self.id = int(app_id) if app_id is not None else None
        self.name = data.get('name', '')
        self.icon = data.get('icon', '')
        self.provisioned = data.get('provisioned', None)
        self.extension = data.get('extension', None)
        self.login_id = data.get('login_id', None)
        self.personal = data.get('personal', None)
