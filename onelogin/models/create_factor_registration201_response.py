# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class CreateFactorRegistration201Response(BaseModel):
    """
    CreateFactorRegistration201Response
    """
    device_id: Optional[StrictStr] = Field(None, description="MFA device identifier.")
    user_display_name: Optional[StrictStr] = Field(None, description="Authentication factor display name assigned by users when they register the device.")
    type_display_name: Optional[StrictStr] = Field(None, description="Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings > Authentication Factors.")
    auth_factor_name: Optional[StrictStr] = Field(None, description="Authentication factor name, as it appears to administrators in OneLogin.")
    id: Optional[StrictStr] = Field(None, description="Verification identifier used in subsequent verification step.")
    user_id: Optional[StrictStr] = Field(None, description="User identifier")
    __properties = ["device_id", "user_display_name", "type_display_name", "auth_factor_name", "id", "user_id"]

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
    def from_json(cls, json_str: str) -> CreateFactorRegistration201Response:
        """Create an instance of CreateFactorRegistration201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateFactorRegistration201Response:
        """Create an instance of CreateFactorRegistration201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateFactorRegistration201Response.parse_obj(obj)

        _obj = CreateFactorRegistration201Response.parse_obj({
            "device_id": obj.get("device_id"),
            "user_display_name": obj.get("user_display_name"),
            "type_display_name": obj.get("type_display_name"),
            "auth_factor_name": obj.get("auth_factor_name"),
            "id": obj.get("id"),
            "user_id": obj.get("user_id")
        })
        return _obj

