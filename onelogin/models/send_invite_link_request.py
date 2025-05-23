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

class SendInviteLinkRequest(BaseModel):
    """
    SendInviteLinkRequest
    """
    email: Optional[StrictStr] = Field(None, description="Set to the user email address to generate an invite link. The value is case sensitive.")
    personal_email: Optional[StrictStr] = Field(None, description="To send an invite email to a different address than the one provided in email, provide it here. The invite link is sent to this address instead.")
    __properties = ["email", "personal_email"]

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
    def from_json(cls, json_str: str) -> SendInviteLinkRequest:
        """Create an instance of SendInviteLinkRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SendInviteLinkRequest:
        """Create an instance of SendInviteLinkRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SendInviteLinkRequest.parse_obj(obj)

        _obj = SendInviteLinkRequest.parse_obj({
            "email": obj.get("email"),
            "personal_email": obj.get("personal_email")
        })
        return _obj

