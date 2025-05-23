# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class RequestBrand(BaseModel):
    """
    RequestBrand
    """
    enabled: Optional[StrictBool] = Field(False, description="Indicates if the brand is enabled or not")
    name: StrictStr = Field(..., description="Brand’s name for humans. This isn’t related to subdomains.")
    custom_support_enabled: Optional[StrictBool] = Field(None, description="Indicates if the custom support is enabled. If enabled, the login page includes the ability to submit a support request.")
    custom_color: Optional[StrictStr] = Field(None, description="Primary brand color")
    custom_accent_color: Optional[StrictStr] = Field(None, description="Secondary brand color")
    custom_masking_color: Optional[StrictStr] = Field(None, description="Color for the masking layer above the background image of the branded login screen.")
    custom_masking_opacity: Optional[StrictInt] = Field(None, description="Opacity for the custom_masking_color.")
    enable_custom_label_for_login_screen: Optional[StrictBool] = Field(None, description="Indicates if the custom Username/Email field label is enabled or not")
    custom_label_text_for_login_screen: Optional[StrictStr] = Field(None, description="Custom label for the Username/Email field on the login screen. See example here.")
    login_instruction_title: Optional[StrictStr] = Field(None, description="Link text to show login instruction screen.")
    login_instruction: Optional[StrictStr] = Field(None, description="Text for the login instruction screen, styled in Markdown.")
    hide_onelogin_footer: Optional[StrictBool] = Field(None, description="Indicates if the OneLogin footer will appear at the bottom of the login page.")
    mfa_enrollment_message: Optional[StrictStr] = Field(None, description="Text that replaces the default text displayed on the initial screen of the MFA Registration.")
    background: Optional[StrictStr] = Field(None, description="Base64 encoded image data (JPG/PNG, <5MB)")
    logo: Optional[StrictStr] = Field(None, description="Base64 encoded image data (PNG, <1MB)")
    __properties = ["enabled", "name", "custom_support_enabled", "custom_color", "custom_accent_color", "custom_masking_color", "custom_masking_opacity", "enable_custom_label_for_login_screen", "custom_label_text_for_login_screen", "login_instruction_title", "login_instruction", "hide_onelogin_footer", "mfa_enrollment_message", "background", "logo"]

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
    def from_json(cls, json_str: str) -> RequestBrand:
        """Create an instance of RequestBrand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RequestBrand:
        """Create an instance of RequestBrand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestBrand.parse_obj(obj)

        _obj = RequestBrand.parse_obj({
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "name": obj.get("name"),
            "custom_support_enabled": obj.get("custom_support_enabled"),
            "custom_color": obj.get("custom_color"),
            "custom_accent_color": obj.get("custom_accent_color"),
            "custom_masking_color": obj.get("custom_masking_color"),
            "custom_masking_opacity": obj.get("custom_masking_opacity"),
            "enable_custom_label_for_login_screen": obj.get("enable_custom_label_for_login_screen"),
            "custom_label_text_for_login_screen": obj.get("custom_label_text_for_login_screen"),
            "login_instruction_title": obj.get("login_instruction_title"),
            "login_instruction": obj.get("login_instruction"),
            "hide_onelogin_footer": obj.get("hide_onelogin_footer"),
            "mfa_enrollment_message": obj.get("mfa_enrollment_message"),
            "background": obj.get("background"),
            "logo": obj.get("logo")
        })
        return _obj

