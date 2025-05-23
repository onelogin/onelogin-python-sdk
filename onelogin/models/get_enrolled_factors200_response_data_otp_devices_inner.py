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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class GetEnrolledFactors200ResponseDataOtpDevicesInner(BaseModel):
    """
    GetEnrolledFactors200ResponseDataOtpDevicesInner
    """
    active: Optional[StrictBool] = Field(None, description="True = enabled (used successfully for authentication at least once). False = pending (registered but never used).")
    default: Optional[StrictBool] = Field(None, description="True = is user’s default MFA device for OneLogin.")
    state_token: Optional[StrictStr] = Field(None, description="A short lived token that is required to Verify the Factor. This token expires in 120 seconds.")
    auth_factor_name: Optional[StrictStr] = Field(None, description="\"Official\" authentication factor name, as it appears to administrators in OneLogin.")
    phone_number: Optional[StrictStr] = Field(None, description="For OTP codes sent via SMS, the phone number receiving the SMS message.")
    type_display_name: Optional[StrictStr] = Field(None, description="Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings > Authentication Factors.")
    needs_trigger: Optional[StrictBool] = Field(None, description="true: You MUST Activate this Factor to trigger an SMS or Push notification before Verifying the OTP code. false: No Activation required. You can Verify the OTP immediately. MFA factors that provide both push notifications (user accepts notification) and pull code submission (user initiates code submission from device or enters it manually) should appear twice; once with needs_trigger: true and once with needs_trigger: false.")
    user_display_name: Optional[StrictStr] = Field(None, description="Authentication factor display name assigned by users when they enroll the device.")
    id: Optional[StrictInt] = Field(None, description="MFA device identifier.")
    __properties = ["active", "default", "state_token", "auth_factor_name", "phone_number", "type_display_name", "needs_trigger", "user_display_name", "id"]

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
    def from_json(cls, json_str: str) -> GetEnrolledFactors200ResponseDataOtpDevicesInner:
        """Create an instance of GetEnrolledFactors200ResponseDataOtpDevicesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetEnrolledFactors200ResponseDataOtpDevicesInner:
        """Create an instance of GetEnrolledFactors200ResponseDataOtpDevicesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetEnrolledFactors200ResponseDataOtpDevicesInner.parse_obj(obj)

        _obj = GetEnrolledFactors200ResponseDataOtpDevicesInner.parse_obj({
            "active": obj.get("active"),
            "default": obj.get("default"),
            "state_token": obj.get("state_token"),
            "auth_factor_name": obj.get("auth_factor_name"),
            "phone_number": obj.get("phone_number"),
            "type_display_name": obj.get("type_display_name"),
            "needs_trigger": obj.get("needs_trigger"),
            "user_display_name": obj.get("user_display_name"),
            "id": obj.get("id")
        })
        return _obj

