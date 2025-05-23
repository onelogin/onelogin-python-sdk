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

class UpdatePasswordSecureRequest(BaseModel):
    """
    UpdatePasswordSecureRequest
    """
    password: StrictStr = Field(..., description="Set to the password value using a SHA-256-encoded value. If you are including your own password_salt value in your request, prepend the salt value to the cleartext password value before SHA-256-encoding it. For example, if your salt value is hello and your cleartext password value is password, the value you need to SHA-256-encode is hellopassword. The resulting encoded value would be b1c788abac15390de987ad17b65ac73c9b475d428a51f245c645a442fddd078b. Note that the alpha characters in this has must all be lower case.")
    password_confirmation: StrictStr = Field(..., description="This value must match the password value.")
    password_algorithm: StrictStr = Field(..., description="Set to salt+sha256.")
    password_salt: Optional[StrictStr] = Field(None, description="Optional. If your password hash has been salted then you can provide the salt used in this param. This assumes that the salt was prepended to the password before doing the SHA256 hash. The API supports a salt value that is up to 40 characters long.")
    __properties = ["password", "password_confirmation", "password_algorithm", "password_salt"]

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
    def from_json(cls, json_str: str) -> UpdatePasswordSecureRequest:
        """Create an instance of UpdatePasswordSecureRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdatePasswordSecureRequest:
        """Create an instance of UpdatePasswordSecureRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdatePasswordSecureRequest.parse_obj(obj)

        _obj = UpdatePasswordSecureRequest.parse_obj({
            "password": obj.get("password"),
            "password_confirmation": obj.get("password_confirmation"),
            "password_algorithm": obj.get("password_algorithm"),
            "password_salt": obj.get("password_salt")
        })
        return _obj

