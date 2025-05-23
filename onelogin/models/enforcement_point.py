# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, ClassVar
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, field_validator
from onelogin.models.clock_counter import ClockCounter
from onelogin.models.enforcement_point_resources_inner import EnforcementPointResourcesInner

class EnforcementPoint(BaseModel):
    """
    For apps that connect to a OneLogin Access Enforcement Point the following enforcement_point object will be included with the app payload.
    """
    require_sitewide_authentication: Optional[StrictBool] = Field(None, description="Require user authentication to access any resource protected by this enforcement point.")
    conditions: Optional[StrictStr] = Field(None, description="If access is conditional, the conditions that must evaluate to true to allow access to a resource. For example, to require the user must be authenticated and have either the role Admin or User")
    session_expiry_fixed: Optional[ClockCounter] = None
    session_expiry_inactivity: Optional[ClockCounter] = None
    permissions: Optional[StrictStr] = Field(None, description="Specify to always `allow`, `deny` access to resources, of if access is `conditional`.")
    token: Optional[StrictStr] = Field(None, description="Can only be set on create. Access Gateway Token.")
    target: Optional[StrictStr] = Field(None, description="A fully-qualified URL to the internal application including scheme, authority and path. The target host authority must be an IP address, not a hostname.")
    resources: Optional[conlist(EnforcementPointResourcesInner)] = Field(None, description="Array of resource objects")
    context_root: Optional[StrictStr] = Field(None, description="The root path to the application, often the name of the application. Can be any name, path or just a slash (“/”). The context root uniquely identifies the application within the enforcement point.")
    use_target_host_header: Optional[StrictBool] = Field(None, description="Use the target host header as opposed to the original gateway or upstream host header.")
    vhost: Optional[StrictStr] = Field(None, description="A comma-delimited list of one or more virtual hosts that map to applications assigned to the enforcement point. A VHOST may be a host name or an IP address. VHOST distinguish between applications that are at the same context root.")
    landing_page: Optional[StrictStr] = Field(None, description="The location within the context root to which the browser will be redirected for IdP-initiated single sign-on. For example, the landing page might be an index page in the context root such as index.html or default.aspx. The landing page cannot begin with a slash and must use valid URL characters.")
    case_sensitive: Optional[StrictBool] = Field(None, description="The URL path evaluation is case insensitive by default. Resources hosted on web servers such as Apache, NGINX and Java EE are case sensitive paths. Web servers such as Microsoft IIS are not case-sensitive.")
    
    # Define properties as a class variable
    _properties: ClassVar[List[str]] = ["require_sitewide_authentication", "conditions", "session_expiry_fixed", "session_expiry_inactivity", "permissions", "token", "target", "resources", "context_root", "use_target_host_header", "vhost", "landing_page", "case_sensitive"]

    @field_validator('permissions')
    @classmethod
    def permissions_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('allow', 'deny', 'conditional'):
            raise ValueError("must be one of enum values ('allow', 'deny', 'conditional')")
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
    def from_json(cls, json_str: str) -> EnforcementPoint:
        """Create an instance of EnforcementPoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "token",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of session_expiry_fixed
        if self.session_expiry_fixed:
            _dict['session_expiry_fixed'] = self.session_expiry_fixed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session_expiry_inactivity
        if self.session_expiry_inactivity:
            _dict['session_expiry_inactivity'] = self.session_expiry_inactivity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resources'] = _items
        # set to None if target (nullable) is None
        # and __fields_set__ contains the field
        if self.target is None and "target" in self.__fields_set__:
            _dict['target'] = None

        # set to None if vhost (nullable) is None
        # and __fields_set__ contains the field
        if self.vhost is None and "vhost" in self.__fields_set__:
            _dict['vhost'] = None

        # set to None if landing_page (nullable) is None
        # and __fields_set__ contains the field
        if self.landing_page is None and "landing_page" in self.__fields_set__:
            _dict['landing_page'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnforcementPoint:
        """Create an instance of EnforcementPoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnforcementPoint.parse_obj(obj)

        _obj = EnforcementPoint.parse_obj({
            "require_sitewide_authentication": obj.get("require_sitewide_authentication"),
            "conditions": obj.get("conditions"),
            "session_expiry_fixed": ClockCounter.from_dict(obj.get("session_expiry_fixed")) if obj.get("session_expiry_fixed") is not None else None,
            "session_expiry_inactivity": ClockCounter.from_dict(obj.get("session_expiry_inactivity")) if obj.get("session_expiry_inactivity") is not None else None,
            "permissions": obj.get("permissions"),
            "token": obj.get("token"),
            "target": obj.get("target"),
            "resources": [EnforcementPointResourcesInner.from_dict(_item) for _item in obj.get("resources")] if obj.get("resources") is not None else None,
            "context_root": obj.get("context_root"),
            "use_target_host_header": obj.get("use_target_host_header"),
            "vhost": obj.get("vhost"),
            "landing_page": obj.get("landing_page"),
            "case_sensitive": obj.get("case_sensitive")
        })
        return _obj

