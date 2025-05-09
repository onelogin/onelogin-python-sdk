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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class BrandReq(BaseModel):
    """
    BrandReq
    """
    id: Optional[StrictInt] = Field(None, description="Brand’s unique ID in OneLogin.")
    enabled: Optional[StrictBool] = Field(None, description="Indicates if the brand is enabled or not.")
    name: Optional[StrictStr] = Field(None, description="Brand name for humans. This isn’t related to subdomains.")
    __properties = ["id", "enabled", "name"]

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
    def from_json(cls, json_str: str) -> BrandReq:
        """Create an instance of BrandReq from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BrandReq:
        """Create an instance of BrandReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BrandReq.parse_obj(obj)

        _obj = BrandReq.parse_obj({
            "id": obj.get("id"),
            "enabled": obj.get("enabled"),
            "name": obj.get("name")
        })
        return _obj

