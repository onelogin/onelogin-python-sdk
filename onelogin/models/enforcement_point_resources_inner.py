# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, ClassVar, List
from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator

class EnforcementPointResourcesInner(BaseModel):
    """
    EnforcementPointResourcesInner
    """
    path: Optional[StrictStr] = None
    is_path_regex: Optional[StrictBool] = None
    require_auth: Optional[StrictBool] = None
    permission: Optional[StrictStr] = None
    conditions: Optional[StrictStr] = Field(None, description="required if permission == \"conditions\"")
    
    # Define properties as a class variable
    _properties: ClassVar[List[str]] = ["path", "is_path_regex", "require_auth", "permission", "conditions"]

    @field_validator('permission')
    @classmethod
    def permission_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('allow', 'deny', 'conditions'):
            raise ValueError("must be one of enum values ('allow', 'deny', 'conditions')")
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
    def from_json(cls, json_str: str) -> EnforcementPointResourcesInner:
        """Create an instance of EnforcementPointResourcesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if is_path_regex (nullable) is None
        # and __fields_set__ contains the field
        if self.is_path_regex is None and "is_path_regex" in self.__fields_set__:
            _dict['is_path_regex'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnforcementPointResourcesInner:
        """Create an instance of EnforcementPointResourcesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnforcementPointResourcesInner.parse_obj(obj)

        _obj = EnforcementPointResourcesInner.parse_obj({
            "path": obj.get("path"),
            "is_path_regex": obj.get("is_path_regex"),
            "require_auth": obj.get("require_auth"),
            "permission": obj.get("permission"),
            "conditions": obj.get("conditions")
        })
        return _obj

