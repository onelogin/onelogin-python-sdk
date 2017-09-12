# OneLogin's Python SDK

This SDK will let you execute all the API methods, version/1, described
at https://developers.onelogin.com/api-docs/1/getting-started/dev-overview.

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

### Pydoc

Pydoc of this SDK is published at:
https://onelogin.github.io/onelogin-python-sdk/index.html


### Settings

SDK settings are stored in a file named *onelogin.sdk.ini*. A template can be found at *src/* folder.

The SDK has 3 settings parameters:
* onelogin.sdk.client_id  Onelogin OAuth2 client ID
* onelogin.sdk.client_secret  Onelogin OAuth2 client secret
* onelogin.sdk.instance  Indicates where the instance is hosted. Possible values: 'us' or 'eu'.

Read more about Onelogin API credentials at:
https://developers.onelogin.com/api-docs/1/getting-started/working-with-api-credentials


### Errors and exceptions

Onelogin's API can return 400, 401, 403 or 404 when there was any issue executing the action. When that happens, the methods of the SDK will include error and errorMessage in the OneLoginClient. Use the getError() and the getErrorDescription() to retrieve them.


### How it works

Following there is Python code that executes calls on all the available methods on the SDK.

It assumes that there are 2 users on the OL instance: 'user@example.com' and other with MFA enabled 'usermfa@example.com' and some roles, custom attributes and groups defined.

```python
#!/usr/bin/python

import os

from onelogin.api.client import OneLoginClient


current_dir_path = os.path.dirname(os.path.abspath(__file__))
client = OneLoginClient(current_dir_path)

# Get an AccessToken
token = client.get_access_token()

# Refresh an AccessToken
token2 = client.regenerate_token()

# Revoke an AccessToken
token3 = client.revoke_token()

# By default methods call internally to getAccessToken()
# if there is not valid access_token

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

# Get Users with limit
query_parameters = {
    "limit": 3
}
users_filtered_limited = client.get_users(query_parameters)

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
roles = client.get_roles();

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

# Sets Password by ID Using Cleartext
password = "Aa765431-XxX"
result = client.set_password_using_clear_text(user.id, password, password);

# Sets Password by ID Using Salt and SHA-256
password = "Aa765432-YyY";
salt = "11xxxx1";
import hashlib
hashed_salted_password = hashlib.sha256(salt + password).hexdigest()
result = client.set_password_using_hash_salt(user_mfa.id, hashed_salted_password, hashed_salted_password, "salt+sha256", salt);

 Set Custom Attribute Value to User
customAttributes = {
    custom_global_attributes[0]: "xxxx",
    custom_global_attributes[1]: "yyyy"
}
result = client.set_custom_attribute_to_user(34687020, customAttributes);

# Log Out User
result = client.log_user_out(user.id);

# Lock User
result = client.lock_user(user.id, 5);

# Get User apps
apps = client.get_user_apps(user.id)

# Get User Roles
role_ids = client.get_user_roles(user.id)

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

# Create Session Login Token
session_login_token_params = {
    "username_or_email": "user@example.com",
    "password": "Aa765431-XxX",
    "subdomain": "example-onelogin-subdomain"
}
session_token_data = client.create_session_login_token(session_login_token_params);

# Create Session Login Token MFA , after verify
session_login_token_mfa_params = {
    "username_or_email": "usermfa@example.com",
    "password": "Aa765432-YyY",
    "subdomain": "example-onelogin-subdomain"
}
session_token_mfa_data = client.create_session_login_token(session_login_token_mfa_params)
otp_token = "000000"; // We may take that value from OTP device
session_token_data2 = client.get_session_token_verified(session_token_mfa_data.devices[0].id, session_token_mfa_data.state_token, otp_token);

# Get EventTypes
event_types = client.get_event_types()

# Get Events
events = client.get_events()

query_events_params = {
    'limit': 2
}
events_limited = client.get_events(query_events_params)

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
query_events_params = array(
  "user_id": "00000000"
);
events = client.get_events(query_events_params);

# Get Groups
groups = client.get_groups()

# Get Group
group = client.get_group(groups[0].id)

# Get SAMLResponse directly
app_id = "000000"
saml_endpoint_response = client.get_saml_assertion("user@example.com", "Aa765431-XxX", app_id, "example-onelogin-subdomain");

# Get SAMLResponse after MFA
saml_endpoint_response2 = client.get_saml_assertion("usermfa@example.com", "Aa765432-YyY", app_id, "example-onelogin-subdomain");
mfa = saml_endpoint_response2.mfa
otp_token = "000000";
saml_endpoint_response_after_verify = client.get_saml_assertion_verifying(app_id, mfa.devices[0].id, mfa.state_token, "78395727", None);

# Generate Invite Link
url_link = client.generate_invite_link("user@example.com")

# Send Invite Link
sent = client.send_invite_link("user@example.com")

#Get Apps to Embed for a User
embed_token = "30e256c101cd0d2e731de1ec222e93c4be8a1572"
apps = client.get_embed_apps("30e256c101cd0d2e731de1ec222e93c4be8a1572", "user@example.com")
```
