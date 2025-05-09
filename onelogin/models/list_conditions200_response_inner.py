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

class ListConditions200ResponseInner(BaseModel):
    """
    ListConditions200ResponseInner
    """
    name: Optional[StrictStr] = Field(None, description="Name of the rule condition")
    value: Optional[StrictStr] = Field(None, description="The unique identifier of the condition. This should be used when defining conditions for a rule.")
    __properties = ["name", "value"]

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
    def from_json(cls, json_str: str) -> ListConditions200ResponseInner:
        """Create an instance of ListConditions200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListConditions200ResponseInner:
        """Create an instance of ListConditions200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListConditions200ResponseInner.parse_obj(obj)

        _obj = ListConditions200ResponseInner.parse_obj({
            "name": obj.get("name"),
            "value": obj.get("value")
        })
        return _obj

