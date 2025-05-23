
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
from pydantic import BaseModel, Field, StrictStr, confloat, conlist

class GetRiskScore200Response(BaseModel):
    """
    GetRiskScore200Response
    """
    score: Optional[confloat(le=100, ge=0, strict=True)] = Field(None, description="A risk score 0 is low risk and 100 is the highest risk level possible.")
    triggers: Optional[conlist(StrictStr)] = Field(None, description="Triggers are indicators of some of the key items that influenced the risk score.")
    __properties = ["score", "triggers"]

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
    def from_json(cls, json_str: str) -> GetRiskScore200Response:
        """Create an instance of GetRiskScore200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRiskScore200Response:
        """Create an instance of GetRiskScore200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRiskScore200Response.parse_obj(obj)

        _obj = GetRiskScore200Response.parse_obj({
            "score": obj.get("score"),
            "triggers": obj.get("triggers")
        })
        return _obj

