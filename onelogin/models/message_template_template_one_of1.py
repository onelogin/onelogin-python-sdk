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



from pydantic import BaseModel, Field, constr

class MessageTemplateTemplateOneOf1(BaseModel):
    """
    MessageTemplateTemplateOneOf1
    """
    message: constr(strict=True, max_length=160) = Field(..., description="The body of the SMS message. Max length 160 characters.")
    __properties = ["message"]

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

        if type(obj) is not dict:
            return MessageTemplateTemplateOneOf1.parse_obj(obj)

        _obj = MessageTemplateTemplateOneOf1.parse_obj({
            "message": obj.get("message")
        })
        return _obj

