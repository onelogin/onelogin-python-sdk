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

class SamlFactor(BaseModel):
    """
    SamlFactor
    """
    app_id: StrictStr = Field(..., description="App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin.")
    device_id: StrictStr = Field(..., description="Provide the MFA device_id you are submitting for verification. The device_id is supplied by the Generate SAML Assertion API.")
    state_token: StrictStr = Field(..., description="Provide the state_token associated with the MFA device_id you are submitting for verification. The state_token is supplied by the Generate SAML Assertion API.")
    otp_token: Optional[StrictStr] = Field(None, description="Provide the OTP value for the MFA factor you are submitting for verification. For some MFA factors; such as OneLogin OTP SMS, which requires the user to request an OTP; the otp_token value is not required, and if not included, returns a 200 OK - Pending result. You’ll make a subsequent Verify Factor API call to provide the otp_token value once it has been provided to the user.")
    do_not_notify: Optional[StrictBool] = Field(None, description="When verifying MFA via Protect Push, set this to true to stop additional push notifications being sent to the OneLogin Protect device.")
    __properties = ["app_id", "device_id", "state_token", "otp_token", "do_not_notify"]

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
    def from_json(cls, json_str: str) -> SamlFactor:
        """Create an instance of SamlFactor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SamlFactor:
        """Create an instance of SamlFactor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SamlFactor.parse_obj(obj)

        _obj = SamlFactor.parse_obj({
            "app_id": obj.get("app_id"),
            "device_id": obj.get("device_id"),
            "state_token": obj.get("state_token"),
            "otp_token": obj.get("otp_token"),
            "do_not_notify": obj.get("do_not_notify")
        })
        return _obj

