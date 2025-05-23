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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class TokenClaim(BaseModel):
    """
    TokenClaim
    """
    id: Optional[StrictInt] = Field(None, description="The unique ID of the claim.")
    label: Optional[StrictStr] = Field(None, description="The UI label for the claims.")
    user_attribute_mappings: Optional[StrictStr] = Field(None, description="A user attribute to map values from.")
    user_attribute_macros: Optional[StrictStr] = Field(None, description="When `user_attribute_mappings` is set to `_macro_` this macro will be used to assign the claims value.")
    attribute_transformations: Optional[StrictStr] = Field(None, description="The type of transformation to perform on multi valued attributes.")
    skip_if_blank: Optional[StrictBool] = Field(None, description="not used")
    values: Optional[conlist(StrictStr)] = Field(None, description="Relates to Rules/Entitlements. Not supported yet.")
    default_values: Optional[StrictStr] = Field(None, description="Relates to Rules/Entitlements. Not supported yet.")
    provisioned_entitlements: Optional[StrictBool] = Field(None, description="Relates to Rules/Entitlements. Not supported yet.")
    __properties = ["id", "label", "user_attribute_mappings", "user_attribute_macros", "attribute_transformations", "skip_if_blank", "values", "default_values", "provisioned_entitlements"]

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
    def from_json(cls, json_str: str) -> TokenClaim:
        """Create an instance of TokenClaim from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TokenClaim:
        """Create an instance of TokenClaim from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TokenClaim.parse_obj(obj)

        _obj = TokenClaim.parse_obj({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "user_attribute_mappings": obj.get("user_attribute_mappings"),
            "user_attribute_macros": obj.get("user_attribute_macros"),
            "attribute_transformations": obj.get("attribute_transformations"),
            "skip_if_blank": obj.get("skip_if_blank"),
            "values": obj.get("values"),
            "default_values": obj.get("default_values"),
            "provisioned_entitlements": obj.get("provisioned_entitlements")
        })
        return _obj

