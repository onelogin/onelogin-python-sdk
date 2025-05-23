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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class GetAuthenticationDevices200ResponseInner(BaseModel):
    """
    GetAuthenticationDevices200ResponseInner
    """
    device_id: Optional[StrictStr] = Field(None, description="MFA device identifier.")
    user_display_name: Optional[StrictStr] = Field(None, description="Authentication factor display name assigned by users when they register the device.")
    type_display_name: Optional[StrictStr] = Field(None, description="Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings > Authentication Factors.")
    auth_factor_name: Optional[StrictStr] = Field(None, description="Authentication factor name, as it appears to administrators in OneLogin.")
    default: Optional[StrictBool] = Field(False, description="true = is user’s default MFA device for OneLogin.")
    __properties = ["device_id", "user_display_name", "type_display_name", "auth_factor_name", "default"]

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
    def from_json(cls, json_str: str) -> GetAuthenticationDevices200ResponseInner:
        """Create an instance of GetAuthenticationDevices200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAuthenticationDevices200ResponseInner:
        """Create an instance of GetAuthenticationDevices200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAuthenticationDevices200ResponseInner.parse_obj(obj)

        _obj = GetAuthenticationDevices200ResponseInner.parse_obj({
            "device_id": obj.get("device_id"),
            "user_display_name": obj.get("user_display_name"),
            "type_display_name": obj.get("type_display_name"),
            "auth_factor_name": obj.get("auth_factor_name"),
            "default": obj.get("default") if obj.get("default") is not None else False
        })
        return _obj

