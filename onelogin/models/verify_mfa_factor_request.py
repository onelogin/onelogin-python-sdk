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

class VerifyMfaFactorRequest(BaseModel):
    """
    VerifyMfaFactorRequest
    """
    state_token: Optional[StrictStr] = Field(None, description="The state_token is returned after a successful request to Enroll a Factor or Activate a Factor. The state_token MUST be provided if the needs_trigger attribute from the proceeding calls is set to true. Note that the state_token expires 120 seconds after creation. If the token is expired you will need to Activate the Factor again.")
    otp_token: Optional[StrictStr] = Field(None, description="OTP code provided by the device or SMS message sent to user. When a device like OneLogin Protect that supports Push has been used you do not need to provide the otp_token and can keep polling this endpoint until the state_token expires.")
    __properties = ["state_token", "otp_token"]

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
    def from_json(cls, json_str: str) -> VerifyMfaFactorRequest:
        """Create an instance of VerifyMfaFactorRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyMfaFactorRequest:
        """Create an instance of VerifyMfaFactorRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VerifyMfaFactorRequest.parse_obj(obj)

        _obj = VerifyMfaFactorRequest.parse_obj({
            "state_token": obj.get("state_token"),
            "otp_token": obj.get("otp_token")
        })
        return _obj

