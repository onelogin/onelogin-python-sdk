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
from pydantic import BaseModel, conlist
from onelogin.models.error import Error
from onelogin.models.get_role_by_id200_response_data_inner import GetRoleById200ResponseDataInner

class GetRoleById200Response(BaseModel):
    """
    GetRoleById200Response
    """
    status: Optional[Error] = None
    data: Optional[conlist(GetRoleById200ResponseDataInner)] = None
    __properties = ["status", "data"]

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
    def from_json(cls, json_str: str) -> GetRoleById200Response:
        """Create an instance of GetRoleById200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRoleById200Response:
        """Create an instance of GetRoleById200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRoleById200Response.parse_obj(obj)

        _obj = GetRoleById200Response.parse_obj({
            "status": Error.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "data": [GetRoleById200ResponseDataInner.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None
        })
        return _obj

