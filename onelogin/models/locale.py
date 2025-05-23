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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class Locale(BaseModel):
    """
    Locale
    """
    language: Optional[StrictStr] = Field(None, description="locale string")
    is_default: Optional[StrictBool] = Field(None, description="indicator if language is default")
    __properties = ["language", "is_default"]

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
    def from_json(cls, json_str: str) -> Locale:
        """Create an instance of Locale from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Locale:
        """Create an instance of Locale from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Locale.parse_obj(obj)

        _obj = Locale.parse_obj({
            "language": obj.get("language"),
            "is_default": obj.get("is_default")
        })
        return _obj

