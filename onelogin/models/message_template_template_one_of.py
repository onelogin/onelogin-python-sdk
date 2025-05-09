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

class MessageTemplateTemplateOneOf(BaseModel):
    """
    MessageTemplateTemplateOneOf
    """
    subject: StrictStr = Field(..., description="Custom Email Subject")
    html: StrictStr = Field(..., description="The HTML body of the Custom Email")
    plain: StrictStr = Field(..., description="The Plain text body of the email")
    __properties = ["subject", "html", "plain"]

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
    def from_json(cls, json_str: str) -> MessageTemplateTemplateOneOf:
        """Create an instance of MessageTemplateTemplateOneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessageTemplateTemplateOneOf:
        """Create an instance of MessageTemplateTemplateOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MessageTemplateTemplateOneOf.parse_obj(obj)

        _obj = MessageTemplateTemplateOneOf.parse_obj({
            "subject": obj.get("subject"),
            "html": obj.get("html"),
            "plain": obj.get("plain")
        })
        return _obj

