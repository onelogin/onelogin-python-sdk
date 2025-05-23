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
from pydantic import BaseModel, Field, StrictStr, conlist

class ActionObj(BaseModel):
    """
    ActionObj
    """
    action: Optional[StrictStr] = Field(None, description="The action to apply")
    value: Optional[conlist(StrictStr)] = Field(None, description="Only applicable to provisioned and set_* actions. Items in the array will be a plain text string or valid value for the selected action.")
    __properties = ["action", "value"]

    
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
    def from_json(cls, json_str: str) -> ActionObj:
        """Create an instance of ActionObj from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActionObj:
        """Create an instance of ActionObj from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActionObj.parse_obj(obj)

        _obj = ActionObj.parse_obj({
            "action": obj.get("action"),
            "value": obj.get("value")
        })
        return _obj

