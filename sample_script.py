import os
import onelogin
from onelogin.rest import ApiException
from pprint import pprint

# Change host to your domain or it will default to https://your-api-subdomain.onelogin.com
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com",
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
    privilege = {"name":"User Helpdesk","description":"Can administer helpdesk users","privilege":{"Version":"2018-05-18","Statement":[{"Effect":"Allow","Action":["users:List","users:Get","users:Unlock","users:ResetPassword","users:GenerateTempMfaToken"],"Scope":["*"]}]}} # Privilege |  (optional)

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


    auth_servers = None
    auth_server_api = onelogin.APIAuthorizationServerApi(api_client)

    try:
        # Create a dummy auth server for testing
        auth_server = onelogin.AuthServer(
                name="Test Auth Server",
                description="This is a dummy auth server", 
                configuration= {
                     "resource_identifier": "http://myapi.com/contacts2", 
                    "audiences": ["http://myapi.com/contacts2"]
                }
            )
        # auth_server = onelogin.AuthServer(
        auth_server_response = auth_server_api.create_auth_server(
            auth_server=auth_server
        )

        pprint("The response of APIAuthorizationServerApi->create_auth_server:\n")
        pprint(auth_server_response)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->create_auth_server: %s\n" % e)
    
    try:
        # List auth servers
        auth_servers_response = auth_server_api.list_auth_servers()
        auth_servers = auth_servers_response
        print("The response of APIAuthorizationServerApi->list_auth_servers:\n")    
        pprint(auth_servers_response)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->list_auth_servers: %s\n" % e)

    try:
        # Update Auth Server
        auth_server = onelogin.AuthServer(
            id=auth_servers[0].id,
            name="Test Auth Server v3",
            description="This is a dummy auth server v3", 
        )
        
        auth_server_response = auth_server_api.update_auth_server(api_auth_id=str(auth_servers[0].id), auth_server=auth_server)
        print("The response of APIAuthorizationServerApi->update_auth_server:\n")
        pprint(auth_server_response)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->update_auth_server: %s\n" % e)

    try:
        # Delete Auth Server
        auth_server_response = auth_server_api.delete_auth_server(api_auth_id=str(auth_servers[-1].id))
        print("The response of APIAuthorizationServerApi->delete_auth_server:\n")
        pprint(auth_server_response)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->delete_auth_server: %s\n" % e)


    auth_claims = None
    auth_claims_api = onelogin.APIAuthClaimsApi(api_client)

    try:
        # Create a new claim
        claim = onelogin.AuthClaim(
            name="Dummy Claim v2", 
            user_attribute_mappings="firstname"
        )

        claim_response = auth_claims_api.create_auth_claim(api_auth_id=str(auth_servers[0].id), auth_claim=claim)
        print("The response of APIAuthClaimsApi->create_auth_claim:\n")
        pprint(claim_response)
    except Exception as e:
        print("Exception when calling APIAuthClaimsApi->create_auth_claim: %s\n" % e)

    try:
        #List Auth Claim by ID
        auth_claims_response = auth_claims_api.get_authclaims(api_auth_id=str(auth_servers[0].id))
        auth_claims = auth_claims_response
        print("The response of APIAuthClaimsApi->get_authclaims:\n")
        pprint(auth_claims_response)
    except Exception as e:
        print("Exception when calling APIAuthClaimsApi->get_authclaims: %s\n" % e)

    try:
        # Update claim
        auth_claims_response = auth_claims_api.update_claim(api_auth_id=str(auth_servers[0].id), claim_id=auth_claims[1].id, auth_claim=onelogin.AuthClaim(name="Test Claim v1"))
        print("The response of APIAuthClaimsApi->update_claim:\n")
        pprint(auth_claims_response)
    except Exception as e:
        print("Exception when calling APIAuthClaimsApi->update_claim: %s\n" % e)

    try:
        # Delete Claim
        auth_claims_response = auth_claims_api.delete_auth_claim(api_auth_id=str(auth_servers[0].id), claim_id=auth_claims[1].id)
        print("The response of APIAuthClaimsApi->delete_claim:\n")
        pprint(auth_claims_response)
    except Exception as e:
        print("Exception when calling APIAuthClaimsApi->delete_claim: %s\n" % e)