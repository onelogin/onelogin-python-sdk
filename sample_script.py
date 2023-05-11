import os
import onelogin
from onelogin.rest import ApiException
from pprint import pprint

# Change host to your domain or it will default to https://your-api-subdomain.onelogin.com
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

configuration = onelogin.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    token_instance = onelogin.OAuth2Api(api_client)
    generate_token_request = {"grant_type":"client_credentials"} # GenerateTokenRequest | Request Body to Generate OAuth Token
    content_type="application/json"
    try:
        # Generate and Save Access Token
        api_response = token_instance.generate_token(generate_token_request, content_type=content_type)
        configuration.access_token = api_response.access_token
        print(configuration.access_token)
    except Exception as e:
        print("Exception when generating access token: %s\n" % e)
    
    user_instance = onelogin.UsersV2Api(api_client)
    try:
        # List Users
        api_response = user_instance.list_users2()
        print("The response of UsersV2Api->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->list_users: %s\n" % e)
    
    priv_instance = onelogin.PrivilegesApi(api_client)
    privilege = {"name":"User Helpdesk","description":"Can administer helpdesk users","privilege":{"Version":"2018-05-18","Statement":[{"Effect":"Allow","Action":["Users:List","Users:Get","Users:Unlock","Users:ResetPassword","Users:GenerateTempMfaToken"],"Scope":["*"]}]}} # Privilege |  (optional)

    try:
        # Create a Privilege
        api_response = priv_instance.create_privilege(privilege=privilege)
        print("The response of PrivilegesApi->create_privilege:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->create_privilege: %s\n" % e)
    
    privilege_instance = onelogin.PrivilegesApi(api_client)

    try:
        # List Privileges
        api_response = privilege_instance.list_privileges()
        print("The response of PrivilegesApi->list_privileges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->list_privileges: %s\n" % e)