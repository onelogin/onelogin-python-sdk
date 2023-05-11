# EnforcementPoint

For apps that connect to a OneLogin Access Enforcement Point the following enforcement_point object will be included with the app payload.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_sitewide_authentication** | **bool** | Require user authentication to access any resource protected by this enforcement point. | [optional] 
**conditions** | **str** | If access is conditional, the conditions that must evaluate to true to allow access to a resource. For example, to require the user must be authenticated and have either the role Admin or User | [optional] 
**session_expiry_fixed** | [**ClockCounter**](ClockCounter.md) |  | [optional] 
**session_expiry_inactivity** | [**ClockCounter**](ClockCounter.md) |  | [optional] 
**permissions** | **str** | Specify to always &#x60;allow&#x60;, &#x60;deny&#x60; access to resources, of if access is &#x60;conditional&#x60;. | [optional] 
**token** | **str** | Can only be set on create. Access Gateway Token. | [optional] [readonly] 
**target** | **str** | A fully-qualified URL to the internal application including scheme, authority and path. The target host authority must be an IP address, not a hostname. | [optional] 
**resources** | [**List[EnforcementPointResourcesInner]**](EnforcementPointResourcesInner.md) | Array of resource objects | [optional] 
**context_root** | **str** | The root path to the application, often the name of the application. Can be any name, path or just a slash (“/”). The context root uniquely identifies the application within the enforcement point. | [optional] 
**use_target_host_header** | **bool** | Use the target host header as opposed to the original gateway or upstream host header. | [optional] 
**vhost** | **str** | A comma-delimited list of one or more virtual hosts that map to applications assigned to the enforcement point. A VHOST may be a host name or an IP address. VHOST distinguish between applications that are at the same context root. | [optional] 
**landing_page** | **str** | The location within the context root to which the browser will be redirected for IdP-initiated single sign-on. For example, the landing page might be an index page in the context root such as index.html or default.aspx. The landing page cannot begin with a slash and must use valid URL characters. | [optional] 
**case_sensitive** | **bool** | The URL path evaluation is case insensitive by default. Resources hosted on web servers such as Apache, NGINX and Java EE are case sensitive paths. Web servers such as Microsoft IIS are not case-sensitive. | [optional] 

## Example

```python
from onelogin.models.enforcement_point import EnforcementPoint

# TODO update the JSON string below
json = "{}"
# create an instance of EnforcementPoint from a JSON string
enforcement_point_instance = EnforcementPoint.from_json(json)
# print the JSON string representation of the object
print EnforcementPoint.to_json()

# convert the object into a dict
enforcement_point_dict = enforcement_point_instance.to_dict()
# create an instance of EnforcementPoint from a dict
enforcement_point_form_dict = enforcement_point.from_dict(enforcement_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


