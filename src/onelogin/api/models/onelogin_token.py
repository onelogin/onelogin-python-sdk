#!/usr/bin/python

from dateutil import parser

from .base import Base


class OneLoginToken(Base):
    def __init__(self, data):
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
        self.account_id = data['account_id']
        self.token_type = data['token_type']
        self.created_at = parser.parse(data['created_at'])
        self.expires_in = data['expires_in']
