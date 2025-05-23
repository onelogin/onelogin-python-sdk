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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, field_validator

class User(BaseModel):
    """
    User
    """
    id: Optional[StrictInt] = None
    username: Optional[StrictStr] = Field(None, description="A username for the user.")
    email: Optional[StrictStr] = Field(None, description="A valid email for the user.")
    firstname: Optional[StrictStr] = Field(None, description="The user's first name.")
    lastname: Optional[StrictStr] = Field(None, description="The user's last name.")
    title: Optional[StrictStr] = Field(None, description="The user's job title.")
    department: Optional[StrictStr] = Field(None, description="The user's department.")
    company: Optional[StrictStr] = Field(None, description="The user's company.")
    comment: Optional[StrictStr] = Field(None, description="Free text related to the user.")
    group_id: Optional[StrictInt] = Field(None, description="The ID of the Group in OneLogin that the user is assigned to.")
    role_ids: Optional[conlist(StrictInt)] = Field(None, description="A list of OneLogin Role IDs of the user")
    phone: Optional[StrictStr] = Field(None, description="The E.164 format phone number for a user.")
    state: Optional[StrictInt] = None
    status: Optional[StrictInt] = None
    directory_id: Optional[StrictInt] = Field(None, description="The ID of the OneLogin Directory of the user.")
    trusted_idp_id: Optional[StrictInt] = Field(None, description="The ID of the OneLogin Trusted IDP of the user.")
    manager_ad_id: Optional[StrictStr] = Field(None, description="The ID of the user's manager in Active Directory.")
    manager_user_id: Optional[StrictStr] = Field(None, description="The OneLogin User ID for the user's manager.")
    samaccountname: Optional[StrictStr] = Field(None, description="The user's Active Directory username.")
    member_of: Optional[StrictStr] = Field(None, description="The user's directory membership.")
    userprincipalname: Optional[StrictStr] = Field(None, description="The principle name of the user.")
    distinguished_name: Optional[StrictStr] = Field(None, description="The distinguished name of the user.")
    external_id: Optional[StrictStr] = Field(None, description="The ID of the user in an external directory.")
    activated_at: Optional[StrictStr] = None
    last_login: Optional[StrictStr] = None
    invitation_sent_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    preferred_locale_code: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    invalid_login_attempts: Optional[StrictInt] = None
    locked_until: Optional[StrictStr] = None
    password_changed_at: Optional[StrictStr] = None
    password: Optional[StrictStr] = Field(None, description="The password to set for a user.")
    password_confirmation: Optional[StrictStr] = Field(None, description="Required if the password is being set.")
    password_algorithm: Optional[StrictStr] = Field(None, description="Use this when importing a password that's already hashed. Prepend the salt value to the cleartext password value before SHA-256-encoding it")
    salt: Optional[StrictStr] = Field(None, description="The salt value used with the password_algorithm.")
    __properties = ["id", "username", "email", "firstname", "lastname", "title", "department", "company", "comment", "group_id", "role_ids", "phone", "state", "status", "directory_id", "trusted_idp_id", "manager_ad_id", "manager_user_id", "samaccountname", "member_of", "userprincipalname", "distinguished_name", "external_id", "activated_at", "last_login", "invitation_sent_at", "updated_at", "preferred_locale_code", "created_at", "invalid_login_attempts", "locked_until", "password_changed_at", "password", "password_confirmation", "password_algorithm", "salt"]

    @field_validator('state')
    @classmethod
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0, 1, 2, 3):
            raise ValueError("must be one of enum values (0, 1, 2, 3)")
        return value

    @field_validator('status')
    @classmethod
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0, 1, 2, 3, 4, 5, 7, 8):
            raise ValueError("must be one of enum values (0, 1, 2, 3, 4, 5, 7, 8)")
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
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User.parse_obj(obj)

        _obj = User.parse_obj({
            "id": obj.get("id"),
            "username": obj.get("username"),
            "email": obj.get("email"),
            "firstname": obj.get("firstname"),
            "lastname": obj.get("lastname"),
            "title": obj.get("title"),
            "department": obj.get("department"),
            "company": obj.get("company"),
            "comment": obj.get("comment"),
            "group_id": obj.get("group_id"),
            "role_ids": obj.get("role_ids"),
            "phone": obj.get("phone"),
            "state": obj.get("state"),
            "status": obj.get("status"),
            "directory_id": obj.get("directory_id"),
            "trusted_idp_id": obj.get("trusted_idp_id"),
            "manager_ad_id": obj.get("manager_ad_id"),
            "manager_user_id": obj.get("manager_user_id"),
            "samaccountname": obj.get("samaccountname"),
            "member_of": obj.get("member_of"),
            "userprincipalname": obj.get("userprincipalname"),
            "distinguished_name": obj.get("distinguished_name"),
            "external_id": obj.get("external_id"),
            "activated_at": obj.get("activated_at"),
            "last_login": obj.get("last_login"),
            "invitation_sent_at": obj.get("invitation_sent_at"),
            "updated_at": obj.get("updated_at"),
            "preferred_locale_code": obj.get("preferred_locale_code"),
            "created_at": obj.get("created_at"),
            "invalid_login_attempts": obj.get("invalid_login_attempts"),
            "locked_until": obj.get("locked_until"),
            "password_changed_at": obj.get("password_changed_at"),
            "password": obj.get("password"),
            "password_confirmation": obj.get("password_confirmation"),
            "password_algorithm": obj.get("password_algorithm"),
            "salt": obj.get("salt")
        })
        return _obj

