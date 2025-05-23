# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator

class ConfigurationOidc(BaseModel):
    """
    ConfigurationOidc
    """
    login_url: StrictStr = Field(..., description="The OpenId Connect Client Id. Note that client_secret is only returned after Creating an App.")
    redirect_uri: StrictStr = Field(..., description="Comma or newline separated list of valid redirect uris for the OpenId Connect Authorization Code flow.")
    access_token_expiration_minutes: StrictInt = Field(..., description="Number of minutes the refresh token will be valid for.")
    refresh_token_expiration_minutes: StrictInt = Field(..., description="Number of minutes the refresh token will be valid for.")
    token_endpoint_auth_method: StrictInt = Field(..., description="- 0: Basic - 1: POST - 2: None / PKCE")
    oidc_application_type: StrictInt = Field(..., description="- 0 : Web - 1 : Native / Mobile")
    __properties = ["login_url", "redirect_uri", "access_token_expiration_minutes", "refresh_token_expiration_minutes", "token_endpoint_auth_method", "oidc_application_type"]

    @field_validator('token_endpoint_auth_method')
    @classmethod
    def token_endpoint_auth_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (0, 1, 2):
            raise ValueError("must be one of enum values (0, 1, 2)")
        return value

    @field_validator('oidc_application_type')
    @classmethod
    def oidc_application_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (0, 1):
            raise ValueError("must be one of enum values (0, 1)")
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
    def from_json(cls, json_str: str) -> ConfigurationOidc:
        """Create an instance of ConfigurationOidc from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigurationOidc:
        """Create an instance of ConfigurationOidc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigurationOidc.parse_obj(obj)

        _obj = ConfigurationOidc.parse_obj({
            "login_url": obj.get("login_url"),
            "redirect_uri": obj.get("redirect_uri"),
            "access_token_expiration_minutes": obj.get("access_token_expiration_minutes"),
            "refresh_token_expiration_minutes": obj.get("refresh_token_expiration_minutes"),
            "token_endpoint_auth_method": obj.get("token_endpoint_auth_method"),
            "oidc_application_type": obj.get("oidc_application_type")
        })
        return _obj

