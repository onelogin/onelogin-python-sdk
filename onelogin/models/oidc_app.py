# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from onelogin.models.app_parameters import AppParameters
from onelogin.models.auth_method import AuthMethod
from onelogin.models.configuration_oidc import ConfigurationOidc
from onelogin.models.enforcement_point import EnforcementPoint
from onelogin.models.generic_app_provisioning import GenericAppProvisioning
from onelogin.models.sso_oidc import SsoOidc

class OidcApp(BaseModel):
    """
    OidcApp
    """
    id: Optional[StrictInt] = Field(None, description="Apps unique ID in OneLogin.")
    name: StrictStr = Field(..., description="The name of the app.")
    visible: StrictBool = Field(..., description="Indicates if the app is visible in the OneLogin portal.")
    description: StrictStr = Field(..., description="Freeform description of the app.")
    notes: Optional[StrictStr] = Field(None, description="Freeform notes about the app.")
    icon_url: Optional[StrictStr] = Field(None, description="A link to the apps icon url")
    auth_method: Optional[AuthMethod] = None
    policy_id: StrictInt = Field(..., description="The security policy assigned to the app.")
    allow_assumed_signin: Optional[StrictBool] = Field(None, description="Indicates whether or not administrators can access the app as a user that they have assumed control over.")
    tab_id: Optional[StrictInt] = Field(None, description="ID of the OneLogin portal tab that the app is assigned to.")
    connector_id: StrictInt = Field(..., description="ID of the connector to base the app from.")
    created_at: Optional[StrictStr] = Field(None, description="the date the app was created")
    updated_at: Optional[StrictStr] = Field(None, description="the date the app was last updated")
    role_ids: Optional[conlist(StrictInt)] = Field(None, description="List of Role IDs that are assigned to the app. On App Create or Update the entire array is replaced with the values provided.")
    provisioning: Optional[GenericAppProvisioning] = None
    parameters: Optional[AppParameters] = None
    enforcement_point: Optional[EnforcementPoint] = None
    configuration: ConfigurationOidc = ...
    sso: Optional[SsoOidc] = None
    __properties = ["id", "name", "visible", "description", "notes", "icon_url", "auth_method", "policy_id", "allow_assumed_signin", "tab_id", "connector_id", "created_at", "updated_at", "role_ids", "provisioning", "parameters", "enforcement_point", "configuration", "sso"]

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
    def from_json(cls, json_str: str) -> OidcApp:
        """Create an instance of OidcApp from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of provisioning
        if self.provisioning:
            _dict['provisioning'] = self.provisioning.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enforcement_point
        if self.enforcement_point:
            _dict['enforcement_point'] = self.enforcement_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sso
        if self.sso:
            _dict['sso'] = self.sso.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OidcApp:
        """Create an instance of OidcApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OidcApp.parse_obj(obj)

        _obj = OidcApp.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "visible": obj.get("visible"),
            "description": obj.get("description"),
            "notes": obj.get("notes"),
            "icon_url": obj.get("icon_url"),
            "auth_method": obj.get("auth_method"),
            "policy_id": obj.get("policy_id"),
            "allow_assumed_signin": obj.get("allow_assumed_signin"),
            "tab_id": obj.get("tab_id"),
            "connector_id": obj.get("connector_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "role_ids": obj.get("role_ids"),
            "provisioning": GenericAppProvisioning.from_dict(obj.get("provisioning")) if obj.get("provisioning") is not None else None,
            "parameters": AppParameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None,
            "enforcement_point": EnforcementPoint.from_dict(obj.get("enforcement_point")) if obj.get("enforcement_point") is not None else None,
            "configuration": ConfigurationOidc.from_dict(obj.get("configuration")) if obj.get("configuration") is not None else None,
            "sso": SsoOidc.from_dict(obj.get("sso")) if obj.get("sso") is not None else None
        })
        return _obj

