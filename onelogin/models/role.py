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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class Role(BaseModel):
    """
    Role
    """
    id: Optional[StrictInt] = Field(None, description="Role ID")
    name: StrictStr = Field(..., description="The name of the role.")
    apps: Optional[conlist(StrictInt)] = Field(None, description="A list of app IDs that will be assigned to the role.")
    users: Optional[conlist(StrictInt)] = Field(None, description="A list of user IDs to assign to the role.")
    admins: Optional[conlist(StrictInt)] = Field(None, description="A list of user IDs to assign as role administrators.")
    __properties = ["id", "name", "apps", "users", "admins"]

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
    def from_json(cls, json_str: str) -> Role:
        """Create an instance of Role from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Role:
        """Create an instance of Role from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Role.parse_obj(obj)

        _obj = Role.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "apps": obj.get("apps"),
            "users": obj.get("users"),
            "admins": obj.get("admins")
        })
        return _obj

