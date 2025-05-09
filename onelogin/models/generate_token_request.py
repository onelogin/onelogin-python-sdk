# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class GenerateTokenRequest(BaseModel):
    """
    GenerateTokenRequest
    """
    grant_type: StrictStr = Field(..., description="Set to client_credentials.")
    __properties = ["grant_type"]

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
    def from_json(cls, json_str: str) -> GenerateTokenRequest:
        """Create an instance of GenerateTokenRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GenerateTokenRequest:
        """Create an instance of GenerateTokenRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GenerateTokenRequest.parse_obj(obj)

        _obj = GenerateTokenRequest.parse_obj({
            "grant_type": obj.get("grant_type") if obj.get("grant_type") is not None else 'client_credentials'
        })
        return _obj

