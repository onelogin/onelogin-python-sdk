# coding: utf-8

"""
    OneLogin API Python SDK

    Official Python SDK for the OneLogin API
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, StrictInt, StrictStr
from onelogin.models.brand_logo_urls import BrandLogoUrls

class BrandLogo(BaseModel):
    """
    BrandLogo
    """
    urls: BrandLogoUrls = ...
    file_size: StrictInt = ...
    updated_at: StrictStr = ...
    content_type: StrictStr = ...
    __properties = ["urls", "file_size", "updated_at", "content_type"]

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
    def from_json(cls, json_str: str) -> BrandLogo:
        """Create an instance of BrandLogo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of urls
        if self.urls:
            _dict['urls'] = self.urls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BrandLogo:
        """Create an instance of BrandLogo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BrandLogo.parse_obj(obj)

        _obj = BrandLogo.parse_obj({
            "urls": BrandLogoUrls.from_dict(obj.get("urls")) if obj.get("urls") is not None else None,
            "file_size": obj.get("file_size"),
            "updated_at": obj.get("updated_at"),
            "content_type": obj.get("content_type")
        })
        return _obj

