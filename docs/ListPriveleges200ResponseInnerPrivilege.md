# ListPriveleges200ResponseInnerPrivilege


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**statement** | [**List[ListPriveleges200ResponseInnerPrivilegeStatementInner]**](ListPriveleges200ResponseInnerPrivilegeStatementInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_priveleges200_response_inner_privilege import ListPriveleges200ResponseInnerPrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of ListPriveleges200ResponseInnerPrivilege from a JSON string
list_priveleges200_response_inner_privilege_instance = ListPriveleges200ResponseInnerPrivilege.from_json(json)
# print the JSON string representation of the object
print ListPriveleges200ResponseInnerPrivilege.to_json()

# convert the object into a dict
list_priveleges200_response_inner_privilege_dict = list_priveleges200_response_inner_privilege_instance.to_dict()
# create an instance of ListPriveleges200ResponseInnerPrivilege from a dict
list_priveleges200_response_inner_privilege_form_dict = list_priveleges200_response_inner_privilege.from_dict(list_priveleges200_response_inner_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


