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

class HookStatus(BaseModel):
    """
    HookStatus
    """
    name: Optional[StrictStr] = Field(None, description="responses status nam")
    message: Optional[StrictStr] = Field(None, description="your operation was successful")
    __properties = ["name", "message"]

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
    def from_json(cls, json_str: str) -> HookStatus:
        """Create an instance of HookStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HookStatus:
        """Create an instance of HookStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HookStatus.parse_obj(obj)

        _obj = HookStatus.parse_obj({
            "name": obj.get("name"),
            "message": obj.get("message")
        })
        return _obj

