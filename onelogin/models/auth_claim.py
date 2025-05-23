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

class AuthClaim(BaseModel):
    """
    AuthClaim
    """
    name: StrictStr = Field(..., description="The attribute name for the claim when its returned in an Access Token")
    user_attribute_mappings: Optional[StrictStr] = Field(None, description="A user attribute to map values from For custom attributes prefix the name of the attribute with `custom_attribute_`. e.g. To get the value for custom attribute `employee_id` use `custom_attribute_employee_id`.")
    user_attribute_macros: Optional[StrictStr] = Field(None, description="When `user_attribute_mappings` is set to `_macro_` this macro will be used to assign the parameter value.")
    __properties = ["name", "user_attribute_mappings", "user_attribute_macros"]

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
    def from_json(cls, json_str: str) -> AuthClaim:
        """Create an instance of AuthClaim from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthClaim:
        """Create an instance of AuthClaim from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthClaim.parse_obj(obj)

        _obj = AuthClaim.parse_obj({
            "name": obj.get("name"),
            "user_attribute_mappings": obj.get("user_attribute_mappings"),
            "user_attribute_macros": obj.get("user_attribute_macros")
        })
        return _obj

