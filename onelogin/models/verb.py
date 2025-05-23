# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Verb(str, Enum):
    """
    Verbs are used to distinguish between different types of events. Where possible use one of the following verbs to describe the event. Alternately you can create custom verbs to describe other types of actions within your application.
    """

    """
    allowed enum values
    """
    LOG_MINUS_IN = 'log-in'
    LOG_MINUS_OUT = 'log-out'
    LOG_MINUS_IN_MINUS_DENIED = 'log-in-denied'
    AUTHENTICATION_MINUS_CHALLENGE = 'authentication-challenge'
    AUTHENTICATION_MINUS_CHALLENGE_MINUS_PASS = 'authentication-challenge-pass'
    AUTHENTICATION_MINUS_CHALLENGE_MINUS_FAIL = 'authentication-challenge-fail'

    @classmethod
    def from_json(cls, json_str: str) -> Verb:
        """Create an instance of Verb from a JSON string"""
        return Verb(json.loads(json_str))


