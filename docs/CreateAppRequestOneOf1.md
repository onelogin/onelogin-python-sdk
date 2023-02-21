# CreateAppRequestOneOf1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**visible** | **bool** |  | 
**policy_id** | **int** |  | 
**configuration** | [**CreateAppRequestOneOf1Configuration**](CreateAppRequestOneOf1Configuration.md) |  | 
**parameters** | [**CreateAppRequestOneOf1Parameters**](CreateAppRequestOneOf1Parameters.md) |  | 

## Example

```python
from onelogin.models.create_app_request_one_of1 import CreateAppRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppRequestOneOf1 from a JSON string
create_app_request_one_of1_instance = CreateAppRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print CreateAppRequestOneOf1.to_json()

# convert the object into a dict
create_app_request_one_of1_dict = create_app_request_one_of1_instance.to_dict()
# create an instance of CreateAppRequestOneOf1 from a dict
create_app_request_one_of1_form_dict = create_app_request_one_of1.from_dict(create_app_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


