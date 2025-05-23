
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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class RiskUser(BaseModel):
    """
    An Object containing User details.
    """
    id: StrictStr = Field(..., description="A unique identifier for the user.")
    name: Optional[StrictStr] = Field(None, description="A name for the user.")
    authenticated: Optional[StrictBool] = Field(False, description="Indicates if the metadata supplied in this event should be considered as trusted for the user.")
    __properties = ["id", "name", "authenticated"]

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
    def from_json(cls, json_str: str) -> RiskUser:
        """Create an instance of RiskUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RiskUser:
        """Create an instance of RiskUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RiskUser.parse_obj(obj)

        _obj = RiskUser.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "authenticated": obj.get("authenticated") if obj.get("authenticated") is not None else False
        })
        return _obj

