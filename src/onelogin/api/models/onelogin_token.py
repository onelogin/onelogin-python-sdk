#!/usr/bin/python

from onelogin.api.util.utils import str2int, str2date
from .base import Base


class OneLoginToken(Base):
    def __init__(self, data):
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
        self.account_id = str2int(data.get('account_id',None))
        self.token_type = data['token_type']
        self.created_at = str2date(data.get('created_at', None))
        self.expires_in = str2int(data.get('expires_in',None))
