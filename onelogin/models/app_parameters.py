# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Dict, Any, ClassVar, List
from pydantic import BaseModel, Field, StrictBool, StrictStr

class AppParameters(BaseModel):
    """
    The parameters section contains parameterized attributes that have defined at the connector level as well as custom attributes that have been defined specifically for this app. Regardless of how they are defined, all parameters have the following attributes. Each parameter is an object with the key for the object being set as the parameters short name.
    """
    user_attribute_mappings: Optional[StrictStr] = Field(None, description="A user attribute to map values from For custom attributes prefix the name of the attribute with `custom_attribute_`. e.g. To get the value for custom attribute `employee_id` use `custom_attribute_employee_id`.")
    user_attribute_macros: Optional[StrictStr] = Field(None, description="When `user_attribute_mappings` is set to `_macro_` this macro will be used to assign the parameter value.")
    label: Optional[StrictStr] = Field(None, description="The can only be set when creating a new parameter. It can not be updated.")
    include_in_saml_assertion: Optional[StrictBool] = Field(None, description="When true, this parameter will be included in a SAML assertion payload.")
    additional_properties: Dict[str, Any] = {}
    
    # Define properties as a class variable
    _properties: ClassVar[List[str]] = ["user_attribute_mappings", "user_attribute_macros", "label", "include_in_saml_assertion"]

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
    def from_json(cls, json_str: str) -> AppParameters:
        """Create an instance of AppParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AppParameters:
        """Create an instance of AppParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AppParameters.parse_obj(obj)

        _obj = AppParameters.parse_obj({
            "user_attribute_mappings": obj.get("user_attribute_mappings"),
            "user_attribute_macros": obj.get("user_attribute_macros"),
            "label": obj.get("label"),
            "include_in_saml_assertion": obj.get("include_in_saml_assertion")
        })
        # store additional fields in additional_properties
        standard_props = getattr(cls, "_properties", ["user_attribute_mappings", "user_attribute_macros", "label", "include_in_saml_assertion"])
        for _key in obj.keys():
            if _key not in standard_props:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

