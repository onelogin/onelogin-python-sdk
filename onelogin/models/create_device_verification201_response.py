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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class CreateDeviceVerification201Response(BaseModel):
    """
    CreateDeviceVerification201Response
    """
    device_id: Optional[StrictInt] = Field(None, description="Specifies the factor to be verified.")
    display_name: Optional[StrictStr] = Field(None, description="A name for the users device")
    expires_at: Optional[StrictStr] = Field(None, description="A short lived token that is required to Verify the Factor. This token expires based on the expires_in parameter passed in.")
    redirect_to: Optional[StrictStr] = Field(None, description="Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user.")
    user_display_name: Optional[StrictStr] = Field(None, description="Authentication factor display name assigned by users when they register the device.")
    id: Optional[StrictStr] = Field(None, description="Registration identifier.")
    type_display_name: Optional[StrictStr] = Field(None, description="Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings > Authentication Factors.")
    auth_factor_name: Optional[StrictStr] = Field(None, description="Authentication factor name, as it appears to administrators in OneLogin.")
    __properties = ["device_id", "display_name", "expires_at", "redirect_to", "user_display_name", "id", "type_display_name", "auth_factor_name"]

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
    def from_json(cls, json_str: str) -> CreateDeviceVerification201Response:
        """Create an instance of CreateDeviceVerification201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateDeviceVerification201Response:
        """Create an instance of CreateDeviceVerification201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateDeviceVerification201Response.parse_obj(obj)

        _obj = CreateDeviceVerification201Response.parse_obj({
            "device_id": obj.get("device_id"),
            "display_name": obj.get("display_name"),
            "expires_at": obj.get("expires_at"),
            "redirect_to": obj.get("redirect_to"),
            "user_display_name": obj.get("user_display_name"),
            "id": obj.get("id"),
            "type_display_name": obj.get("type_display_name"),
            "auth_factor_name": obj.get("auth_factor_name")
        })
        return _obj

