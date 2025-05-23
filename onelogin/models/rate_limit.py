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

class RateLimit(BaseModel):
    """
    RateLimit
    """
    x_rate_limit_limit: Optional[StrictInt] = Field(None, alias="X-RateLimit-Limit", description="Rate Limit Limit")
    x_rate_limit_remaining: Optional[StrictInt] = Field(None, alias="X-RateLimit-Remaining", description="Rate Limit Remaining")
    x_rate_limit_reset: Optional[StrictInt] = Field(None, alias="X-RateLimit-Reset", description="Rate Limit Reset")
    __properties = ["X-RateLimit-Limit", "X-RateLimit-Remaining", "X-RateLimit-Reset"]

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
    def from_json(cls, json_str: str) -> RateLimit:
        """Create an instance of RateLimit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RateLimit:
        """Create an instance of RateLimit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RateLimit.parse_obj(obj)

        _obj = RateLimit.parse_obj({
            "x_rate_limit_limit": obj.get("X-RateLimit-Limit"),
            "x_rate_limit_remaining": obj.get("X-RateLimit-Remaining"),
            "x_rate_limit_reset": obj.get("X-RateLimit-Reset")
        })
        return _obj

