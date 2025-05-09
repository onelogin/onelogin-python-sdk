
# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist, field_validator

class PrivilegePrivilegeStatementInner(BaseModel):
    """
    PrivilegePrivilegeStatementInner
    """
    effect: StrictStr = Field(..., alias="Effect", description="Set to “Allow.” By default, all actions are denied, this Statement allows the listed actions to be executed.")
    action: conlist(StrictStr) = Field(..., alias="Action", description="An array of strings that represent actions within OneLogin. Actions are prefixed with the class of object they are related to and followed by a specific action for the given class. e.g. users:List, where the class is users and the specific action is List. Don’t mix classes within an Action array. To create a privilege that includes multiple different classes, create multiple statements. A wildcard * that includes all actions is supported. Use wildcards to create a Super User privilege.")
    scope: conlist(StrictStr) = Field(..., alias="Scope", description="Target the privileged action against specific resources with the scope. The scope pattern is the class of object used by the Action, followed by an ID that represents a resource in OneLogin. e.g. apps/1234, where apps is the class and 1234 is the ID of an app. The wildcard * is supported and indicates that all resources of the class type declared, in the Action, are in scope. The Action and Scope classes must match. However, there is an exception, a scope of roles/{role_id} can be combined with Actions on the user or app class. The exception allows you to target groups of users or apps with specific actions.")
    __properties = ["Effect", "Action", "Scope"]

    @field_validator('action')
    @classmethod
    def action_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in ('apps:Create', 'apps:Delete', 'apps:List', 'apps:Get', 'apps:Update', 'apps:ManageConnectors', 'apps:ManageRoles', 'apps:ManageTabs', 'apps:ManageUsers', 'apps:ReapplyMappings', 'users:Create', 'users:Delete', 'users:List', 'users:Get', 'users:Update', 'users:AssumeUser', 'users:ManageApps', 'users:Unlock', 'users:GenerateTempMfaToken', 'users:ResetPassword', 'users:ReapplyMappings', 'users:ManageLicense', 'users:Invite', 'users:ManageRoles', 'roles:Create', 'roles:Get', 'roles:List', 'roles:Update', 'roles:Delete', 'roles:ManageUsers', 'roles:ManageApps', 'reports:Create', 'reports:Get', 'reports:List', 'reports:Update', 'reports:Delete', 'reports:Clone', 'events:Get', 'events:List', 'groups:Create', 'groups:Get', 'groups:List', 'groups:Update', 'groups:Delete', 'policies:Create', 'policies:Get', 'policies:List', 'policies:Update', 'policies:Delete', 'policies:SetDefault'):
                raise ValueError("each list item must be one of ('apps:Create', 'apps:Delete', 'apps:List', 'apps:Get', 'apps:Update', 'apps:ManageConnectors', 'apps:ManageRoles', 'apps:ManageTabs', 'apps:ManageUsers', 'apps:ReapplyMappings', 'users:Create', 'users:Delete', 'users:List', 'users:Get', 'users:Update', 'users:AssumeUser', 'users:ManageApps', 'users:Unlock', 'users:GenerateTempMfaToken', 'users:ResetPassword', 'users:ReapplyMappings', 'users:ManageLicense', 'users:Invite', 'users:ManageRoles', 'roles:Create', 'roles:Get', 'roles:List', 'roles:Update', 'roles:Delete', 'roles:ManageUsers', 'roles:ManageApps', 'reports:Create', 'reports:Get', 'reports:List', 'reports:Update', 'reports:Delete', 'reports:Clone', 'events:Get', 'events:List', 'groups:Create', 'groups:Get', 'groups:List', 'groups:Update', 'groups:Delete', 'policies:Create', 'policies:Get', 'policies:List', 'policies:Update', 'policies:Delete', 'policies:SetDefault')")
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
    def from_json(cls, json_str: str) -> PrivilegePrivilegeStatementInner:
        """Create an instance of PrivilegePrivilegeStatementInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrivilegePrivilegeStatementInner:
        """Create an instance of PrivilegePrivilegeStatementInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrivilegePrivilegeStatementInner.parse_obj(obj)

        _obj = PrivilegePrivilegeStatementInner.parse_obj({
            "effect": obj.get("Effect"),
            "action": obj.get("Action"),
            "scope": obj.get("Scope")
        })
        return _obj

