# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt

class LockAccountUserRequest(BaseModel):
    """
    LockAccountUserRequest
    """
    locked_until: StrictInt = Field(..., description="Set to the number of minutes for which you want to lock the user account. Set to 0 if you want to lock the user account based on the Lock effective period set in the policy assigned to the user. If no policy is assigned to the user, setting this value to 0 will lock the user’s account until you unlock it Note that this value can not be less time that the Lock Effective Period specified on a user policy.")
    __properties = ["locked_until"]

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
    def from_json(cls, json_str: str) -> LockAccountUserRequest:
        """Create an instance of LockAccountUserRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LockAccountUserRequest:
        """Create an instance of LockAccountUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LockAccountUserRequest.parse_obj(obj)

        _obj = LockAccountUserRequest.parse_obj({
            "locked_until": obj.get("locked_until")
        })
        return _obj

