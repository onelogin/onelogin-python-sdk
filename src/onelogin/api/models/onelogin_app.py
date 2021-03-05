#!/usr/bin/python

from onelogin.api.util.utils import str2int, str2bool
from .base import Base


class OneLoginApp(Base):
    def __init__(self, data):
        self.id = str2int(data.get('id', None))
        self.connector_id = str2int(data.get('connector_id', None))
        self.name = data.get('name', '')
        self.extension = str2bool(data.get('extension', None))
        self.icon = data.get('icon', '')        
        self.visible = str2bool(data.get('visible', None))
        self.provisioning = str2bool(data.get('provisioning', None))
