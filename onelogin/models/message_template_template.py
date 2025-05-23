# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from onelogin.models.message_template_template_one_of import MessageTemplateTemplateOneOf
from onelogin.models.message_template_template_one_of1 import MessageTemplateTemplateOneOf1
from typing import Any, List, Literal
from pydantic import StrictStr

MESSAGETEMPLATETEMPLATE_ONE_OF_SCHEMAS = ["MessageTemplateTemplateOneOf", "MessageTemplateTemplateOneOf1"]

class MessageTemplateTemplate(BaseModel):
    """
    MessageTemplateTemplate
    """
    # data type: MessageTemplateTemplateOneOf
    oneof_schema_1_validator: Optional[MessageTemplateTemplateOneOf] = None
    # data type: MessageTemplateTemplateOneOf1
    oneof_schema_2_validator: Optional[MessageTemplateTemplateOneOf1] = None
    actual_instance: Any
    one_of_schemas: List[str] = Literal[MESSAGETEMPLATETEMPLATE_ONE_OF_SCHEMAS]

    """Pydantic configuration"""
    model_config = {
        "validate_assignment": True
    }

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    @classmethod
    def actual_instance_must_validate_oneof(cls, v):
        instance = MessageTemplateTemplate.construct()
        error_messages = []
        match = 0
        # validate data type: MessageTemplateTemplateOneOf
        if not isinstance(v, MessageTemplateTemplateOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageTemplateTemplateOneOf`")
        else:
            match += 1
        # validate data type: MessageTemplateTemplateOneOf1
        if not isinstance(v, MessageTemplateTemplateOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageTemplateTemplateOneOf1`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in MessageTemplateTemplate with oneOf schemas: MessageTemplateTemplateOneOf, MessageTemplateTemplateOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in MessageTemplateTemplate with oneOf schemas: MessageTemplateTemplateOneOf, MessageTemplateTemplateOneOf1. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> MessageTemplateTemplate:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> MessageTemplateTemplate:
        """Returns the object represented by the json string"""
        instance = MessageTemplateTemplate.construct()
        error_messages = []
        match = 0

        # deserialize data into MessageTemplateTemplateOneOf
        try:
            instance.actual_instance = MessageTemplateTemplateOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MessageTemplateTemplateOneOf1
        try:
            instance.actual_instance = MessageTemplateTemplateOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into MessageTemplateTemplate with oneOf schemas: MessageTemplateTemplateOneOf, MessageTemplateTemplateOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into MessageTemplateTemplate with oneOf schemas: MessageTemplateTemplateOneOf, MessageTemplateTemplateOneOf1. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

