import os
import onelogin
from onelogin.rest import ApiException
from pprint import pprint

# Change host to your domain or it will default to https://your-api-subdomain.onelogin.com
configuration = onelogin.Configuration(
    host = "https://sumit-shadow.onelogin-shadow01.com",
    username = "6c5576b0622759fcbbefe177e61be499879b4d0f5fb33a512c551f7e238c3da6",
    password = "e4c318ac6c5c2691f544c104dd534356428e8d9c0a36ed7a14da782436b486f9"
)

# configuration = onelogin.Configuration(

# )

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

    # Create an instance of the APIAuthClaimsApi
    auth_claims_api = onelogin.APIAuthClaimsApi(api_client)
    content_type = "application/json"
    
    # First, list available auth servers to get an ID
    auth_server_api = onelogin.APIAuthorizationServerApi(api_client)
    try:
        # Get list of auth servers
        auth_servers = auth_server_api.get_auth_servers(content_type=content_type)
        print("Available Auth Servers:\n")
        pprint(auth_servers)
        
        # For testing, use the first auth server ID if available
        if auth_servers and len(auth_servers) > 0:
            auth_server_id = str(auth_servers[0].id)
            
            # Create an auth claim
            auth_claim = onelogin.AuthClaim(
                name="test_claim",
                user_attribute_mappings="email"
            )
            
            try:
                # Create Auth Claim
                create_response = auth_claims_api.create_auth_claim(
                    api_auth_id=auth_server_id,
                    content_type=content_type,
                    auth_claim=auth_claim
                )
                print("Created Auth Claim with ID:\n")
                pprint(create_response)
                
                # Get the created claim ID
                claim_id = create_response
                
                # List all claims to verify creation
                try:
                    all_claims = auth_claims_api.get_authclaims(
                        api_auth_id=auth_server_id,
                        content_type=content_type
                    )
                    print("All Auth Claims:\n")
                    pprint(all_claims)
                except Exception as e:
                    print(f"Exception when listing auth claims: {e}")
                
                # Delete the auth claim
                try:
                    auth_claims_api.delete_auth_claim(
                        api_auth_id=auth_server_id,
                        claim_id=claim_id,
                        content_type=content_type
                    )
                    print(f"Successfully deleted auth claim with ID: {claim_id}")
                    
                    # Verify deletion by listing claims again
                    all_claims_after = auth_claims_api.get_authclaims(
                        api_auth_id=auth_server_id,
                        content_type=content_type
                    )
                    print("Auth Claims after deletion:\n")
                    pprint(all_claims_after)
                except Exception as e:
                    print(f"Exception when deleting auth claim: {e}")
            
            except Exception as e:
                print(f"Exception when creating auth claim: {e}")
        else:
            print("No authorization servers found to test with.")
    except Exception as e:
        print(f"Exception when getting auth servers: {e}")