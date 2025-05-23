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

class ConfigurationSaml(BaseModel):
    """
    ConfigurationSaml
    """
    signature_algorithm: Optional[StrictStr] = Field(None, description="One of the following:   - SHA-1   - SHA-256   - SHA-348   - SHA-512")
    certificate_id: Optional[StrictInt] = Field(None, description="When creating apps the default certificate will be used unless the `certificate_id` attribute is applied in the `configuration` object.")
    __properties = ["signature_algorithm", "certificate_id"]

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
    def from_json(cls, json_str: str) -> ConfigurationSaml:
        """Create an instance of ConfigurationSaml from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigurationSaml:
        """Create an instance of ConfigurationSaml from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigurationSaml.parse_obj(obj)

        _obj = ConfigurationSaml.parse_obj({
            "signature_algorithm": obj.get("signature_algorithm"),
            "certificate_id": obj.get("certificate_id")
        })
        return _obj

