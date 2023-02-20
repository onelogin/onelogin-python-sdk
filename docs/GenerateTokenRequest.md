# GenerateTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | Set to client_credentials. | [default to 'client_credentials']

## Example

```python
from openapi_client.models.generate_token_request import GenerateTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateTokenRequest from a JSON string
generate_token_request_instance = GenerateTokenRequest.from_json(json)
# print the JSON string representation of the object
print GenerateTokenRequest.to_json()

# convert the object into a dict
generate_token_request_dict = generate_token_request_instance.to_dict()
# create an instance of GenerateTokenRequest from a dict
generate_token_request_form_dict = generate_token_request.from_dict(generate_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


