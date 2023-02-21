# GenerateToken200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Provides the requested access token. You can use this token to call our resource APIs. | [optional] 
**created_at** | **str** | Time at which the access token was generated. | [optional] 
**expires_in** | **int** | Indicates that the generated access token expires in 36,000 seconds, 600 minutes, or 10 hours. An expired access token cannot be used to make resource API calls, but it can still be used along with its associated refresh token to call the Refresh Tokens v2 API. | [optional] 
**refresh_token** | **str** | deprecated No longer in use | [optional] 
**token_type** | **str** | Indicates that the generated access token is a bearer token. | [optional] 
**account_id** | **int** | Account ID associated with the API credentials used to generate the token. | [optional] 

## Example

```python
from onelogin.models.generate_token200_response import GenerateToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateToken200Response from a JSON string
generate_token200_response_instance = GenerateToken200Response.from_json(json)
# print the JSON string representation of the object
print GenerateToken200Response.to_json()

# convert the object into a dict
generate_token200_response_dict = generate_token200_response_instance.to_dict()
# create an instance of GenerateToken200Response from a dict
generate_token200_response_form_dict = generate_token200_response.from_dict(generate_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


