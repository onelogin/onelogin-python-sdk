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
from pydantic import BaseModel, Field, StrictStr
from onelogin.models.risk_device import RiskDevice
from onelogin.models.risk_user import RiskUser
from onelogin.models.session import Session
from onelogin.models.source import Source

class GetRiskScoreRequest(BaseModel):
    """
    GetRiskScoreRequest
    """
    ip: StrictStr = Field(..., description="The IP address of the User's request.")
    user_agent: StrictStr = Field(..., description="The user agent of the User's request.")
    user: RiskUser = ...
    source: Optional[Source] = None
    session: Optional[Session] = None
    device: Optional[RiskDevice] = None
    fp: Optional[StrictStr] = Field(None, description="Set to the value of the __tdli_fp cookie.")
    __properties = ["ip", "user_agent", "user", "source", "session", "device", "fp"]

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
    def from_json(cls, json_str: str) -> GetRiskScoreRequest:
        """Create an instance of GetRiskScoreRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRiskScoreRequest:
        """Create an instance of GetRiskScoreRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRiskScoreRequest.parse_obj(obj)

        _obj = GetRiskScoreRequest.parse_obj({
            "ip": obj.get("ip"),
            "user_agent": obj.get("user_agent"),
            "user": RiskUser.from_dict(obj.get("user")) if obj.get("user") is not None else None,
            "source": Source.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "session": Session.from_dict(obj.get("session")) if obj.get("session") is not None else None,
            "device": RiskDevice.from_dict(obj.get("device")) if obj.get("device") is not None else None,
            "fp": obj.get("fp")
        })
        return _obj

