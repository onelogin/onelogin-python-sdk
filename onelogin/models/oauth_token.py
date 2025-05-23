
# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class OauthToken(BaseModel):
    """
    OauthToken
    """
    access_token: Optional[StrictStr] = Field(None, description="Provides the requested access token. You can use this token to call our resource APIs.")
    created_at: Optional[StrictStr] = Field(None, description="Time at which the access token was generated.")
    expires_in: Optional[StrictInt] = Field(None, description="Indicates that the generated access token expires in 36,000 seconds, 600 minutes, or 10 hours. An expired access token cannot be used to make resource API calls, but it can still be used along with its associated refresh token to call the Refresh Tokens v2 API.")
    refresh_token: Optional[StrictStr] = Field(None, description="deprecated No longer in use")
    token_type: Optional[StrictStr] = Field(None, description="Indicates that the generated access token is a bearer token.")
    account_id: Optional[StrictInt] = Field(None, description="Account ID associated with the API credentials used to generate the token.")
    __properties = ["access_token", "created_at", "expires_in", "refresh_token", "token_type", "account_id"]

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
    def from_json(cls, json_str: str) -> OauthToken:
        """Create an instance of OauthToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OauthToken:
        """Create an instance of OauthToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OauthToken.parse_obj(obj)

        _obj = OauthToken.parse_obj({
            "access_token": obj.get("access_token"),
            "created_at": obj.get("created_at"),
            "expires_in": obj.get("expires_in"),
            "refresh_token": obj.get("refresh_token"),
            "token_type": obj.get("token_type"),
            "account_id": obj.get("account_id")
        })
        return _obj

