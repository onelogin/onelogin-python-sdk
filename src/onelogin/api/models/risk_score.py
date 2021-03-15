#!/usr/bin/python

from onelogin.api.util.utils import str2int

from .base import Base


class RiskScore(Base):
    def __init__(self, data):
        self.score = str2int(data.get('score', None))
        self.risk_level = data.get('risk_level', None)
        self.triggers = data.get('triggers', None)
        self.messages = data.get('messages', None)
