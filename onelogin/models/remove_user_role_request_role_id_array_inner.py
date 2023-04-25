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


from typing import Optional
from pydantic import BaseModel, StrictInt

class RemoveUserRoleRequestRoleIdArrayInner(BaseModel):
    """
    RemoveUserRoleRequestRoleIdArrayInner
    """
    role_id: Optional[StrictInt] = None
    __properties = ["role_id"]

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
    def from_json(cls, json_str: str) -> RemoveUserRoleRequestRoleIdArrayInner:
        """Create an instance of RemoveUserRoleRequestRoleIdArrayInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RemoveUserRoleRequestRoleIdArrayInner:
        """Create an instance of RemoveUserRoleRequestRoleIdArrayInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RemoveUserRoleRequestRoleIdArrayInner.parse_obj(obj)

        _obj = RemoveUserRoleRequestRoleIdArrayInner.parse_obj({
            "role_id": obj.get("role_id")
        })
        return _obj

