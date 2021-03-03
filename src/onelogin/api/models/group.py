#!/usr/bin/python


from .base import Base

class Group(Base):
    def __init__(self, data):
        self.id = data.get('id', None)
        self.name = data.get('name', '')
        self.reference = data.get('reference', '')
