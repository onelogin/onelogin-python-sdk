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
from pydantic import BaseModel, Field, StrictStr

class GetInviteLinkRequest(BaseModel):
    """
    GetInviteLinkRequest
    """
    email: Optional[StrictStr] = Field(None, description="Set to the user email address to generate an invite link. The value is case sensitive.")
    __properties = ["email"]

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
    def from_json(cls, json_str: str) -> GetInviteLinkRequest:
        """Create an instance of GetInviteLinkRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetInviteLinkRequest:
        """Create an instance of GetInviteLinkRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetInviteLinkRequest.parse_obj(obj)

        _obj = GetInviteLinkRequest.parse_obj({
            "email": obj.get("email")
        })
        return _obj

