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
from pydantic import BaseModel, StrictBool

class HookOptions(BaseModel):
    """
    A set of attributes allow control over the information that is included in the hook context.
    """
    risk_enabled: Optional[StrictBool] = None
    location_enabled: Optional[StrictBool] = None
    mfa_device_info_enabled: Optional[StrictBool] = None
    __properties = ["risk_enabled", "location_enabled", "mfa_device_info_enabled"]

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
    def from_json(cls, json_str: str) -> HookOptions:
        """Create an instance of HookOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HookOptions:
        """Create an instance of HookOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HookOptions.parse_obj(obj)

        _obj = HookOptions.parse_obj({
            "risk_enabled": obj.get("risk_enabled"),
            "location_enabled": obj.get("location_enabled"),
            "mfa_device_info_enabled": obj.get("mfa_device_info_enabled")
        })
        return _obj

