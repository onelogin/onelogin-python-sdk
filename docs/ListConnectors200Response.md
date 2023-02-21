# ListConnectors200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Connectors unique ID in OneLogin. | [optional] 
**name** | **str** | Name of Connector | [optional] 
**icon_url** | **str** | A link to the icon&#39;s url. | [optional] 
**auth_method** | **int** | An ID indicating the type of app. See above for possible values. | [optional] 
**allows_new_parameters** | **bool** | Indicates if apps created using this connector will be allowed to create custom parameters. | [optional] 

## Example

```python
from onelogin.models.list_connectors200_response import ListConnectors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListConnectors200Response from a JSON string
list_connectors200_response_instance = ListConnectors200Response.from_json(json)
# print the JSON string representation of the object
print ListConnectors200Response.to_json()

# convert the object into a dict
list_connectors200_response_dict = list_connectors200_response_instance.to_dict()
# create an instance of ListConnectors200Response from a dict
list_connectors200_response_form_dict = list_connectors200_response.from_dict(list_connectors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


