# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt

class GetRateLimit200ResponseData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    x_rate_limit_limit: Optional[StrictInt] = Field(None, alias="X-RateLimit-Limit", description="Rate Limit Limit")
    x_rate_limit_remaining: Optional[StrictInt] = Field(None, alias="X-RateLimit-Remaining", description="Rate Limit Remaining")
    x_rate_limit_reset: Optional[StrictInt] = Field(None, alias="X-RateLimit-Reset", description="Rate Limit Reset")
    __properties = ["X-RateLimit-Limit", "X-RateLimit-Remaining", "X-RateLimit-Reset"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetRateLimit200ResponseData:
        """Create an instance of GetRateLimit200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRateLimit200ResponseData:
        """Create an instance of GetRateLimit200ResponseData from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetRateLimit200ResponseData.parse_obj(obj)

        _obj = GetRateLimit200ResponseData.parse_obj({
            "x_rate_limit_limit": obj.get("X-RateLimit-Limit"),
            "x_rate_limit_remaining": obj.get("X-RateLimit-Remaining"),
            "x_rate_limit_reset": obj.get("X-RateLimit-Reset")
        })
        return _obj

