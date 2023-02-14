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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.list_priveleges200_response_inner_privilege_statement_inner import ListPriveleges200ResponseInnerPrivilegeStatementInner

class ListPriveleges200ResponseInnerPrivilege(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    version: Optional[StrictStr] = Field(None, alias="Version")
    statement: Optional[List[ListPriveleges200ResponseInnerPrivilegeStatementInner]] = Field(None, alias="Statement")
    __properties = ["Version", "Statement"]

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
    def from_json(cls, json_str: str) -> ListPriveleges200ResponseInnerPrivilege:
        """Create an instance of ListPriveleges200ResponseInnerPrivilege from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in statement (list)
        _items = []
        if self.statement:
            for _item in self.statement:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Statement'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListPriveleges200ResponseInnerPrivilege:
        """Create an instance of ListPriveleges200ResponseInnerPrivilege from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ListPriveleges200ResponseInnerPrivilege.parse_obj(obj)

        _obj = ListPriveleges200ResponseInnerPrivilege.parse_obj({
            "version": obj.get("Version"),
            "statement": [ListPriveleges200ResponseInnerPrivilegeStatementInner.from_dict(_item) for _item in obj.get("Statement")] if obj.get("Statement") is not None else None
        })
        return _obj

