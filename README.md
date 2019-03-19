# OneLogin Python SDK

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

You'll need a OneLogin account and a set of API credentials before you get started. 

If you don't have an account you can [sign up for a free developer account here](https://www.onelogin.com/developer-signup).

|||
|---|---|
|client_id|Required: A valid OneLogin API client_id|   
|client_secret|Required: A valid OneLogin API client_secret|   
|region| Optional: `us` or `eu`. Defaults to `us`   |   

```python
from onelogin.api.client import OneLoginClient

client = OneLoginClient(
    client_id, 
    client_secret,
    region
)

# Now you can make requests
client.get_users()
```

For all methods see Pydoc of this SDK published at:
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

# Get all Apps in a OneLogin account
apps = client.get_apps()

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

# Enroll an Authentication Factor
enroll_factor = client.enroll_factor(user_id, auth_factors[0].id, 'My Device', '+14156456830')

# Get Enrolled Authentication Factors
otp_devices = client.get_enrolled_factors(user_id)
 
# Activate an Authentication Factor
device_id = 0000000
enrollment_response = client.activate_factor(user_id, device_id)

# Verify an Authentication Factor
result = client.verify_factor(user_id, device_id, otp_token="4242342423")

# Remove an Auth Factor
result = client.remove_factor(user_id, device_id)

# Generate Invite Link
url_link = client.generate_invite_link("user@example.com")

# Send Invite Link
sent = client.send_invite_link("user@example.com")

# Get Apps to Embed for a User
embed_token = "30e256c101cd0d2e731de1ec222e93c4be8a1572"
apps = client.get_embed_apps("30e256c101cd0d2e731de1ec222e93c4be8a1572", "user@example.com")

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

After checking out the repo, run `pip setup install` or `python setup.py develop` to install dependencies. Then, run `pip setup test` to run the tests.

Alternatively run `pip install -r requirements-test.txt` and then run `nosetests` from the project's root directory.

To release a new version, update the version number in `src/onelogin/api/version.py` and commit it, then you will be able to update it to pypy.
with `python setup.py sdist upload` and `python setup.py bdist_wheel upload`.
Create also a relase tag on github.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/onelogin/onelogin-python-sdk. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the OneLogin Python SDK project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/onelogin/onelogin-python-sdk/blob/master/CODE_OF_CONDUCT.md).
