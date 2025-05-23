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

class UpdatePasswordInsecureRequest(BaseModel):
    """
    UpdatePasswordInsecureRequest
    """
    password: StrictStr = Field(..., description="Set to the password value using cleartext. Hashes are never stored as cleartext. They are stored securely using cryptographic hash. OneLogin continuously upgrades the strength of the hash. Ensure that the value meets the password strength requirements set for the account.")
    password_confirmation: StrictStr = Field(..., description="Ensure that this value matches the password value exactly.")
    validate_policy: Optional[StrictBool] = Field(False, description="Will passwords validate against the User Policy. Defaults to false.")
    __properties = ["password", "password_confirmation", "validate_policy"]

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
    def from_json(cls, json_str: str) -> UpdatePasswordInsecureRequest:
        """Create an instance of UpdatePasswordInsecureRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdatePasswordInsecureRequest:
        """Create an instance of UpdatePasswordInsecureRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdatePasswordInsecureRequest.parse_obj(obj)

        _obj = UpdatePasswordInsecureRequest.parse_obj({
            "password": obj.get("password"),
            "password_confirmation": obj.get("password_confirmation"),
            "validate_policy": obj.get("validate_policy") if obj.get("validate_policy") is not None else False
        })
        return _obj

