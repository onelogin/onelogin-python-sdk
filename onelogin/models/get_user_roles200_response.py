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
from onelogin.models.error import Error

class GetUserRoles200Response(BaseModel):
    """
    GetUserRoles200Response
    """
    status: Optional[Error] = None
    data: Optional[conlist(StrictInt)] = Field(None, description="List of Role IDs that are assigned to the User")
    __properties = ["status", "data"]

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
    def from_json(cls, json_str: str) -> GetUserRoles200Response:
        """Create an instance of GetUserRoles200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetUserRoles200Response:
        """Create an instance of GetUserRoles200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetUserRoles200Response.parse_obj(obj)

        _obj = GetUserRoles200Response.parse_obj({
            "status": Error.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "data": obj.get("data")
        })
        return _obj

