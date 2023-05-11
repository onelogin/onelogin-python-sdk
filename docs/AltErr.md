# AltErr


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | HTTP error code https://developer.mozilla.org/en-US/docs/Web/HTTP/Status | [optional] 
**name** | **str** | Error Code Name | [optional] 
**message** | **str** | Description of Error | [optional] 

## Example

```python
from onelogin.models.alt_err import AltErr

# TODO update the JSON string below
json = "{}"
# create an instance of AltErr from a JSON string
alt_err_instance = AltErr.from_json(json)
# print the JSON string representation of the object
print AltErr.to_json()

# convert the object into a dict
alt_err_dict = alt_err_instance.to_dict()
# create an instance of AltErr from a dict
alt_err_form_dict = alt_err.from_dict(alt_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


