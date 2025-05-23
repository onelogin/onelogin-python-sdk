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

class ActivateMfaFactorsRequest(BaseModel):
    """
    ActivateMfaFactorsRequest
    """
    state_token_expires_in: Optional[StrictInt] = Field(None, description="Optional. Sets the window of time in seconds that the factor must be verified within. Defaults to 120 seconds (2 minutes). Max 900 seconds (15 minutes).")
    numeric_sms_otp: Optional[StrictBool] = Field(None, description="Optional. Defaults to false. Only applies to SMS factor. When set to `true` a 6 digit numeric code will be sent to the user instead of the standard code which is alphanumeric.")
    sms_message: Optional[StrictStr] = Field(None, description="Optional. Only applies to SMS factor. A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters. The following template variables can be included in the message. - {{otp_code}} - The security code. - {{expiration}} - The number of minutes until the one time code expires.")
    __properties = ["state_token_expires_in", "numeric_sms_otp", "sms_message"]

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
    def from_json(cls, json_str: str) -> ActivateMfaFactorsRequest:
        """Create an instance of ActivateMfaFactorsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActivateMfaFactorsRequest:
        """Create an instance of ActivateMfaFactorsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActivateMfaFactorsRequest.parse_obj(obj)

        _obj = ActivateMfaFactorsRequest.parse_obj({
            "state_token_expires_in": obj.get("state_token_expires_in"),
            "numeric_sms_otp": obj.get("numeric_sms_otp"),
            "sms_message": obj.get("sms_message")
        })
        return _obj

