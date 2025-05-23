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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, field_validator
from onelogin.models.action_obj import ActionObj
from onelogin.models.condition import Condition

class AppRule(BaseModel):
    """
    AppRule
    """
    id: Optional[StrictInt] = Field(None, description="App Rule ID")
    name: Optional[StrictStr] = Field(None, description="Rule Name")
    match: Optional[StrictStr] = Field(None, description="Indicates how conditions should be matched.")
    enabled: Optional[StrictBool] = Field(None, description="Indicates if the rule is enabled or not.")
    position: Optional[StrictInt] = Field(None, description="Indicates the order of the rule. When `null` this will default to last position.")
    conditions: Optional[conlist(Condition)] = Field(None, description="An array of conditions that the user must meet in order for the rule to be applied.")
    actions: Optional[conlist(ActionObj)] = None
    __properties = ["id", "name", "match", "enabled", "position", "conditions", "actions"]

    @field_validator('match')
    @classmethod
    def match_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('all', 'any'):
            raise ValueError("must be one of enum values ('all', 'any')")
        return value

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
    def from_json(cls, json_str: str) -> AppRule:
        """Create an instance of AppRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AppRule:
        """Create an instance of AppRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AppRule.parse_obj(obj)

        _obj = AppRule.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "match": obj.get("match"),
            "enabled": obj.get("enabled"),
            "position": obj.get("position"),
            "conditions": [Condition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "actions": [ActionObj.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None
        })
        return _obj

