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
from pydantic import BaseModel, StrictInt

class AddClientApp201Response(BaseModel):
    """
    AddClientApp201Response
    """
    app_id: Optional[StrictInt] = None
    api_auth_id: Optional[StrictInt] = None
    __properties = ["app_id", "api_auth_id"]

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
    def from_json(cls, json_str: str) -> AddClientApp201Response:
        """Create an instance of AddClientApp201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddClientApp201Response:
        """Create an instance of AddClientApp201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddClientApp201Response.parse_obj(obj)

        _obj = AddClientApp201Response.parse_obj({
            "app_id": obj.get("app_id"),
            "api_auth_id": obj.get("api_auth_id")
        })
        return _obj

