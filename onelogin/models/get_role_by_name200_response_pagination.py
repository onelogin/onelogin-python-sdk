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
from pydantic import BaseModel, StrictStr

class GetRoleByName200ResponsePagination(BaseModel):
    """
    GetRoleByName200ResponsePagination
    """
    after_cursor: Optional[StrictStr] = None
    before_cursor: Optional[StrictStr] = None
    next_link: Optional[StrictStr] = None
    previous_link: Optional[StrictStr] = None
    __properties = ["after_cursor", "before_cursor", "next_link", "previous_link"]

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
    def from_json(cls, json_str: str) -> GetRoleByName200ResponsePagination:
        """Create an instance of GetRoleByName200ResponsePagination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRoleByName200ResponsePagination:
        """Create an instance of GetRoleByName200ResponsePagination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRoleByName200ResponsePagination.parse_obj(obj)

        _obj = GetRoleByName200ResponsePagination.parse_obj({
            "after_cursor": obj.get("after_cursor"),
            "before_cursor": obj.get("before_cursor"),
            "next_link": obj.get("next_link"),
            "previous_link": obj.get("previous_link")
        })
        return _obj

