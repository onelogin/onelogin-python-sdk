
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
from pydantic import BaseModel, Field, StrictBool, StrictInt

class GenerateOTPRequest(BaseModel):
    """
    GenerateOTPRequest
    """
    expires_in: Optional[StrictInt] = Field(None, description="Set the duration of the token in seconds. Token expiration defaults to 259200 seconds = 72 hours. 72 hours is the max value.")
    reusable: Optional[StrictBool] = Field(False, description="Defines if the token is reusable multiple times within the expiry window. Value defaults to false. If set to true, token can be used multiple times, until it expires.")
    __properties = ["expires_in", "reusable"]

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
    def from_json(cls, json_str: str) -> GenerateOTPRequest:
        """Create an instance of GenerateOTPRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GenerateOTPRequest:
        """Create an instance of GenerateOTPRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GenerateOTPRequest.parse_obj(obj)

        _obj = GenerateOTPRequest.parse_obj({
            "expires_in": obj.get("expires_in"),
            "reusable": obj.get("reusable") if obj.get("reusable") is not None else False
        })
        return _obj

