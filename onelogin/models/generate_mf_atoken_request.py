# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt

class GenerateMFAtokenRequest(BaseModel):
    """
    GenerateMFAtokenRequest
    """
    expires_in: Optional[StrictInt] = Field(None, description="Set the duration of the token in seconds. Token expiration defaults to 259200 seconds = 72 hours. 72 hours is the max value.")
    reusable: Optional[StrictBool] = Field(False, description="Defines if the token is reusable multiple times within the expiry window. Value defaults to false. If set to true, token can be used multiple times, until it expires.")
    __properties = ["expires_in", "reusable"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GenerateMFAtokenRequest:
        """Create an instance of GenerateMFAtokenRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GenerateMFAtokenRequest:
        """Create an instance of GenerateMFAtokenRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GenerateMFAtokenRequest.parse_obj(obj)

        _obj = GenerateMFAtokenRequest.parse_obj({
            "expires_in": obj.get("expires_in"),
            "reusable": obj.get("reusable") if obj.get("reusable") is not None else False
        })
        return _obj

