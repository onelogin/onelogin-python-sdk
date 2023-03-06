# RiskUser

An Object containing User details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the user. | 
**name** | **str** | A name for the user. | [optional] 
**authenticated** | **bool** | Indicates if the metadata supplied in this event should be considered as trusted for the user. | [optional] [default to False]

## Example

```python
from onelogin.models.risk_user import RiskUser

# TODO update the JSON string below
json = "{}"
# create an instance of RiskUser from a JSON string
risk_user_instance = RiskUser.from_json(json)
# print the JSON string representation of the object
print RiskUser.to_json()

# convert the object into a dict
risk_user_dict = risk_user_instance.to_dict()
# create an instance of RiskUser from a dict
risk_user_form_dict = risk_user.from_dict(risk_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


