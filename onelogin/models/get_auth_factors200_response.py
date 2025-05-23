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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class GetAuthFactors200Response(BaseModel):
    """
    GetAuthFactors200Response
    """
    factor_id: Optional[StrictInt] = Field(None, description="Identifier for the factor which will be used for user enrollment")
    name: Optional[StrictStr] = Field(None, description="Authentication factor name, as it appears to administrators in OneLogin.")
    auth_factor_name: Optional[StrictStr] = Field(None, description="Internal use only")
    __properties = ["factor_id", "name", "auth_factor_name"]

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
    def from_json(cls, json_str: str) -> GetAuthFactors200Response:
        """Create an instance of GetAuthFactors200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAuthFactors200Response:
        """Create an instance of GetAuthFactors200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAuthFactors200Response.parse_obj(obj)

        _obj = GetAuthFactors200Response.parse_obj({
            "factor_id": obj.get("factor_id"),
            "name": obj.get("name"),
            "auth_factor_name": obj.get("auth_factor_name")
        })
        return _obj

