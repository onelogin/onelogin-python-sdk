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

class OtpDevice(BaseModel):
    """
    OtpDevice
    """
    factor_id: StrictInt = Field(..., description="The identifier of the factor to enroll the user with.")
    display_name: StrictStr = Field(..., description="A name for the users device")
    number: StrictStr = Field(..., description="The phone number of the user in E.164 format.")
    verified: Optional[StrictBool] = Field(None, description="Defaults to false. Some factors like SMS or Voice require that a user recieve a token and then that token is supplied to the Verify endpoint before the device is considered active. You can set verfied to `true` which indicates the the users phone number is pre verified and the device can be immediately activated.           ")
    __properties = ["factor_id", "display_name", "number", "verified"]

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
    def from_json(cls, json_str: str) -> OtpDevice:
        """Create an instance of OtpDevice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "factor_id",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OtpDevice:
        """Create an instance of OtpDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OtpDevice.parse_obj(obj)

        _obj = OtpDevice.parse_obj({
            "factor_id": obj.get("factor_id"),
            "display_name": obj.get("display_name"),
            "number": obj.get("number"),
            "verified": obj.get("verified")
        })
        return _obj

