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
from pydantic import BaseModel
from onelogin.models.configuration_oidc import ConfigurationOidc
from onelogin.models.sso_oidc import SsoOidc

class OidcAppAllOf(BaseModel):
    """
    OidcAppAllOf
    """
    configuration: ConfigurationOidc = ...
    sso: Optional[SsoOidc] = None
    __properties = ["configuration", "sso"]

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
    def from_json(cls, json_str: str) -> OidcAppAllOf:
        """Create an instance of OidcAppAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sso
        if self.sso:
            _dict['sso'] = self.sso.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OidcAppAllOf:
        """Create an instance of OidcAppAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OidcAppAllOf.parse_obj(obj)

        _obj = OidcAppAllOf.parse_obj({
            "configuration": ConfigurationOidc.from_dict(obj.get("configuration")) if obj.get("configuration") is not None else None,
            "sso": SsoOidc.from_dict(obj.get("sso")) if obj.get("sso") is not None else None
        })
        return _obj

