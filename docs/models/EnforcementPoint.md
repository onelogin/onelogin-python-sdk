# onelogin.model.enforcement_point.EnforcementPoint

For apps that connect to a OneLogin Access Enforcement Point the following enforcement_point object will be included with the app payload.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | For apps that connect to a OneLogin Access Enforcement Point the following enforcement_point object will be included with the app payload. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**require_sitewide_authentication** | bool,  | BoolClass,  | Require user authentication to access any resource protected by this enforcement point. | [optional] 
**conditions** | str,  | str,  | If access is conditional, the conditions that must evaluate to true to allow access to a resource. For example, to require the user must be authenticated and have either the role Admin or User | [optional] 
**session_expiry_fixed** | [**ClockCounter**](ClockCounter.md) | [**ClockCounter**](ClockCounter.md) |  | [optional] 
**session_expiry_inactivity** | [**ClockCounter**](ClockCounter.md) | [**ClockCounter**](ClockCounter.md) |  | [optional] 
**permissions** | str,  | str,  | Specify to always &#x60;allow&#x60;, &#x60;deny&#x60; access to resources, of if access is &#x60;conditional&#x60;. | [optional] must be one of ["allow", "deny", "conditional", ] 
**token** | str,  | str,  | Can only be set on create. Access Gateway Token. | [optional] 
**target** | None, str,  | NoneClass, str,  | A fully-qualified URL to the internal application including scheme, authority and path. The target host authority must be an IP address, not a hostname. | [optional] 
**[resources](#resources)** | list, tuple,  | tuple,  | Array of resource objects | [optional] 
**context_root** | str,  | str,  | The root path to the application, often the name of the application. Can be any name, path or just a slash (“/”). The context root uniquely identifies the application within the enforcement point. | [optional] 
**use_target_host_header** | bool,  | BoolClass,  | Use the target host header as opposed to the original gateway or upstream host header. | [optional] 
**vhost** | None, str,  | NoneClass, str,  | A comma-delimited list of one or more virtual hosts that map to applications assigned to the enforcement point. A VHOST may be a host name or an IP address. VHOST distinguish between applications that are at the same context root. | [optional] 
**landing_page** | None, str,  | NoneClass, str,  | The location within the context root to which the browser will be redirected for IdP-initiated single sign-on. For example, the landing page might be an index page in the context root such as index.html or default.aspx. The landing page cannot begin with a slash and must use valid URL characters. | [optional] 
**case_sensitive** | bool,  | BoolClass,  | The URL path evaluation is case insensitive by default. Resources hosted on web servers such as Apache, NGINX and Java EE are case sensitive paths. Web servers such as Microsoft IIS are not case-sensitive. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# resources

Array of resource objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of resource objects | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**is_path_regex** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**require_auth** | bool,  | BoolClass,  |  | [optional] 
**permission** | str,  | str,  |  | [optional] must be one of ["allow", "deny", "conditions", ] 
**conditions** | str,  | str,  | required if permission &#x3D;&#x3D; \&quot;conditions\&quot; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

