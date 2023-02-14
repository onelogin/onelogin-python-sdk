# GetScopes401Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | HTTP error code https://developer.mozilla.org/en-US/docs/Web/HTTP/Status | [optional] 
**name** | **str** | Error Code Name | [optional] 
**message** | **str** | Description of Error | [optional] 

## Example

```python
from openapi_client.models.get_scopes401_response import GetScopes401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetScopes401Response from a JSON string
get_scopes401_response_instance = GetScopes401Response.from_json(json)
# print the JSON string representation of the object
print GetScopes401Response.to_json()

# convert the object into a dict
get_scopes401_response_dict = get_scopes401_response_instance.to_dict()
# create an instance of GetScopes401Response from a dict
get_scopes401_response_form_dict = get_scopes401_response.from_dict(get_scopes401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


