#!/usr/bin/python

from dateutil import parser

from .base import Base
from .user import User


class SessionTokenInfo(Base):
    def __init__(self, data):
        self.status = data.get('status', '')
        if data['user']:
            self.user = User(data['user'])  # Partial info
        self.return_to_url = data.get('return_to_url', '')
        self.expires_at = parser.parse(data['expires_at'])
        self.session_token = data.get('session_token', '')
