# RateLimit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_rate_limit_limit** | **int** | Rate Limit Limit | [optional] 
**x_rate_limit_remaining** | **int** | Rate Limit Remaining | [optional] 
**x_rate_limit_reset** | **int** | Rate Limit Reset | [optional] 

## Example

```python
from onelogin.models.rate_limit import RateLimit

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimit from a JSON string
rate_limit_instance = RateLimit.from_json(json)
# print the JSON string representation of the object
print RateLimit.to_json()

# convert the object into a dict
rate_limit_dict = rate_limit_instance.to_dict()
# create an instance of RateLimit from a dict
rate_limit_form_dict = rate_limit.from_dict(rate_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


