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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class SsoSamlCertificate(BaseModel):
    """
    The Certificate used for signing
    """
    id: Optional[StrictInt] = Field(None, description="SAML Certificate ID")
    name: Optional[StrictStr] = Field(None, description="SAML Certificate Name")
    value: Optional[StrictStr] = Field(None, description="SAML Certificate Value")
    __properties = ["id", "name", "value"]

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
    def from_json(cls, json_str: str) -> SsoSamlCertificate:
        """Create an instance of SsoSamlCertificate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SsoSamlCertificate:
        """Create an instance of SsoSamlCertificate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SsoSamlCertificate.parse_obj(obj)

        _obj = SsoSamlCertificate.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "value": obj.get("value")
        })
        return _obj

