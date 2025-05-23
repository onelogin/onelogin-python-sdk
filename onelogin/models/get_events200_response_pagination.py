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

class GetEvents200ResponsePagination(BaseModel):
    """
    GetEvents200ResponsePagination
    """
    before_cursor: Optional[StrictStr] = None
    after_cursor: Optional[StrictStr] = None
    previous_link: Optional[StrictStr] = None
    next_link: Optional[StrictStr] = None
    __properties = ["before_cursor", "after_cursor", "previous_link", "next_link"]

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
    def from_json(cls, json_str: str) -> GetEvents200ResponsePagination:
        """Create an instance of GetEvents200ResponsePagination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetEvents200ResponsePagination:
        """Create an instance of GetEvents200ResponsePagination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetEvents200ResponsePagination.parse_obj(obj)

        _obj = GetEvents200ResponsePagination.parse_obj({
            "before_cursor": obj.get("before_cursor"),
            "after_cursor": obj.get("after_cursor"),
            "previous_link": obj.get("previous_link"),
            "next_link": obj.get("next_link")
        })
        return _obj

