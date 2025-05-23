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

class GetMFAFactors200ResponseDataAuthFactorsInner(BaseModel):
    """
    GetMFAFactors200ResponseDataAuthFactorsInner
    """
    name: Optional[StrictStr] = Field(None, description="Official authentication factor name, as it appears to administrators in OneLogin.")
    factor_id: Optional[StrictInt] = Field(None, description="Identifier for the factor which will be used for user enrollment")
    __properties = ["name", "factor_id"]

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
    def from_json(cls, json_str: str) -> GetMFAFactors200ResponseDataAuthFactorsInner:
        """Create an instance of GetMFAFactors200ResponseDataAuthFactorsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetMFAFactors200ResponseDataAuthFactorsInner:
        """Create an instance of GetMFAFactors200ResponseDataAuthFactorsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetMFAFactors200ResponseDataAuthFactorsInner.parse_obj(obj)

        _obj = GetMFAFactors200ResponseDataAuthFactorsInner.parse_obj({
            "name": obj.get("name"),
            "factor_id": obj.get("factor_id")
        })
        return _obj

