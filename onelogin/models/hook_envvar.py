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
from pydantic import BaseModel, Field, StrictStr

class HookEnvvar(BaseModel):
    """
    HookEnvvar
    """
    id: Optional[StrictStr] = Field(None, description="A unique identifier for the Hook Environment Variable")
    name: StrictStr = Field(..., description="The name of the environment variable.")
    created_at: Optional[StrictStr] = Field(None, description="The ISO8601 formatted date that the environment variable was created.")
    updated_at: Optional[StrictStr] = Field(None, description="The ISO8601 formatted date that the environment variable was last updated.")
    value: StrictStr = Field(..., description="The secret value that will be encrypted at rest and injected in applicable hook functions at run time.")
    __properties = ["id", "name", "created_at", "updated_at", "value"]

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
    def from_json(cls, json_str: str) -> HookEnvvar:
        """Create an instance of HookEnvvar from a JSON string"""
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
    def from_dict(cls, obj: dict) -> HookEnvvar:
        """Create an instance of HookEnvvar from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HookEnvvar.parse_obj(obj)

        _obj = HookEnvvar.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "value": obj.get("value")
        })
        return _obj

