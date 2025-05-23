# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, field_validator

class SetUserStateRequest(BaseModel):
    """
    SetUserStateRequest
    """
    state: StrictInt = Field(..., description="Set to the state value. Valid values include:   - 0 : Unapproved   - 1 : Approved   - 2 : Rejected   - 3 : Unlicensed")
    __properties = ["state"]

    @field_validator('state')
    @classmethod
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (0, 1, 2, 3):
            raise ValueError("must be one of enum values (0, 1, 2, 3)")
        return value

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
    def from_json(cls, json_str: str) -> SetUserStateRequest:
        """Create an instance of SetUserStateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetUserStateRequest:
        """Create an instance of SetUserStateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetUserStateRequest.parse_obj(obj)

        _obj = SetUserStateRequest.parse_obj({
            "state": obj.get("state")
        })
        return _obj

