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

class GetUserVerification200Response(BaseModel):
    """
    GetUserVerification200Response
    """
    id: Optional[StrictStr] = Field(None, description="registration identifier")
    status: Optional[StrictStr] = Field(None, description="pending = has not been completed. accepted registration has successfully completed, rejected user has denied the MFA attempt or incorrectly provided the OneLogin Voice OTP code.")
    device_id: Optional[StrictStr] = Field(None, description="Device Id to be used with verify factor")
    __properties = ["id", "status", "device_id"]

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
    def from_json(cls, json_str: str) -> GetUserVerification200Response:
        """Create an instance of GetUserVerification200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetUserVerification200Response:
        """Create an instance of GetUserVerification200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetUserVerification200Response.parse_obj(obj)

        _obj = GetUserVerification200Response.parse_obj({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "device_id": obj.get("device_id")
        })
        return _obj

