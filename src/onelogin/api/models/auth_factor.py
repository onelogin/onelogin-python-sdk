#!/usr/bin/python

from onelogin.api.util.utils import str2int

from .base import Base


class AuthFactor(Base):
    def __init__(self, data):
        self.id = str2int(data.get('factor_id', None))
        self.name = data.get('name', '')
