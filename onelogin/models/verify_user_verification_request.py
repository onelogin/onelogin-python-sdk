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

class VerifyUserVerificationRequest(BaseModel):
    """
    VerifyUserVerificationRequest
    """
    otp: Optional[StrictStr] = Field(None, description="OTP code provided by the device or SMS message sent to user.")
    device_id: Optional[StrictInt] = Field(None, description="ID of the specified device which has been registerd for the given user. Available on Get Devices API call.")
    __properties = ["otp", "device_id"]

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
    def from_json(cls, json_str: str) -> VerifyUserVerificationRequest:
        """Create an instance of VerifyUserVerificationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyUserVerificationRequest:
        """Create an instance of VerifyUserVerificationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VerifyUserVerificationRequest.parse_obj(obj)

        _obj = VerifyUserVerificationRequest.parse_obj({
            "otp": obj.get("otp"),
            "device_id": obj.get("device_id")
        })
        return _obj

