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
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr, field_validator
from onelogin.models.message_template_template import MessageTemplateTemplate

class MessageTemplate(BaseModel):
    """
    MessageTemplate
    """
    id: Optional[StrictInt] = None
    account_id: Optional[StrictInt] = None
    type: StrictStr = Field(..., description="Template type that describes the source (sms, voice, email) and purpose (registration, invite, etc)")
    locale: constr(strict=True) = Field(..., description="The 2 character language locale for the template. e.g. en = English, es = Spanish")
    template: MessageTemplateTemplate = ...
    template_class: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = Field(None, description="Last time template was updated")
    brand_id: Optional[StrictInt] = Field(None, description="brand id number")
    __properties = ["id", "account_id", "type", "locale", "template", "template_class", "updated_at", "brand_id"]

    @field_validator('type')
    @classmethod
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('email_forgot_password', 'email_code_registration', 'email_code_login_verification', 'email_code_app_verification', 'email_code_pw_reset_verification', 'email_magiclink_registration', 'email_magiclink_login_verification', 'email_magiclink_app_verification', 'email_magiclink_pw_reset_verification', 'sms_registration', 'sms_login_verification', 'sms_app_verification', 'sms_pw_reset_verification'):
            raise ValueError("must be one of enum values ('email_forgot_password', 'email_code_registration', 'email_code_login_verification', 'email_code_app_verification', 'email_code_pw_reset_verification', 'email_magiclink_registration', 'email_magiclink_login_verification', 'email_magiclink_app_verification', 'email_magiclink_pw_reset_verification', 'sms_registration', 'sms_login_verification', 'sms_app_verification', 'sms_pw_reset_verification')")
        return value

    @field_validator('locale')
    @classmethod
    def locale_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z]{2}$", value):
            raise ValueError(r"must validate the regular expression /^[a-z]{2}$/")
        return value

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
    def from_json(cls, json_str: str) -> MessageTemplate:
        """Create an instance of MessageTemplate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "account_id",
                            "template_class",
                            "updated_at",
                            "brand_id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessageTemplate:
        """Create an instance of MessageTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MessageTemplate.parse_obj(obj)

        _obj = MessageTemplate.parse_obj({
            "id": obj.get("id"),
            "account_id": obj.get("account_id"),
            "type": obj.get("type"),
            "locale": obj.get("locale"),
            "template": MessageTemplateTemplate.from_dict(obj.get("template")) if obj.get("template") is not None else None,
            "template_class": obj.get("template_class"),
            "updated_at": obj.get("updated_at"),
            "brand_id": obj.get("brand_id")
        })
        return _obj

