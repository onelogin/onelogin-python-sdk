# GenerateMFAtokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in** | **int** | Set the duration of the token in seconds. Token expiration defaults to 259200 seconds &#x3D; 72 hours. 72 hours is the max value. | [optional] 
**reusable** | **bool** | Defines if the token is reusable multiple times within the expiry window. Value defaults to false. If set to true, token can be used multiple times, until it expires. | [optional] [default to False]

## Example

```python
from onelogin.models.generate_mf_atoken_request import GenerateMFAtokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateMFAtokenRequest from a JSON string
generate_mf_atoken_request_instance = GenerateMFAtokenRequest.from_json(json)
# print the JSON string representation of the object
print GenerateMFAtokenRequest.to_json()

# convert the object into a dict
generate_mf_atoken_request_dict = generate_mf_atoken_request_instance.to_dict()
# create an instance of GenerateMFAtokenRequest from a dict
generate_mf_atoken_request_form_dict = generate_mf_atoken_request.from_dict(generate_mf_atoken_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


