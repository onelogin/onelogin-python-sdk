# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, constr

class MessageTemplateTemplateOneOf1(BaseModel):
    """
    MessageTemplateTemplateOneOf1
    """
    message: constr(strict=True, max_length=160) = Field(..., description="The body of the SMS message. Max length 160 characters.")
    __properties = ["message"]

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
    def from_json(cls, json_str: str) -> MessageTemplateTemplateOneOf1:
        """Create an instance of MessageTemplateTemplateOneOf1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessageTemplateTemplateOneOf1:
        """Create an instance of MessageTemplateTemplateOneOf1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MessageTemplateTemplateOneOf1.parse_obj(obj)

        _obj = MessageTemplateTemplateOneOf1.parse_obj({
            "message": obj.get("message")
        })
        return _obj

