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
from pydantic import BaseModel, Field, SecretStr, StrictBool, StrictInt, StrictStr

class EmailConfig(BaseModel):
    """
    EmailConfig
    """
    address: StrictStr = Field(..., description="Email Settings server address")
    use_tls: Optional[StrictBool] = Field(True, description="Use TLS")
    var_from: StrictStr = Field(..., alias="from", description="The From email address in the message.")
    domain: StrictStr = Field(..., description="Domain of the From address.")
    user_name: Optional[StrictStr] = Field(None, description="The user name of the account to authenticate with the Email Settings server.")
    password: Optional[SecretStr] = Field(None, description="The password of the account to authenticate with the Email Settings server.")
    port: Optional[StrictInt] = Field(25, description="Defaults to 25.")
    __properties = ["address", "use_tls", "from", "domain", "user_name", "password", "port"]

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
    def from_json(cls, json_str: str) -> EmailConfig:
        """Create an instance of EmailConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EmailConfig:
        """Create an instance of EmailConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EmailConfig.parse_obj(obj)

        _obj = EmailConfig.parse_obj({
            "address": obj.get("address"),
            "use_tls": obj.get("use_tls") if obj.get("use_tls") is not None else True,
            "var_from": obj.get("from"),
            "domain": obj.get("domain"),
            "user_name": obj.get("user_name"),
            "password": obj.get("password"),
            "port": obj.get("port") if obj.get("port") is not None else 25
        })
        return _obj

