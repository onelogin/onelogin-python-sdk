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

class CreateDeviceVerificationRequest(BaseModel):
    """
    CreateDeviceVerificationRequest
    """
    device_id: StrictInt = Field(..., description="Specifies the factor to be verified.")
    display_name: Optional[StrictStr] = Field(None, description="A name for the users device")
    expires_in: Optional[StrictStr] = Field(None, description="Defaults to 120. Valid values are: 120-900 seconds.")
    redirect_to: Optional[StrictStr] = Field(None, description="Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user.")
    custom_message: Optional[StrictStr] = Field(None, description="Only applies to SMS factor. A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters including the OTP code. SMS must already be configured by the user. The following template variables can be included in the message. - {{otp_code}} - The security code. - {{otp_expiry}} - The number of minutes until the one time code expires.")
    __properties = ["device_id", "display_name", "expires_in", "redirect_to", "custom_message"]

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
    def from_json(cls, json_str: str) -> CreateDeviceVerificationRequest:
        """Create an instance of CreateDeviceVerificationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateDeviceVerificationRequest:
        """Create an instance of CreateDeviceVerificationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateDeviceVerificationRequest.parse_obj(obj)

        _obj = CreateDeviceVerificationRequest.parse_obj({
            "device_id": obj.get("device_id"),
            "display_name": obj.get("display_name"),
            "expires_in": obj.get("expires_in"),
            "redirect_to": obj.get("redirect_to"),
            "custom_message": obj.get("custom_message")
        })
        return _obj

