import os
import onelogin
from onelogin.rest import ApiException
from pprint import pprint

# Change host to your domain or it will default to https://your-api-subdomain.onelogin.com
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com",
    username = "<client_id>",
    password = "<client_secret>"
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
        pprint(configuration.access_token)
    except Exception as e:
        print("Exception when generating access token: %s\n" % e)
    
    users = None
    user_instance = onelogin.UsersV2Api(api_client)

    try:
        # List All Users
        api_response = user_instance.list_users2()
        print("The response of UsersV2Api->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->list_users: %s\n" % e)

    try:
        # Create User
        dummy_user = {
            "email": "dummy@quest.com",
        }
        api_response = user_instance.create_user2(user=dummy_user, _headers={"Authorization": "Bearer " + configuration.access_token})
        users = api_response
        print("The response of UsersV2Api->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->create_user: %s\n" % e)

    try:
        # Get User by ID
        api_response = user_instance.get_user2(user_id=users.id)
        pprint("The response of UsersV2Api->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->get_user: %s\n" % e)

    try:
        # List User Apps
        api_response = user_instance.get_user_apps2(user_id=users.id)
        print("The response of UsersV2Api->list_user_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->list_user_apps: %s\n" % e)

    try:
        # Update User
        user_details = {"firstname": 'dummy', "lastname": 'user'}
        api_response = user_instance.update_user2(user_id=users.id, user=user_details, _headers={"Authorization": "Bearer " + configuration.access_token})
        print("The response of UsersV2Api->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->update_user: %s\n" % e)

    try:
        # Delete User
        api_response = user_instance.delete_user2(user_id=users.id)
        print("The response of UsersV2Api->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->delete_user: %s\n" % e)