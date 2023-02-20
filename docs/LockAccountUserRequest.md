# LockAccountUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locked_until** | **int** | Set to the number of minutes for which you want to lock the user account. Set to 0 if you want to lock the user account based on the Lock effective period set in the policy assigned to the user. If no policy is assigned to the user, setting this value to 0 will lock the user’s account until you unlock it Note that this value can not be less time that the Lock Effective Period specified on a user policy. | 

## Example

```python
from openapi_client.models.lock_account_user_request import LockAccountUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LockAccountUserRequest from a JSON string
lock_account_user_request_instance = LockAccountUserRequest.from_json(json)
# print the JSON string representation of the object
print LockAccountUserRequest.to_json()

# convert the object into a dict
lock_account_user_request_dict = lock_account_user_request_instance.to_dict()
# create an instance of LockAccountUserRequest from a dict
lock_account_user_request_form_dict = lock_account_user_request.from_dict(lock_account_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


