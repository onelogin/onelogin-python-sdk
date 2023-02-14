# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from openapi_client.models.create_app_request_one_of1_configuration import CreateAppRequestOneOf1Configuration
from openapi_client.models.create_app_request_one_of1_parameters import CreateAppRequestOneOf1Parameters

class CreateAppRequestOneOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    connector_id: StrictInt = ...
    name: StrictStr = ...
    description: StrictStr = ...
    visible: StrictBool = ...
    policy_id: StrictInt = ...
    configuration: CreateAppRequestOneOf1Configuration = ...
    parameters: CreateAppRequestOneOf1Parameters = ...
    __properties = ["connector_id", "name", "description", "visible", "policy_id", "configuration", "parameters"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateAppRequestOneOf1:
        """Create an instance of CreateAppRequestOneOf1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateAppRequestOneOf1:
        """Create an instance of CreateAppRequestOneOf1 from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateAppRequestOneOf1.parse_obj(obj)

        _obj = CreateAppRequestOneOf1.parse_obj({
            "connector_id": obj.get("connector_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "visible": obj.get("visible"),
            "policy_id": obj.get("policy_id"),
            "configuration": CreateAppRequestOneOf1Configuration.from_dict(obj.get("configuration")) if obj.get("configuration") is not None else None,
            "parameters": CreateAppRequestOneOf1Parameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None
        })
        return _obj

