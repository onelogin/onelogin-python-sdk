import os
import onelogin
from onelogin.rest import ApiException
from onelogin.models.generic_app import GenericApp
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
    
    app_id = "<int_app_id>" # Replace with your app ID
    app_instance = onelogin.AppsApi(api_client)

    try:
        # List Apps
        api_response = app_instance.list_apps()
        print("The response of AppsApi->get_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)

    try:
        # Get App by ID
        api_response = app_instance.get_app(app_id=app_id)
        print("The response of AppsApi->get_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)

    try:
        # Update App
        api_response = app_instance.update_app(app_id=app_id, request_body={"visible": False})
        print("The response of AppsApi->update_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->update_app: %s\n" % e)

    # try:
    #     # Delete App
    #     api_response = app_instance.delete_app(app_id=app_id)
    #     print("The response of AppsApi->delete_app:\n")
    #     pprint(api_response)
    # except Exception as e:
    #     print("Exception when calling AppsApi->delete_app: %s\n" % e)

    try:
        # Get App Users
        api_response = app_instance.get_app_users(app_id=app_id)
        print("The response of AppsApi->get_app_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_users: %s\n" % e)