# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class GenerateOTP201Response(BaseModel):
    """
    GenerateOTP201Response
    """
    mfa_token: Optional[StrictStr] = Field(None, description="Token can function as a temporary MFA token. It can be used to authenticate for any app when valid.")
    reusable: Optional[StrictBool] = Field(False, description="true indcates the token can be used multiple times, until it expires. false indicates the token is invalid after a single use or once it expires. Defaults to false.")
    expires_at: Optional[StrictStr] = Field(None, description="Defines the expiration time and date for the token. Format is UTC time.")
    device_id: Optional[StrictStr] = Field(None, description="A unique identifier for the temp otp device that has been created for this token.")
    __properties = ["mfa_token", "reusable", "expires_at", "device_id"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GenerateOTP201Response:
        """Create an instance of GenerateOTP201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GenerateOTP201Response:
        """Create an instance of GenerateOTP201Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GenerateOTP201Response.parse_obj(obj)

        _obj = GenerateOTP201Response.parse_obj({
            "mfa_token": obj.get("mfa_token"),
            "reusable": obj.get("reusable") if obj.get("reusable") is not None else False,
            "expires_at": obj.get("expires_at"),
            "device_id": obj.get("device_id")
        })
        return _obj

