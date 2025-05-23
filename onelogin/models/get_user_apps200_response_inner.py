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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, field_validator

class GetUserApps200ResponseInner(BaseModel):
    """
    GetUserApps200ResponseInner
    """
    id: Optional[StrictInt] = Field(None, description="The App ID")
    icon_url: Optional[StrictStr] = Field(None, description="A url for the icon that represents the app in the OneLogin portal")
    extension: Optional[StrictBool] = Field(None, description="Boolean that indicates if the OneLogin browser extension is required to launch this app.")
    login_id: Optional[StrictInt] = Field(None, description="Unqiue identifier for this user and app combination.")
    name: Optional[StrictStr] = Field(None, description="The name of the app.")
    provisioning_status: Optional[StrictStr] = None
    provisioning_state: Optional[StrictStr] = Field(None, description="If provisioning is enabled this indicates the state of provisioning for the given user.")
    provisioning_enabled: Optional[StrictBool] = Field(None, description="Indicates if provisioning is enabled for this app.")
    __properties = ["id", "icon_url", "extension", "login_id", "name", "provisioning_status", "provisioning_state", "provisioning_enabled"]

    @field_validator('provisioning_status')
    @classmethod
    def provisioning_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('enabling', 'disabling', 'enabling_pending_approval', 'disabling_pendding_approval', 'enabled', 'disabled', 'disabling_failed', 'enabling_failed'):
            raise ValueError("must be one of enum values ('enabling', 'disabling', 'enabling_pending_approval', 'disabling_pendding_approval', 'enabled', 'disabled', 'disabling_failed', 'enabling_failed')")
        return value

    @field_validator('provisioning_state')
    @classmethod
    def provisioning_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('unknown', 'provisioning', 'modifying', 'deleting', 'provisioning_pending_approval', 'deleting_pending_approval', 'modifying_pending_approval', 'linking', 'provisioned', 'deleted', 'modifying_failed', 'provisioning_failed', 'deleting_failed', 'linking_failed', 'disabled', 'nonexistent', 'modifying_pending_approval_then_disabled'):
            raise ValueError("must be one of enum values ('unknown', 'provisioning', 'modifying', 'deleting', 'provisioning_pending_approval', 'deleting_pending_approval', 'modifying_pending_approval', 'linking', 'provisioned', 'deleted', 'modifying_failed', 'provisioning_failed', 'deleting_failed', 'linking_failed', 'disabled', 'nonexistent', 'modifying_pending_approval_then_disabled')")
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
    def from_json(cls, json_str: str) -> GetUserApps200ResponseInner:
        """Create an instance of GetUserApps200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetUserApps200ResponseInner:
        """Create an instance of GetUserApps200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetUserApps200ResponseInner.parse_obj(obj)

        _obj = GetUserApps200ResponseInner.parse_obj({
            "id": obj.get("id"),
            "icon_url": obj.get("icon_url"),
            "extension": obj.get("extension"),
            "login_id": obj.get("login_id"),
            "name": obj.get("name"),
            "provisioning_status": obj.get("provisioning_status"),
            "provisioning_state": obj.get("provisioning_state"),
            "provisioning_enabled": obj.get("provisioning_enabled")
        })
        return _obj

