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
from pydantic import BaseModel, Field, StrictStr, conlist
from onelogin.models.privilege_privilege_statement_inner import PrivilegePrivilegeStatementInner

class PrivilegePrivilege(BaseModel):
    """
    PrivilegePrivilege
    """
    version: Optional[StrictStr] = Field(None, alias="Version")
    statement: Optional[conlist(PrivilegePrivilegeStatementInner)] = Field(None, alias="Statement")
    __properties = ["Version", "Statement"]

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
    def from_json(cls, json_str: str) -> PrivilegePrivilege:
        """Create an instance of PrivilegePrivilege from a JSON string"""
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
    def from_dict(cls, obj: dict) -> PrivilegePrivilege:
        """Create an instance of PrivilegePrivilege from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrivilegePrivilege.parse_obj(obj)

        _obj = PrivilegePrivilege.parse_obj({
            "version": obj.get("Version"),
            "statement": [PrivilegePrivilegeStatementInner.from_dict(_item) for _item in obj.get("Statement")] if obj.get("Statement") is not None else None
        })
        return _obj

