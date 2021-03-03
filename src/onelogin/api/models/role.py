#!/usr/bin/python

from .base import Base


class Role(Base):
    def __init__(self, data):
        self.id = data.get('id', None)
        self.name = data.get('name', '')
