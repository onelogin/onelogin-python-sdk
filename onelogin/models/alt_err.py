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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class AltErr(BaseModel):
    """
    AltErr
    """
    status_code: Optional[StrictInt] = Field(None, alias="statusCode", description="HTTP error code https://developer.mozilla.org/en-US/docs/Web/HTTP/Status")
    name: Optional[StrictStr] = Field(None, description="Error Code Name")
    message: Optional[StrictStr] = Field(None, description="Description of Error")
    __properties = ["statusCode", "name", "message"]

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
    def from_json(cls, json_str: str) -> AltErr:
        """Create an instance of AltErr from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AltErr:
        """Create an instance of AltErr from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AltErr.parse_obj(obj)

        _obj = AltErr.parse_obj({
            "status_code": obj.get("statusCode"),
            "name": obj.get("name"),
            "message": obj.get("message")
        })
        return _obj

