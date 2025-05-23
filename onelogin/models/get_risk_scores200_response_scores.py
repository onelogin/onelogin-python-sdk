
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
from pydantic import BaseModel, StrictInt

class GetRiskScores200ResponseScores(BaseModel):
    """
    GetRiskScores200ResponseScores
    """
    minimal: Optional[StrictInt] = None
    low: Optional[StrictInt] = None
    medium: Optional[StrictInt] = None
    high: Optional[StrictInt] = None
    very_high: Optional[StrictInt] = None
    __properties = ["minimal", "low", "medium", "high", "very_high"]

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
    def from_json(cls, json_str: str) -> GetRiskScores200ResponseScores:
        """Create an instance of GetRiskScores200ResponseScores from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRiskScores200ResponseScores:
        """Create an instance of GetRiskScores200ResponseScores from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRiskScores200ResponseScores.parse_obj(obj)

        _obj = GetRiskScores200ResponseScores.parse_obj({
            "minimal": obj.get("minimal"),
            "low": obj.get("low"),
            "medium": obj.get("medium"),
            "high": obj.get("high"),
            "very_high": obj.get("very_high")
        })
        return _obj

