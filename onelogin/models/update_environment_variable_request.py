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

class UpdateEnvironmentVariableRequest(BaseModel):
    """
    UpdateEnvironmentVariableRequest
    """
    value: StrictStr = Field(..., description="The secret value that will be encrypted at rest and injected in applicable hook functions at run time.")
    __properties = ["value"]

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
    def from_json(cls, json_str: str) -> UpdateEnvironmentVariableRequest:
        """Create an instance of UpdateEnvironmentVariableRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateEnvironmentVariableRequest:
        """Create an instance of UpdateEnvironmentVariableRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateEnvironmentVariableRequest.parse_obj(obj)

        _obj = UpdateEnvironmentVariableRequest.parse_obj({
            "value": obj.get("value")
        })
        return _obj

