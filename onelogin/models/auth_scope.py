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

class AuthScope(BaseModel):
    """
    AuthScope
    """
    id: Optional[StrictInt] = Field(None, description="Unique ID for the Scope")
    value: Optional[StrictStr] = Field(None, description="A value representing the api scope that with be authorized")
    description: Optional[StrictStr] = Field(None, description="A description of what access the scope enables")
    __properties = ["id", "value", "description"]

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
    def from_json(cls, json_str: str) -> AuthScope:
        """Create an instance of AuthScope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthScope:
        """Create an instance of AuthScope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthScope.parse_obj(obj)

        _obj = AuthScope.parse_obj({
            "id": obj.get("id"),
            "value": obj.get("value"),
            "description": obj.get("description")
        })
        return _obj

