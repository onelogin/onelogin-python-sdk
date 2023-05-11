# PrivilegePrivilegeStatementInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Set to “Allow.” By default, all actions are denied, this Statement allows the listed actions to be executed. | 
**action** | **List[str]** | An array of strings that represent actions within OneLogin. Actions are prefixed with the class of object they are related to and followed by a specific action for the given class. e.g. users:List, where the class is users and the specific action is List. Don’t mix classes within an Action array. To create a privilege that includes multiple different classes, create multiple statements. A wildcard * that includes all actions is supported. Use wildcards to create a Super User privilege. | 
**scope** | **List[str]** | Target the privileged action against specific resources with the scope. The scope pattern is the class of object used by the Action, followed by an ID that represents a resource in OneLogin. e.g. apps/1234, where apps is the class and 1234 is the ID of an app. The wildcard * is supported and indicates that all resources of the class type declared, in the Action, are in scope. The Action and Scope classes must match. However, there is an exception, a scope of roles/{role_id} can be combined with Actions on the user or app class. The exception allows you to target groups of users or apps with specific actions. | 

## Example

```python
from onelogin.models.privilege_privilege_statement_inner import PrivilegePrivilegeStatementInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegePrivilegeStatementInner from a JSON string
privilege_privilege_statement_inner_instance = PrivilegePrivilegeStatementInner.from_json(json)
# print the JSON string representation of the object
print PrivilegePrivilegeStatementInner.to_json()

# convert the object into a dict
privilege_privilege_statement_inner_dict = privilege_privilege_statement_inner_instance.to_dict()
# create an instance of PrivilegePrivilegeStatementInner from a dict
privilege_privilege_statement_inner_form_dict = privilege_privilege_statement_inner.from_dict(privilege_privilege_statement_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


