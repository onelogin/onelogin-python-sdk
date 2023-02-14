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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class ListClientApps200ResponseScopesInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[StrictInt] = Field(None, description="Unique Scope ID value")
    value: Optional[StrictStr] = Field(None, description="Scope Value")
    description: Optional[StrictStr] = Field(None, description="Description of the scope")
    __properties = ["id", "value", "description"]

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
    def from_json(cls, json_str: str) -> ListClientApps200ResponseScopesInner:
        """Create an instance of ListClientApps200ResponseScopesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListClientApps200ResponseScopesInner:
        """Create an instance of ListClientApps200ResponseScopesInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ListClientApps200ResponseScopesInner.parse_obj(obj)

        _obj = ListClientApps200ResponseScopesInner.parse_obj({
            "id": obj.get("id"),
            "value": obj.get("value"),
            "description": obj.get("description")
        })
        return _obj

