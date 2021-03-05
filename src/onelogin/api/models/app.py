#!/usr/bin/python

from onelogin.api.util.utils import str2bool, str2int

from .base import Base


class App(Base):
    def __init__(self, data):
        self.id = str2int(data.get('id', None))
        self.name = data.get('name', '')
        if "icon" in data.keys():
            self.icon = data.get('icon', '')
        else:
            self.icon = data.get('icon_url', '')
        self.provisioned = str2bool(data.get('provisioned', None))
        self.extension = str2bool(data.get('extension', None))
        self.login_id = str2int(data.get('login_id', None))
        self.personal = str2bool(data.get('personal', None))
        self.provisioning_status  = data.get('provisioning_status', None)
        self.provisioning_state  = data.get('provisioning_state', None)
        self.provisioning_enabled  = data.get('provisioning_enabled', None)