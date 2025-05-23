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

class Device(BaseModel):
    """
    Device
    """
    device_id: Optional[StrictInt] = Field(None, description="an ID for the device type that must be submitted with the Verify Factor API call.")
    device_type: Optional[StrictStr] = Field(None, description="Lists an available MFA device type, such as OneLogin OTP SMS or Google Authenticator.")
    __properties = ["device_id", "device_type"]

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
    def from_json(cls, json_str: str) -> Device:
        """Create an instance of Device from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Device:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Device.parse_obj(obj)

        _obj = Device.parse_obj({
            "device_id": obj.get("device_id"),
            "device_type": obj.get("device_type")
        })
        return _obj

