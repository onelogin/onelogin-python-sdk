# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class AuthServerConfiguration(BaseModel):
    """
    Authorization server configuration
    """
    audiences: conlist(StrictStr) = Field(..., description="List of API endpoints that will be returned in Access Tokens.")
    refresh_token_expiration_minutes: Optional[StrictInt] = Field(None, description="The number of minutes until refresh token expires. There is no maximum expiry limit.")
    resource_identifier: StrictStr = Field(..., description="Unique identifier for the API that the Authorization Server will issue Access Tokens for.")
    access_token_expiration_minutes: Optional[StrictInt] = Field(None, description="The number of minutes until access token expires. There is no maximum expiry limit.")
    __properties = ["audiences", "refresh_token_expiration_minutes", "resource_identifier", "access_token_expiration_minutes"]

    """Pydantic configuration"""
    model_config = {
        "validate_by_name": True,
        "validate_by_alias": True,
        "validate_assignment": True
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AuthServerConfiguration:
        """Create an instance of AuthServerConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthServerConfiguration:
        """Create an instance of AuthServerConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthServerConfiguration.parse_obj(obj)

        _obj = AuthServerConfiguration.parse_obj({
            "audiences": obj.get("audiences"),
            "refresh_token_expiration_minutes": obj.get("refresh_token_expiration_minutes"),
            "resource_identifier": obj.get("resource_identifier"),
            "access_token_expiration_minutes": obj.get("access_token_expiration_minutes")
        })
        return _obj

