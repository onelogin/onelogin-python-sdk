#!/usr/bin/python

from .base import Base

class AuthFactor(Base):
    def __init__(self, data):
        self.name = data.get('name', '')
        self.id = data.get('factor_id', None)
