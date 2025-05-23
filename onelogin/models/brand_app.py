# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, StrictBool, StrictInt, StrictStr

class BrandApp(BaseModel):
    """
    BrandApp
    """
    id: StrictInt = ...
    updated_at: StrictStr = ...
    name: StrictStr = ...
    connector_id: StrictInt = ...
    auth_method_description: StrictStr = ...
    description: StrictStr = ...
    auth_method: StrictInt = ...
    created_at: StrictStr = ...
    visible: StrictBool = ...
    __properties = ["id", "updated_at", "name", "connector_id", "auth_method_description", "description", "auth_method", "created_at", "visible"]

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
    def from_json(cls, json_str: str) -> BrandApp:
        """Create an instance of BrandApp from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BrandApp:
        """Create an instance of BrandApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BrandApp.parse_obj(obj)

        _obj = BrandApp.parse_obj({
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "name": obj.get("name"),
            "connector_id": obj.get("connector_id"),
            "auth_method_description": obj.get("auth_method_description"),
            "description": obj.get("description"),
            "auth_method": obj.get("auth_method"),
            "created_at": obj.get("created_at"),
            "visible": obj.get("visible")
        })
        return _obj

