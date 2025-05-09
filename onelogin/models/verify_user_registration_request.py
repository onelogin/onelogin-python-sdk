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
from pydantic import BaseModel, Field, StrictInt

class VerifyUserRegistrationRequest(BaseModel):
    """
    VerifyUserRegistrationRequest
    """
    otp: Optional[StrictInt] = Field(None, description="One-Time-Password (OTP) that was sent to the user based on the chosen factor. OneLogin SMS and OneLogin Email support this OTP code.")
    __properties = ["otp"]

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
    def from_json(cls, json_str: str) -> VerifyUserRegistrationRequest:
        """Create an instance of VerifyUserRegistrationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyUserRegistrationRequest:
        """Create an instance of VerifyUserRegistrationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VerifyUserRegistrationRequest.parse_obj(obj)

        _obj = VerifyUserRegistrationRequest.parse_obj({
            "otp": obj.get("otp")
        })
        return _obj

