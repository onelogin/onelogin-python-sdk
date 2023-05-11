# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class VerifyUserRegistration200Response(BaseModel):
    """
    VerifyUserRegistration200Response
    """
    id: Optional[StrictStr] = Field(None, description="Registration identifier.")
    status: Optional[StrictStr] = Field(None, description="pending registration has not been completed successfully. accepted registration has successfully completed.")
    device_id: Optional[StrictStr] = Field(None, description="Device id to be used with Verify the Factor.")
    __properties = ["id", "status", "device_id"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> VerifyUserRegistration200Response:
        """Create an instance of VerifyUserRegistration200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyUserRegistration200Response:
        """Create an instance of VerifyUserRegistration200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VerifyUserRegistration200Response.parse_obj(obj)

        _obj = VerifyUserRegistration200Response.parse_obj({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "device_id": obj.get("device_id")
        })
        return _obj

