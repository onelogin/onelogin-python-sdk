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
from onelogin.models.auth_method import AuthMethod

class Connector(BaseModel):
    """
    Connector
    """
    id: Optional[StrictInt] = Field(None, description="Connectors unique ID in OneLogin.")
    name: Optional[StrictStr] = Field(None, description="Name of Connector")
    icon_url: Optional[StrictStr] = Field(None, description="A link to the icon's url.")
    auth_method: Optional[AuthMethod] = None
    allows_new_parameters: Optional[StrictBool] = Field(None, description="Indicates if apps created using this connector will be allowed to create custom parameters.")
    __properties = ["id", "name", "icon_url", "auth_method", "allows_new_parameters"]

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
    def from_json(cls, json_str: str) -> Connector:
        """Create an instance of Connector from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Connector:
        """Create an instance of Connector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Connector.parse_obj(obj)

        _obj = Connector.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "icon_url": obj.get("icon_url"),
            "auth_method": obj.get("auth_method"),
            "allows_new_parameters": obj.get("allows_new_parameters")
        })
        return _obj

