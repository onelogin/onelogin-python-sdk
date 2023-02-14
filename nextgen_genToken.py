from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = "cfc5f210a3df4e84eeb617e501fa18cb12396fbf33ab399de9026cb39fca7d55",
    password = "8e3f649203a48c95d8bd042369bb8f8367a2660ac1452372df7e010ac7452bb5"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OAuth2Api(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    generate_token_request = {"grant_type":"client_credentials"} # GenerateTokenRequest | Request Body to Generate OAuth Token

    try:
        # Generate Token
        api_response = api_instance.generate_token(content_type, generate_token_request)
        print("The response of OAuth2Api->generate_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2Api->generate_token: %s\n" % e)

with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get Event Types
        api_response = api_instance.get_event_types(content_type=content_type)
        print("The response of EventsApi->get_event_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event_types: %s\n" % e)