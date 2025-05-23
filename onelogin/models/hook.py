# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist, field_validator
from onelogin.models.condition import Condition
from onelogin.models.hook_options import HookOptions

class Hook(BaseModel):
    """
    Hook
    """
    id: Optional[StrictStr] = Field(None, description="The Hook unique ID in OneLogin.")
    type: StrictStr = Field(..., description="A string describing the type of hook. e.g. `pre-authentication`")
    disabled: StrictBool = Field(..., description="Boolean to enable or disable the hook. Disabled hooks will not run.")
    timeout: StrictInt = Field(..., description="The number of seconds to allow the hook function to run before before timing out. Maximum timeout varies based on the type of hook.")
    env_vars: conlist(StrictStr) = Field(..., description="Environment Variable objects that will be available via process.env.ENV_VAR_NAME in the hook code.")
    runtime: StrictStr = Field(..., description="The Smart Hooks supported Node.js version to execute this hook with.")
    retries: conint(strict=True, le=4) = Field(..., description="Number of retries if execution fails.")
    packages: Dict[str, StrictStr] = Field(..., description="An object containing NPM packages that are bundled with the hook function.")
    function: StrictStr = Field(..., description="A base64 encoded string containing the javascript function code.")
    context_version: Optional[StrictStr] = Field(None, description="The semantic version of the content that will be injected into this hook.")
    status: Optional[StrictStr] = Field(None, description="String describing the state of the hook function. When a hook is ready and disabled is false it will be executed.")
    options: Optional[HookOptions] = None
    conditions: Optional[conlist(Condition)] = Field(None, description="An array of objects that let you limit the execution of a hook to users in specific roles.")
    created_at: Optional[StrictStr] = Field(None, description="ISO8601 format date that they hook function was created.")
    updated_at: Optional[StrictStr] = Field(None, description="ISO8601 format date that they hook function was last updated.")
    __properties = ["id", "type", "disabled", "timeout", "env_vars", "runtime", "retries", "packages", "function", "context_version", "status", "options", "conditions", "created_at", "updated_at"]

    @field_validator('status')
    @classmethod
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ready', 'create-queued', 'create-running', 'create-failed', 'update-queued', 'update-running', 'update-failed'):
            raise ValueError("must be one of enum values ('ready', 'create-queued', 'create-running', 'create-failed', 'update-queued', 'update-running', 'update-failed')")
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
    def from_json(cls, json_str: str) -> Hook:
        """Create an instance of Hook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Hook:
        """Create an instance of Hook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Hook.parse_obj(obj)

        _obj = Hook.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "disabled": obj.get("disabled") if obj.get("disabled") is not None else True,
            "timeout": obj.get("timeout") if obj.get("timeout") is not None else 1,
            "env_vars": obj.get("env_vars"),
            "runtime": obj.get("runtime"),
            "retries": obj.get("retries") if obj.get("retries") is not None else 0,
            "packages": obj.get("packages"),
            "function": obj.get("function"),
            "context_version": obj.get("context_version"),
            "status": obj.get("status"),
            "options": HookOptions.from_dict(obj.get("options")) if obj.get("options") is not None else None,
            "conditions": [Condition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

