# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class AuthMethod(int, Enum):
    """
    An ID indicating the type of app:   - 0: Password   - 1: OpenId   - 2: SAML   - 3: API   - 4: Google   - 6: Forms Based App   - 7: WSFED   - 8: OpenId Connect
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3
    NUMBER_4 = 4
    NUMBER_5 = 5
    NUMBER_6 = 6
    NUMBER_7 = 7
    NUMBER_8 = 8

    @classmethod
    def from_json(cls, json_str: str) -> AuthMethod:
        """Create an instance of AuthMethod from a JSON string"""
        return AuthMethod(json.loads(json_str))


