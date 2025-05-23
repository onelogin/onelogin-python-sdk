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

class CreateFactorRegistrationRequest(BaseModel):
    """
    CreateFactorRegistrationRequest
    """
    factor_id: StrictInt = Field(..., description="The identifier of the factor to enroll the user with. See Get Available Factors for a list of possible id values.")
    display_name: StrictStr = Field(..., description="A name for the users device")
    expires_in: Optional[StrictStr] = Field(None, description="Defaults to 120. Valid values are: 120-900 seconds.")
    verified: Optional[StrictBool] = Field(None, description="Defaults to false. The following factors support verified = true as part of the initial registration request: OneLogin SMS, OneLogin Voice, OneLogin Email. When using verified = true it is critical that the supported factors have pre-verified values, most likely imported from an existing directory or by the users themselvdes. Factors such as Authenticator and OneLogin Protect do not support verification = true as the user interaction is required to verify the factor.")
    redirect_to: Optional[StrictStr] = Field(None, description="Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user.")
    custom_message: Optional[StrictStr] = Field(None, description="Only applies to SMS factor. A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters including the OTP code. SMS must already be configured by the user. The following template variables can be included in the message. - {{otp_code}} - The security code. - {{otp_expiry}} - The number of minutes until the one time code expires.")
    __properties = ["factor_id", "display_name", "expires_in", "verified", "redirect_to", "custom_message"]

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
    def from_json(cls, json_str: str) -> CreateFactorRegistrationRequest:
        """Create an instance of CreateFactorRegistrationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateFactorRegistrationRequest:
        """Create an instance of CreateFactorRegistrationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateFactorRegistrationRequest.parse_obj(obj)

        _obj = CreateFactorRegistrationRequest.parse_obj({
            "factor_id": obj.get("factor_id"),
            "display_name": obj.get("display_name"),
            "expires_in": obj.get("expires_in"),
            "verified": obj.get("verified"),
            "redirect_to": obj.get("redirect_to"),
            "custom_message": obj.get("custom_message")
        })
        return _obj

