# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class GetAssignedUser200Response(BaseModel):
    """
    GetAssignedUser200Response
    """
    total: Optional[StrictInt] = None
    users: Optional[conlist(StrictInt)] = None
    before_cursor: Optional[StrictInt] = Field(None, alias="beforeCursor")
    previous_link: Optional[StrictStr] = Field(None, alias="previousLink")
    after_cursor: Optional[StrictInt] = Field(None, alias="afterCursor")
    next_link: Optional[StrictStr] = Field(None, alias="nextLink")
    __properties = ["total", "users", "beforeCursor", "previousLink", "afterCursor", "nextLink"]

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
    def from_json(cls, json_str: str) -> GetAssignedUser200Response:
        """Create an instance of GetAssignedUser200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if before_cursor (nullable) is None
        # and __fields_set__ contains the field
        if self.before_cursor is None and "before_cursor" in self.__fields_set__:
            _dict['beforeCursor'] = None

        # set to None if previous_link (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_link is None and "previous_link" in self.__fields_set__:
            _dict['previousLink'] = None

        # set to None if after_cursor (nullable) is None
        # and __fields_set__ contains the field
        if self.after_cursor is None and "after_cursor" in self.__fields_set__:
            _dict['afterCursor'] = None

        # set to None if next_link (nullable) is None
        # and __fields_set__ contains the field
        if self.next_link is None and "next_link" in self.__fields_set__:
            _dict['nextLink'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAssignedUser200Response:
        """Create an instance of GetAssignedUser200Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetAssignedUser200Response.parse_obj(obj)

        _obj = GetAssignedUser200Response.parse_obj({
            "total": obj.get("total"),
            "users": obj.get("users"),
            "before_cursor": obj.get("beforeCursor"),
            "previous_link": obj.get("previousLink"),
            "after_cursor": obj.get("afterCursor"),
            "next_link": obj.get("nextLink")
        })
        return _obj

