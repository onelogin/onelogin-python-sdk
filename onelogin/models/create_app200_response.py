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
from onelogin.models.generic_app import GenericApp
from onelogin.models.oidc_app import OidcApp
from onelogin.models.saml_app import SamlApp
from typing import Any, List, Literal, ClassVar
from pydantic import StrictStr, Field

CREATEAPP200RESPONSE_ONE_OF_SCHEMAS = ["GenericApp", "OidcApp", "SamlApp"]

class CreateApp200Response(BaseModel):
    """
    CreateApp200Response
    """
    # data type: OidcApp
    oneof_schema_1_validator: Optional[OidcApp] = None
    # data type: SamlApp
    oneof_schema_2_validator: Optional[SamlApp] = None
    # data type: GenericApp
    oneof_schema_3_validator: Optional[GenericApp] = None
    actual_instance: Any
    one_of_schemas: List[str] = Literal[CREATEAPP200RESPONSE_ONE_OF_SCHEMAS]

    """Pydantic configuration"""
    model_config = {
        "validate_assignment": True
    }

    discriminator_value_class_map: ClassVar[dict] = {
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
        instance = CreateApp200Response.construct()
        error_messages = []
        match = 0
        # validate data type: OidcApp
        if not isinstance(v, OidcApp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OidcApp`")
        else:
            match += 1
        # validate data type: SamlApp
        if not isinstance(v, SamlApp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SamlApp`")
        else:
            match += 1
        # validate data type: GenericApp
        if not isinstance(v, GenericApp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GenericApp`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateApp200Response with oneOf schemas: GenericApp, OidcApp, SamlApp. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateApp200Response with oneOf schemas: GenericApp, OidcApp, SamlApp. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> CreateApp200Response:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> CreateApp200Response:
        """Returns the object represented by the json string"""
        instance = CreateApp200Response.construct()
        error_messages = []
        match = 0

        # deserialize data into OidcApp
        try:
            instance.actual_instance = OidcApp.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SamlApp
        try:
            instance.actual_instance = SamlApp.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GenericApp
        try:
            instance.actual_instance = GenericApp.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateApp200Response with oneOf schemas: GenericApp, OidcApp, SamlApp. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateApp200Response with oneOf schemas: GenericApp, OidcApp, SamlApp. Details: " + ", ".join(error_messages))
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

