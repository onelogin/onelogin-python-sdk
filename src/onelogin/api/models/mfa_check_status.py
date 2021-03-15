#!/usr/bin/python

from onelogin.api.util.utils import str2int

from .base import Base


class MFACheckStatus(Base):
    def __init__(self, data):
        self.id = data.get('id', None)
        self.status = data.get('status', None)
        self.device_id = str2int(data.get('device_id', None))
