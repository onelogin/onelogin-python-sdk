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
from pydantic import BaseModel, Field, StrictInt, conlist

class AddClientAppRequest(BaseModel):
    """
    AddClientAppRequest
    """
    app_id: Optional[StrictInt] = Field(None, description="The ID of the OpenId Connect app to allow access through.")
    scopes: Optional[conlist(StrictInt)] = Field(None, description="An array of Scope IDs that represent scopes the app can request")
    __properties = ["app_id", "scopes"]

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
    def from_json(cls, json_str: str) -> AddClientAppRequest:
        """Create an instance of AddClientAppRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddClientAppRequest:
        """Create an instance of AddClientAppRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddClientAppRequest.parse_obj(obj)

        _obj = AddClientAppRequest.parse_obj({
            "app_id": obj.get("app_id"),
            "scopes": obj.get("scopes")
        })
        return _obj

