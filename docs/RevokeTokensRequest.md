# RevokeTokensRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Set to the access token you want to revoke. This access token must have been generated using the client_id and client_secret provided in the Authorization header. | 

## Example

```python
from openapi_client.models.revoke_tokens_request import RevokeTokensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeTokensRequest from a JSON string
revoke_tokens_request_instance = RevokeTokensRequest.from_json(json)
# print the JSON string representation of the object
print RevokeTokensRequest.to_json()

# convert the object into a dict
revoke_tokens_request_dict = revoke_tokens_request_instance.to_dict()
# create an instance of RevokeTokensRequest from a dict
revoke_tokens_request_form_dict = revoke_tokens_request.from_dict(revoke_tokens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


