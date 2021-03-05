#!/usr/bin/python

from onelogin.api.util.utils import str2int

from .base import Base


class AssignedBase(Base):

    def __init__(self, data):
        self.id = str2int(data.get('id', None))
        self.name = data.get('name', None)
        self.email = data.get('email', None)
        self.username = data.get('username', None)
        self.assigned = data.get('assigned', None)
        self.added_by = data.get('added_by', None)

    def get_added_by():
        return self.added_by
