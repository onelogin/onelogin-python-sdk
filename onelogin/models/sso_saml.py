# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr
from onelogin.models.sso_saml_certificate import SsoSamlCertificate

class SsoSaml(BaseModel):
    """
    SsoSaml
    """
    metadata_url: Optional[StrictStr] = None
    acs_url: Optional[StrictStr] = None
    sls_url: Optional[StrictStr] = None
    issuer: Optional[StrictStr] = None
    certificate: Optional[SsoSamlCertificate] = None
    __properties = ["metadata_url", "acs_url", "sls_url", "issuer", "certificate"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SsoSaml:
        """Create an instance of SsoSaml from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of certificate
        if self.certificate:
            _dict['certificate'] = self.certificate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SsoSaml:
        """Create an instance of SsoSaml from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SsoSaml.parse_obj(obj)

        _obj = SsoSaml.parse_obj({
            "metadata_url": obj.get("metadata_url"),
            "acs_url": obj.get("acs_url"),
            "sls_url": obj.get("sls_url"),
            "issuer": obj.get("issuer"),
            "certificate": SsoSamlCertificate.from_dict(obj.get("certificate")) if obj.get("certificate") is not None else None
        })
        return _obj

