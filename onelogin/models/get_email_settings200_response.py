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
from onelogin.models.email_config import EmailConfig
from onelogin.models.get_email_settings200_response_one_of import GetEmailSettings200ResponseOneOf
from typing import Any, List, Literal
from pydantic import StrictStr, Field

GETEMAILSETTINGS200RESPONSE_ONE_OF_SCHEMAS = ["EmailConfig", "GetEmailSettings200ResponseOneOf"]

class GetEmailSettings200Response(BaseModel):
    """
    GetEmailSettings200Response
    """
    # data type: GetEmailSettings200ResponseOneOf
    oneof_schema_1_validator: Optional[GetEmailSettings200ResponseOneOf] = None
    # data type: EmailConfig
    oneof_schema_2_validator: Optional[EmailConfig] = None
    actual_instance: Any
    one_of_schemas: List[str] = Literal[GETEMAILSETTINGS200RESPONSE_ONE_OF_SCHEMAS]

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
        instance = GetEmailSettings200Response.construct()
        error_messages = []
        match = 0
        # validate data type: GetEmailSettings200ResponseOneOf
        if not isinstance(v, GetEmailSettings200ResponseOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetEmailSettings200ResponseOneOf`")
        else:
            match += 1
        # validate data type: EmailConfig
        if not isinstance(v, EmailConfig):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EmailConfig`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetEmailSettings200Response with oneOf schemas: EmailConfig, GetEmailSettings200ResponseOneOf. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetEmailSettings200Response with oneOf schemas: EmailConfig, GetEmailSettings200ResponseOneOf. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GetEmailSettings200Response:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GetEmailSettings200Response:
        """Returns the object represented by the json string"""
        instance = GetEmailSettings200Response.construct()
        error_messages = []
        match = 0

        # deserialize data into GetEmailSettings200ResponseOneOf
        try:
            instance.actual_instance = GetEmailSettings200ResponseOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EmailConfig
        try:
            instance.actual_instance = EmailConfig.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetEmailSettings200Response with oneOf schemas: EmailConfig, GetEmailSettings200ResponseOneOf. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetEmailSettings200Response with oneOf schemas: EmailConfig, GetEmailSettings200ResponseOneOf. Details: " + ", ".join(error_messages))
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

