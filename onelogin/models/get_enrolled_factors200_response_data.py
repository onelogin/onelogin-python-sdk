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
from pydantic import BaseModel, conlist
from onelogin.models.get_enrolled_factors200_response_data_otp_devices_inner import GetEnrolledFactors200ResponseDataOtpDevicesInner

class GetEnrolledFactors200ResponseData(BaseModel):
    """
    GetEnrolledFactors200ResponseData
    """
    otp_devices: Optional[conlist(GetEnrolledFactors200ResponseDataOtpDevicesInner)] = None
    __properties = ["otp_devices"]

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
    def from_json(cls, json_str: str) -> GetEnrolledFactors200ResponseData:
        """Create an instance of GetEnrolledFactors200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in otp_devices (list)
        _items = []
        if self.otp_devices:
            for _item in self.otp_devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['otp_devices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetEnrolledFactors200ResponseData:
        """Create an instance of GetEnrolledFactors200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetEnrolledFactors200ResponseData.parse_obj(obj)

        _obj = GetEnrolledFactors200ResponseData.parse_obj({
            "otp_devices": [GetEnrolledFactors200ResponseDataOtpDevicesInner.from_dict(_item) for _item in obj.get("otp_devices")] if obj.get("otp_devices") is not None else None
        })
        return _obj

