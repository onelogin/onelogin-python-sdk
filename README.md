# OneLogin Python SDK

## What's new on v2

v2 is backward compatible with v1, only some models where modified in order to be used for v1 and v2
at same time.

The code was deeply refactored to improve its maintainability.

The SDK v1 only was able to interact with version/1 methods, 
the SDK v2 will let you execute all the API methods available at:
- version/1, described at https://developers.onelogin.com/api-docs/1/getting-started/dev-overview.
- version/2, described at https://developers.onelogin.com/api-docs/2/getting-started/dev-overview.

It implements a flexible mechanism to decide what version use per resource
(read more about this at the [Getting Started](https://github.com/onelogin/onelogin-python-sdk#getting-started) section, the `api_configuration` parameter).

It also allows you to call urls using the generic domain: api.[region].onelogin.com (that was the unique way on SDK v1) or branded domain: [subdomain].onelogin.com (read more about this at the [Getting Started](https://github.com/onelogin/onelogin-python-sdk#getting-started) section, the `subdomain` parameter).


## Installation
### Hosting
#### Github
The toolkit is hosted on github. You can download it from:
* Lastest release: https://github.com/onelogin/onelogin-python-sdk/releases/latest
* Master repo: https://github.com/onelogin/onelogin-python-sdk/tree/master

#### pypi
The toolkit is hosted in pypi, you can find the package at https://pypi.python.org/pypi/onelogin

You can install it executing:
```
$ pip install onelogin
```

If you want to know how a project can handle python packages review this [guide](https://packaging.python.org/en/latest/tutorial.html) and review this [sampleproject](https://github.com/pypa/sampleproject)


### Dependencies
onelogin-python-sdk works on Python2 or Python 3. It has the following dependencies:

* requests
* defusedxml
* python-dateutil


## Getting started

You'll need a OneLogin account and a set of API credentials before you get started. 

If you don't have an account you can [sign up for a free developer account here](https://www.onelogin.com/developer-signup).

|||
|---|---|
|client_id|Required: A valid OneLogin API client_id|   
|client_secret|Required: A valid OneLogin API client_secret|   
|region| Optional: `us` or `eu`. Defaults to `us`|
|subdomain| Optional: A valid OneLogin subdomain. When provided the API endpoint calls gonna be done to the specific subdomain `<subdomain>.onelogin.com` instead to `api.<region>.onelogin.com`|
|api_configuration| Optional. The SDK by default sets a fixed version per resource. Use this parameter to override the default values.

```python
from onelogin.api.client import OneLoginClient

client = OneLoginClient(
    client_id, 
    client_secret,
    region
)

or

client = OneLoginClient(
    client_id, 
    client_secret,
    subdomain=subdomain
)

# Now you can make requests
client.get_users()
```

If you want to fix user, group and role resources to use the version/1 API,
do the following:

```python
from onelogin.api.client import OneLoginClient

api_configuration = {
    "user": 1,
    "group": 1,
    "role": 1
}

client = OneLoginClient(
    client_id, 
    client_secret,
    region,
    api_configuration=api_configuration
)
```

You can find the relation of all available endpoints/resources at [endpoints.py](https://github.com/onelogin/onelogin-python-sdk/blob/v2/src/onelogin/api/util/endpoints.py). It describes the different endpoints, its related resource and
in what version they are available. For example the `Get List of Users` API, belong the `user` resource and is available on `/1` and `/2`

```
Constants.GET_USERS_URL: {"user": [1, 2]},
```

At [client.py](https://github.com/onelogin/onelogin-python-sdk/blob/v2/src/onelogin/api/client.py#L78) you will find a `api_configuration` attribute that
set the default values that gonna be used on the SDK, if no `api_configuration` parameter is provided on client initialization to override its.

The parameters of the different methods can differ depending on the API version
enabled. Review the docs of each method that will provide detailed references for each API version

To review all methods available at the SDK, there is a Pydoc published at:
https://onelogin.github.io/onelogin-python-sdk/index.html

Is good practice to verify that the provided credentials are ok by executing
a call to client.get_access_token() after call the client constructor and verify that client.error is None after that call, which means that the client was able to fetch an access_token to execute API calls.


## Usage

### Errors and exceptions

OneLogin's API can return 400, 401, 403 or 404 when there was any issue executing the action. When that happens, the methods of the SDK will include error and errorMessage in the OneLoginClient. Review error and error_description attributes to retrieve them.

In some scenarios there is an attribute not provided or invalid that causes the error on the execution of the API call, when that happens at the OneLoginClient there is available a error_attribute that will contain the name of the attribute that caused the issue. See the API documentation to verify when this data is provided by the API.

### Authentication

By default methods call internally to `get_access_token` if there is no valid access_token. You can also get tokens etc directly if needed. 

```python
# Get an AccessToken
token = client.get_access_token()

# Refresh an AccessToken
token2 = client.regenerate_token()

# Revoke an AccessToken
is_revoked = client.revoke_token()
```

### Searches

By default a search (get_users, get_events, get_roles, get_groups) will return
a max of results determined by the client parameter max_results (1000), but
the search accept this parameter to get a different number of results.
The max_results attribute of the client can be also overriden.

### Available Methods

```python
# Build Client
from onelogin.api.client import OneLoginClient
client = OneLoginClient("client_id", "client_secret")

# Get rate limits
rate_limits = client.get_rate_limits()

# Get Custom Attributes
custom_global_attributes = client.get_custom_attributes()

# Get Users with no query parameters
users = client.get_users()

# Get Users with query parameters
query_parameters = {
    "email": "user@example.com"
}
users_filtered = client.get_users(query_parameters)

query_parameters = {
    "email": "usermfa@example.com"
}
users_filtered2 = client.get_users(query_parameters)

# Get 10 Users with role_id 2
query_parameters = {
    "role_id": 2
}
users_filtered_by_role_id = client.get_users(query_parameters, 10)

# Get User by id
user = client.get_user(users_filtered[0].id)
user_mfa = client.get_user(users_filtered2[0].id)

# Update User with specific id
user = client.get_user(user.id)
update_user_params = user.get_user_params()
update_user_params["firstname"] = 'modified_firstname'
user = client.update_user(user.id, update_user_params)
user = client.get_user(user.id)

# Get Global Roles
roles = client.get_roles()

# Get Role
role = client.get_role(roles[0].id)
role2 = client.get_role(roles[1].id)

# Assign & Remove Roles On Users
role_ids = [
    role.id,
    role2.id 
]
result = client.assign_role_to_user(user.id, role_ids)
role_ids.pop()
result = client.remove_role_from_user(user.id, role_ids)
user = client.get_user(user.id)

# Create role
new_role_id = client.create_role({"name": "New Role"})

# Update role
new_role_id = client.update_role(new_role_id, {"name": "New Role Updated"})

# Delete role
result = client.delete_role(new_role_id)

# Set applications to a role
apps = client.get_apps()
assigned_apps = client.set_role_apps(new_role_id, [apps[0].id, apps[1].id])

# List of App assigned to a role
assigned_apps = client.get_role_apps(new_role_id)

# Get Role Users (list of AssignedUser of a role)
new_assigned_users = client.get_role_users(new_role_id)

# Add Role Users
new_assigned_users = client.add_role_users(new_role_id, [users[1].id])

# Remove Role Users
result = client.remove_role_users(new_role_id, [users[1].id])

# Get Role Admins (list of AssignedAdmins of a role)
assigned_users = client.get_role_admins(new_role_id)

# Add Role Admins
new_assigned_users = client.add_role_users(new_role_id, [users[0].id])

# Remove Role Admins
result = client.remove_role_users(new_role_id, [users[0].id])


# Sets Password by ID Using Cleartext
password = "Aa765431-XxX"
result = client.set_password_using_clear_text(user.id, password, password)

# Sets Password by ID Using Salt and SHA-256
password = "Aa765432-YyY"
salt = "11xxxx1"
import hashlib
hashed_salted_password = hashlib.sha256(salt + password).hexdigest()
result = client.set_password_using_hash_salt(user_mfa.id, hashed_salted_password, hashed_salted_password, "salt+sha256", salt)

# Set Custom Attribute Value to User
customAttributes = {
    custom_global_attributes[0]: "xxxx",
    custom_global_attributes[1]: "yyyy"
}
result = client.set_custom_attribute_to_user(34687020, customAttributes)

# Log Out User
result = client.log_user_out(user.id)

# Lock User
result = client.lock_user(user.id, 5)

# Get User apps
apps = client.get_user_apps(user.id)

# Get User Roles
role_ids = client.get_user_roles(user.id)

# Generate MFA Token
mfa_token = client.generate_mfa_token(user.id)

# Connectors
connectors = client.get_connectors()

# Get all Apps in a OneLogin account
apps = client.get_apps()

# Create app
app_params = {
    "connector_id": 999999999999,
    "name": "Test app",
    "description": "Test app desc"
} 
app = client.create_app(app_params)

# Get app
app = client.get_app(app.id)

# Update app
app_params_mod = {
    "description": "Test app desc modified"
} 
app = client.update_app(app.id)

# Delete app parameter
app_parameter_id = app.parameters.items()[0][1]['id']
result = client.delete_app_parameter(app.id, app_parameter_id)

# Get users of app
users = client.get_app_users(app.id)

# Get rules of app
rules = client.get_app_rules(app.id)

# Get rule of app
rule = client.get_app_rule(app.id, rules[0].id)

# Create rule
rule_params = {
    "name": "AppRule Example",
    "enabled": True,
    "match": "all",
    "position": 1,
    "actions": [{"action": "set_nameidvalue",
                  "value": ["email"]}
    ],
    "conditions": [{"source": "last_login",
                    "operator": ">",
                    "value": "90"}
    ]
}
rule = client.create_app_rule(app.id, rule_params)

# Update rule
rule = client.update_app_rule(app.id, rule.id, {"name": "AppRule Example2"})

# List app conditions
conditions = client.get_app_conditions(app.id)

# List app condition operations
condition_ops = client.get_app_condition_operators(app.id, conditions[0]["value"])

# List app condition values
condition_values = client.get_app_condition_values(app.id, conditions[0]["value"])

# List app actions
actions = client.get_app_actions(app.id)

# List app action values
action_values = client.get_app_action_values(app.id, actions[0]["value"])

# Sort app rules
result = client.app_rule_sort(app.id, [rules[2].id, rules[0].id, rules[1].id])

# Delete rule
result = client.delete_app_rule(app.id, rule.id)

# Delete app
result = client.delete_app(app.id)

# Create user
new_user_params = {
    "email": "testcreate_1@example.com",
    "firstname": "testcreate_1_fn",
    "lastname": "testcreate_1_ln",
    "username": "testcreate_1@example.com"
}
created_user = client.create_user(new_user_params)

# Delete User
result = client.delete_user(created_user.id)

# Get EventTypes
event_types = client.get_event_types()

# Get Events
events = client.get_events()

# Get Event
event = client.get_event(events[0].id)

# Create Event
new_event_params = {
    "event_type_id": "000",
    "account_id": "00000",
    "actor_system": "00",
    "user_id": "00000000",
    "user_name": "test_event",
    "custom_message": "test creating event from python :)"
}
result = client.create_event(new_event_params)

# Get Filtered Events
query_events_params = {
  "user_id": "00000000"
}
events = client.get_events(query_events_params)

# Get Groups
groups = client.get_groups()

# Get Group
group = client.get_group(groups[0].id)

# Get SAMLResponse directly
app_id = 000000
saml_endpoint_response = client.get_saml_assertion("user@example.com", "Aa765431-XxX", app_id, "example-onelogin-subdomain")

# Get SAMLResponse after MFA
saml_endpoint_response2 = client.get_saml_assertion("usermfa@example.com", "Aa765432-YyY", app_id, "example-onelogin-subdomain")
mfa = saml_endpoint_response2.mfa
otp_token = "000000"
saml_endpoint_response_after_verify = client.get_saml_assertion_verifying(app_id, mfa.devices[0].id, mfa.state_token, "78395727", None)

# Create Session Login Token
session_login_token_params = {
    "username_or_email": "user@example.com",
    "password": "Aa765431-XxX",
    "subdomain": "example-onelogin-subdomain"
}
session_token_data = client.create_session_login_token(session_login_token_params)

# Create Session Login Token MFA , after verify
session_login_token_mfa_params = {
    "username_or_email": "usermfa@example.com",
    "password": "Aa765432-YyY",
    "subdomain": "example-onelogin-subdomain"
}
session_token_mfa_data = client.create_session_login_token(session_login_token_mfa_params)
otp_token = "000000" # We may take that value from OTP device
session_token_data2 = client.get_session_token_verified(session_token_mfa_data.devices[0].id, session_token_mfa_data.state_token, otp_token)

user_id = 00000000
# Get Available Authentication Factors
auth_factors = client.get_factors(user_id)

# Enroll an Authentication Factor Phone V1
enroll_factor = client.enroll_factor(user_id, auth_factors[0].id, 'My Device', phone='+14156456830')

# Enroll an Authentication Factor Email V2
enroll_factor2 = client.enroll_factor(user_id, auth_factors[1].id, 'My Mail', expires_in=240)

# Verify Enrollment Email
result = client.verify_enroll_factor_otp(user_id, enroll_factor2.id, "otp_token")

# Verify Enrollment Voice
result = client.verify_enroll_factor_poll(user_id, enroll_factor3.id)


# Get Enrolled Authentication Factors
otp_devices = client.get_enrolled_factors(user_id)
 
# Activate an Authentication Factor
device_id = 0000000
enrollment_response = client.activate_factor(user_id, device_id)

# Verify an Authentication Factor
result = client.verify_factor(user_id, device_id, otp_token="4242342423")

verification_id = 000000
# Verify Factor otp
result = client.verify_factor_otp(user_id, verification_id, otp="2323", device_id)

# Verify Factor poll
result = client.verify_factor_poll(user_id, verification_id) 

# Remove an Auth Factor
result = client.remove_factor(user_id, device_id)

# Generate Invite Link
url_link = client.generate_invite_link("user@example.com")

# Send Invite Link
sent = client.send_invite_link("user@example.com")

# Get Apps to Embed for a User
embed_token = "30e256c101cd0d2e731de1ec222e93c4be8a1572"
apps = client.get_embed_apps("30e256c101cd0d2e731de1ec222e93c4be8a1572", "user@example.com")

# Get Mappings
mappings = client.get_mappings()

# Get Mapping conditions
mapping_conditions = client.get_mapping_conditions()

# Get Mapping condition operator
mapping_condition_op = client.get_mapping_condition_operators(mapping_conditions[0]['value'])

# Get Mapping condition values
mapping_condition_values = client.get_mapping_condition_values(mapping_conditions[0]['value'])

# Get Mapping actions
mapping_actions = client.get_mapping_actions()

# Get Mapping action values
mapping_action_value = client.get_mapping_action_values(mapping_actions[0]['value'])

# Track an event
track_info = {"ip" : "1.2.3.4","verb" : "log-in","user_agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3)","user": {"id" : "US_112233", "name" : "Eve Smith"},"source" : {"id" : "1234","name" : "ABC Inc"},"session" : {"id" : "xxxx-xxxxx-xxxxx-xxxxx"},"device" : {"id" :"xxx-xxx-xxx"}} 
result = client.track_event(track_info)

# Get risk score
risk_score = client.get_risk_score(track_info)

# Get Score Insights
risk_score_insights = client.get_risk_score_insights()

# Get risk rules
risk_rules = client.get_risk_rules()

# Create risk rule
risk_rule_params = {"name": "IP Blacklist G", "description": "Blacklist for guest", "type": "blacklist", "target": "location.ip", "source": "guest-123", "filters": ["123.123.123.123"]}
risk_rule = client.create_risk_rule(risk_rule_params)

# Get risk rule
risk_rule = client.get_risk_rule(risk_rule.id)

# Update risk rule
updated_risk_rule = client.update_risk_rule(risk_rule.id, {"description": "Blacklist for guest user accounts"})

# Delete risk rule
result = client.update_risk_rule(risk_rule.id)

# Get Smart-Hook list
smart_hooks = client.get_smart_hooks()

# Create Smart-Hook env
env = client.create_env_var({"name": "EXAMPLE_API_KEY", "value": "xxxx-xxxx-xxxx-xxxx"})

# Create Smart-Hook
smart_hook_params = {"type": "pre-authentication","function": "","disabled": False,"runtime": "nodejs12.x","retries": 0,"timeout": 1,"options": {"risk_enabled": True,"location_enabled": False,"mfa_device_info_enabled": True},"env_vars": ["EXAMPLE_API_KEY"],"packages": {"axios": "0.21.1"},"conditions": [{"source": "roles","operator": "~", "value": "123456"}]}
smart_hook = client.create_smart_hook(smart_hook_params)

# Get Smart-Hook
smart_hook = client.get_smart_hooks(smart_hook.id)

# Update Smart-Hook
smart_hook_params["options"]["location_enabled"] = True
smart_hook = client.update_smart_hook(smart_hook.id, smart_hook_params)

# Get Smart-Hook logs
smart_hook_logs = client.get_smart_hook_logs(smart_hook.id)

# Delete Smart-Hook
result = client.delete_smart_hook(smart_hook.id)

# Get env list
envs = client.get_env_vars()

# Get env
env = client.get_env_var(env.id)

# Update env
env = client.update_env_var(env.id, "yyyy-yyyy")

# Delete env
result = client.delete_env_var(env.id)        

# Smart MFA - Validate User
validate_user_params = {
    "user_identifier": "testmfa@example.com",
    "phone": "+160000000",
    "context": {
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64)",
        "ip": "127.0.0.12"
    }
}
smart_mfa = client.validate_user(validate_user_params)

# Smart MFA - Validate MFA
state_token = smart_mfa.mfa["state_token"]
otp_token = "AB00CD"
result = client.verify_token(state_token, otp_token)

# Get Brands
brands = client.get_brands()

# Create brand
brand_params = {
    "name": "Brand example",
    "enabled": False,
    "custom_support_enabled": False
}
brand = client.create_brand(brand_params)

# Update brand
brand = client.update_brand(brand.id, {"name": "Brand example updated"})

# Get apps associated with account brand
brand_apps = client.get_brand_apps(brand.id)

# Delete brand 
brand = client.delete_brand(brand.id)

# Get Email Settings Config
email_settings = client.get_email_settings()

# Update Email Settings Config
new_email_settings = {
   "address": "smtp.sendgrid.net",
   "use_tls": True,
   "from": "email@example.com",
   "domain": "example.com",
   "user_name": "user-name",
   "password": "password",
   "port": 587
}
email_settings = client.update_email_settings(new_email_settings)

# Reset Email Settings Config 
result = client.reset_email_settings()

# Get Privileges
privileges = client.get_privileges()

# Create Privilege
name = "privilege_example"
version = "2018-05-18"

statement1 = Statement(
    "Allow",
    [
        "users:List",
        "users:Get",
    ],
    ["*"]
)
statement2 = Statement(
    "Allow",
    [
        "apps:List",
        "apps:Get",
    ],
    ["*"]
)
statements = [
    statement1,
    statement2
]
privilege = client.create_privilege(name, version, statements)

# Update Privilege
name = "privilege_example_updated"
statement2 = Statement(
    "Allow",
    [
        "apps:List",
    ],
    ["*"]
)
statements = [
    statement1,
    statement2
]
privilege = client.update_privilege(privilege.id, name, version, statements)

# Get Privilege
privileges = client.get_privilege(privilege.id)

# Delete Privilege
result = client.delete_privilege(privilege.id)

# Gets a list of the roles assigned to a privilege
assigned_roles = client.get_roles_assigned_to_privilege(privilege.id)

# Assign roles to a privilege
result = client.assign_roles_to_privilege(privilege.id, [role_id1, role_id2])

# Remove role from a privilege
result = client.remove_role_from_privilege(privilege.id, role_id_1)

# Gets a list of the users assigned to a privilege
assigned_users = client.get_users_assigned_to_privilege(privilege.id)

# Assign users to a privilege
result = client.assign_users_to_privilege(privilege.id, [user_id1, user_id2])

# Remove user from a privilege
result = client.remove_user_from_privilege(privilege.id, user_id2)
```

## Development

After checking out the repo, run `pip setup install` or `python setup.py develop` to install dependencies. Then you can run `python setup test` to run the tests.

Alternatively you can run `pip install .` or `pip install -e ".[test]"` from the project's root directory.

To release a new version, update the version number in `src/onelogin/api/version.py` and commit it, then you will be able to update it to pypy.
with `python setup.py sdist upload` and `python setup.py bdist_wheel upload`.
Create also a relase tag on github.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/onelogin/onelogin-python-sdk. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the OneLogin Python SDK project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/onelogin/onelogin-python-sdk/blob/master/CODE_OF_CONDUCT.md).
