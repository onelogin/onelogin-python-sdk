
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

class Scope(BaseModel):
    """
    Scope
    """
    id: Optional[StrictInt] = Field(None, description="Unique Scope ID value")
    value: Optional[StrictStr] = Field(None, description="Scope Value")
    description: Optional[StrictStr] = Field(None, description="Description of the scope")
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
    def from_json(cls, json_str: str) -> Scope:
        """Create an instance of Scope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Scope:
        """Create an instance of Scope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Scope.parse_obj(obj)

        _obj = Scope.parse_obj({
            "id": obj.get("id"),
            "value": obj.get("value"),
            "description": obj.get("description")
        })
        return _obj

