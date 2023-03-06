# OauthToken


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
from onelogin.models.oauth_token import OauthToken

# TODO update the JSON string below
json = "{}"
# create an instance of OauthToken from a JSON string
oauth_token_instance = OauthToken.from_json(json)
# print the JSON string representation of the object
print OauthToken.to_json()

# convert the object into a dict
oauth_token_dict = oauth_token_instance.to_dict()
# create an instance of OauthToken from a dict
oauth_token_form_dict = oauth_token.from_dict(oauth_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


