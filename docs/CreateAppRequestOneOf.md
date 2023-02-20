# CreateAppRequestOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**visible** | **bool** |  | 
**policy_id** | **int** |  | 
**configuration** | [**CreateAppRequestOneOfConfiguration**](CreateAppRequestOneOfConfiguration.md) |  | 

## Example

```python
from openapi_client.models.create_app_request_one_of import CreateAppRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppRequestOneOf from a JSON string
create_app_request_one_of_instance = CreateAppRequestOneOf.from_json(json)
# print the JSON string representation of the object
print CreateAppRequestOneOf.to_json()

# convert the object into a dict
create_app_request_one_of_dict = create_app_request_one_of_instance.to_dict()
# create an instance of CreateAppRequestOneOf from a dict
create_app_request_one_of_form_dict = create_app_request_one_of.from_dict(create_app_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


