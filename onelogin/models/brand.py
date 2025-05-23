# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from onelogin.models.brand_background import BrandBackground
from onelogin.models.brand_logo import BrandLogo

class Brand(BaseModel):
    """
    Brand
    """
    id: StrictInt = ...
    enabled: StrictBool = Field(..., description="Indicates if the brand is enabled or not")
    custom_support_enabled: StrictBool = Field(..., description="Indicates if the custom support is enabled. If enabled, the login page includes the ability to submit a support request.")
    custom_color: StrictStr = Field(..., description="Primary brand color")
    custom_accent_color: StrictStr = Field(..., description="Secondary brand color")
    custom_masking_color: StrictStr = Field(..., description="Color for the masking layer above the background image of the branded login screen.")
    custom_masking_opacity: StrictInt = Field(..., description="Opacity for the custom_masking_color.")
    mfa_enrollment_message: StrictStr = Field(..., description="Text that replaces the default text displayed on the initial screen of the MFA Registration.")
    enable_custom_label_for_login_screen: StrictBool = Field(..., description="Indicates if the custom Username/Email field label is enabled or not")
    custom_label_text_for_login_screen: StrictStr = Field(..., description="Custom label for the Username/Email field on the login screen. See example here.")
    login_instruction: StrictStr = Field(..., description="Text for the login instruction screen, styled in Markdown.")
    login_instruction_title: StrictStr = Field(..., description="Link text to show login instruction screen.")
    hide_onelogin_footer: StrictBool = Field(..., description="Indicates if the OneLogin footer will appear at the bottom of the login page.")
    background: BrandBackground = ...
    logo: BrandLogo = ...
    __properties = ["id", "enabled", "custom_support_enabled", "custom_color", "custom_accent_color", "custom_masking_color", "custom_masking_opacity", "mfa_enrollment_message", "enable_custom_label_for_login_screen", "custom_label_text_for_login_screen", "login_instruction", "login_instruction_title", "hide_onelogin_footer", "background", "logo"]

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
    def from_json(cls, json_str: str) -> Brand:
        """Create an instance of Brand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of background
        if self.background:
            _dict['background'] = self.background.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Brand:
        """Create an instance of Brand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Brand.parse_obj(obj)

        _obj = Brand.parse_obj({
            "id": obj.get("id"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "custom_support_enabled": obj.get("custom_support_enabled"),
            "custom_color": obj.get("custom_color"),
            "custom_accent_color": obj.get("custom_accent_color"),
            "custom_masking_color": obj.get("custom_masking_color"),
            "custom_masking_opacity": obj.get("custom_masking_opacity"),
            "mfa_enrollment_message": obj.get("mfa_enrollment_message"),
            "enable_custom_label_for_login_screen": obj.get("enable_custom_label_for_login_screen"),
            "custom_label_text_for_login_screen": obj.get("custom_label_text_for_login_screen"),
            "login_instruction": obj.get("login_instruction"),
            "login_instruction_title": obj.get("login_instruction_title"),
            "hide_onelogin_footer": obj.get("hide_onelogin_footer"),
            "background": BrandBackground.from_dict(obj.get("background")) if obj.get("background") is not None else None,
            "logo": BrandLogo.from_dict(obj.get("logo")) if obj.get("logo") is not None else None
        })
        return _obj

