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

class GetRoleApps200ResponseInner(BaseModel):
    """
    GetRoleApps200ResponseInner
    """
    id: Optional[StrictInt] = Field(None, description="app id")
    name: Optional[StrictStr] = Field(None, description="app name")
    icon_url: Optional[StrictStr] = Field(None, description="url of Icon")
    __properties = ["id", "name", "icon_url"]

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
    def from_json(cls, json_str: str) -> GetRoleApps200ResponseInner:
        """Create an instance of GetRoleApps200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRoleApps200ResponseInner:
        """Create an instance of GetRoleApps200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRoleApps200ResponseInner.parse_obj(obj)

        _obj = GetRoleApps200ResponseInner.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "icon_url": obj.get("icon_url")
        })
        return _obj

