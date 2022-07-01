# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.onelogin_app import OneLoginApp
import unittest
import datetime
from dateutil.tz import tzutc

class OneLogin_API_OneLogin_App_Test(unittest.TestCase):

    apps_v1_payload = {"id":1056931,"connector_id":78887,"name":"Amazon Web Services (AWS) Multi Account","extension":False,"icon":"https://s3.amazonaws.com/onelogin-assets/images/icons/amazonwebservicesmultiaccount.png","visible":True,"provisioning":False}

    apps_v2_payload = {"visible":True,"id":1056931,"auth_method":2,"name":"Amazon Web Services (AWS) Multi Account","description":"","updated_at":"2020-01-07T12:22:11.566Z","connector_id":78887,"created_at":"2020-01-07T12:22:11.566Z","auth_method_description":"SAML2.0"}

    app_v2_payload = {"description":"","parameters":{"saml_username":{"provisioned_entitlements":False,"label":"Amazon Username","default_values":None,"id":160730,"user_attribute_macros":None,"attributes_transformations":"none","user_attribute_mappings":"email","skip_if_blank":False,"values":None},"https://aws.amazon.com/SAML/Attributes/Role":{"provisioned_entitlements":False,"label":"Role","default_values":None,"id":160731,"user_attribute_macros":None,"attributes_transformations":"amazon_roles","user_attribute_mappings":"none","skip_if_blank":False,"values":None},"https://aws.amazon.com/SAML/Attributes/RoleSessionName":{"provisioned_entitlements":False,"label":"RoleSessionName","default_values":None,"id":160732,"user_attribute_macros":None,"attributes_transformations":"none","user_attribute_mappings":"email","skip_if_blank":False,"values":None}},"auth_method_description":"SAML2.0","id":1056931,"visible":True,"login_config":0,"icon_url":"https://cdn.onelogin.com/images/icons/square/amazonwebservicesmultiaccount/original.png?1475019733","role_ids":[285779],"name":"Amazon Web Services (AWS) Multi Account","connector_id":78887,"sso":{"metadata_url":"https://app.onelogin.com/saml/metadata/e6ad18d7-e5f5-436d-8fa6-5af06e285359","issuer":"https://app.onelogin.com/saml/metadata/e6ad18d7-e5f5-436d-8fa6-5af06e285359","certificate":{"id":310778,"name":"Standard Strength Certificate (2048-bit)","value":"-----BEGIN CERTIFICATE-----\\nMIID5TCCAs2gAwIBAgIUOY8Yypt1qMfdmwccZi/mHbHjDs0wDQYJKoZIhvcNAQEF\\nBQAwSDETMBEGA1UECgwKU2l4dG8gcHJvZDEVMBMGA1UECwwMT25lTG9naW4gSWRQ\\nMRowGAYDVQQDDBFPbmVMb2dpbiBBY2NvdW50IDAeFw0xOTEwMDMxNjQwNDVaFw0y\\nNDEwMDMxNjQwNDVaMEgxEzARBgNVBAoMClNpeHRvIHByb2QxFTATBgNVBAsMDE9u\\nZUxvZ2luIElkUDEaMBgGA1UEAwwRT25lTG9naW4gQWNjb3VudCAwggEiMA0GCSqG\\nSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDXeeik1w75X7ytNLsblvJIVLzA5MvPA+J4\\npok0Zj0nR3yLTcSBcpJusdYftXTMDltmb65dXivPQ3lm/NRt04kWZ8hs+4HzfoU7\\nEjabnWldG7WaOhSyaYQcVxKb+DOux9smmCj2m9Y/U11NLrgTlqVOE5oGKJh8WjZi\\nTKr08uihPC/4dneXY+TBYVbRVDhSdrdZRdTijlklArOBIEN8M24IrgXKqm/rhK54\\n+Ji85dEp0b0UTe93iDmFtsoQUOdTABDFyHU+uGVFdnjAt5FC40zKNWGEAyGxeFG2\\nydM0QqTKJzQ7Recnc2GQRtlk4IusuganT/NFJcbNN2Pogq5xiRmDAgMBAAGjgcYw\\ngcMwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUzLC1YPrVTupln4vvVmS7xayGlfAw\\ngYMGA1UdIwR8MHqAFMywtWD61U7qZZ+L71Zku8WshpXwoUykSjBIMRMwEQYDVQQK\\nDApTaXh0byBwcm9kMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxGjAYBgNVBAMMEU9u\\nZUxvZ2luIEFjY291bnQgghQ5jxjKm3Wox92bBxxmL+YdseMOzTAOBgNVHQ8BAf8E\\nBAMCB4AwDQYJKoZIhvcNAQEFBQADggEBAFllblx5PZzFFO7At8lMbDIBTJytQ8SG\\nHklIUhN9xtSWm7wSdFs8/UQbMLoi5JM52wFagispX9RB/OWsiRzWoOnRVGsq1lMs\\n7hhfMsT6KB6FGX3kzBv4xuQMDXInRwZ/vhQJ9tYT54k3+Xqot4nZFB6X1XMmW+tY\\nfpV7K/20rVog4uj7Y5cyP59u/rrnCR8C1Qx3mMhDlpGbHI6pT+MNj2VAJ52/0vmh\\nGGA1uKh6N/gCscT5bqEDQcmCeGWCs3OiwbjN+e49RIyEFsfs4Vwk/BMd8LiWlrSO\\nQvfUhCkx0uF+12OT7PJXlJyXcelHfsgsuTt6yj1b6eDrT7ZhUYRjA8I=\\n-----END CERTIFICATE-----\\n"},"acs_url":"https://sixtoprod-us.onelogin.com/trust/saml2/http-post/sso/e6ad18d7-e5f5-436d-8fa6-5af06e285359","sls_url":"https://sixtoprod-us.onelogin.com/trust/saml2/http-redirect/slo/1056931"},"configuration":{"certificate_id":310778,"external_id":None,"idp_list":None,"external_role":None,"signature_algorithm":"SHA-1"},"created_at":"2020-01-07T12:22:11.566Z","auth_method":2,"allow_assumed_signin":False,"notes":None,"provisioning":{"enabled":False,"status":"Available"},"updated_at":"2020-01-07T12:22:11.566Z","brand_id":None,"tab_id":None,"policy_id":None}

    app_v2_payload_2 = {"provisioning":{"enabled":False,"status":"Not Available"},"sso":{"client_secret":"45064cec7a487dbe28da8b6adedited6bb21b97dcedited9e56c4ce0c7f139e","client_id":"043c7280-4c0d-edited-0a9cc8ac984edited10"},"updated_at":"2020-06-12T23:39:18.023Z","icon_url":"/images/missing_connector_icon/square/original.png","notes":"","parameters":{"groups":{"attributes_transformations":"group_list","user_attribute_macros":None,"provisioned_entitlements":False,"default_values":None,"user_attribute_mappings":"member_of","id":237825,"label":"Groups","skip_if_blank":False,"values":None},"postalcode":{"attributes_transformations":None,"user_attribute_macros":"","provisioned_entitlements":False,"default_values":None,"user_attribute_mappings":"custom_attribute_postalcode","id":347099,"label":"postalcode","skip_if_blank":False,"values":None},"countrycode":{"attributes_transformations":None,"user_attribute_macros":"","provisioned_entitlements":False,"default_values":None,"user_attribute_mappings":"custom_attribute_countrycode","id":347098,"label":"countrycode","skip_if_blank":False,"values":None}},"tab_id":310191,"description":"","id":1101579,"brand_id":None,"name":"App Example 1","created_at":"2020-03-19T12:42:28.492Z","configuration":{"refresh_token_expiration_minutes":None,"access_token_expiration_minutes":None,"oidc_application_type":0,"oidc_api_version":None,"oidc_encryption_key":"","redirect_uri":"https://example.onelogin.com/oidc/2/me\\nhttps://oauth-redirect.googleusercontent.com/r/xxxx-bac44\\n","token_endpoint_auth_method":1,"post_logout_redirect_uri":None,"login_url":""},"connector_id":108419,"auth_method_description":"OpenID Connect","login_config":0,"policy_id":None,"auth_method":8,"visible":True,"allow_assumed_signin":False,"role_ids":[285779]}

    brand_apps_v2_paylad = {"id": 1455, "updated_at": "2020-09-11T19:35:08.288Z", "name": "Mom Corp", "connector_id": 3001, "auth_method_description": "SAML2.0", "description": "Mom’s Friendly Robot Company", "auth_method": 2, "created_at": "2020-09-08T22:24:19.551Z", "visible": True}

    def getTestAppsV1(self):
        test_app = OneLoginApp({})
        test_app.connector_id = 78887
        test_app.extension = False
        test_app.icon_url = "https://s3.amazonaws.com/onelogin-assets/images/icons/amazonwebservicesmultiaccount.png"
        test_app.id = 1056931
        test_app.name = "Amazon Web Services (AWS) Multi Account"
        test_app.provisioning = False
        test_app.visible = True
        return test_app

    def getTestAppsV2(self):
        test_app = OneLoginApp({})
        test_app.allow_assumed_signin = None
        test_app.auth_method = 2
        test_app.auth_method_description = "SAML2.0"
        test_app.brand_id = None
        test_app.configuration = None
        test_app.connector_id = 78887
        test_app.created_at = datetime.datetime(2020, 1, 7, 12, 22, 11, 566000, tzinfo=tzutc())
        test_app.description = ""
        test_app.icon_url = None
        test_app.id = 1056931
        test_app.name = "Amazon Web Services (AWS) Multi Account"
        test_app.notes = None
        test_app.parameters = None
        test_app.policy_id = None
        test_app.role_ids = None
        test_app.tab_id = None
        test_app.updated_at = datetime.datetime(2020, 1, 7, 12, 22, 11, 566000, tzinfo=tzutc())
        test_app.visible = True
        return test_app

    def getTestAppV2(self):
        test_app = OneLoginApp({})
        test_app.allow_assumed_signin = None
        test_app.auth_method = 2
        test_app.auth_method_description = "SAML2.0"
        test_app.brand_id = None
        test_app.configuration = None
        test_app.connector_id = 78887
        test_app.created_at = datetime.datetime(2020, 1, 7, 12, 22, 11, 566000, tzinfo=tzutc())
        test_app.description = ""
        test_app.icon_url = None
        test_app.id = 1056931
        test_app.name = "Amazon Web Services (AWS) Multi Account"
        test_app.notes = None
        test_app.parameters = None
        test_app.policy_id = None
        test_app.role_ids = None
        test_app.tab_id = None
        test_app.updated_at = datetime.datetime(2020, 1, 7, 12, 22, 11, 566000, tzinfo=tzutc())
        test_app.visible = True
        return test_app

    def getTestAppV2_2(self):
        test_app = OneLoginApp({})
        test_app.allow_assumed_signin = False
        test_app.auth_method = 8
        test_app.auth_method_description = "OpenID Connect"
        test_app.brand_id = None
        test_app.configuration = {'refresh_token_expiration_minutes': None, 'token_endpoint_auth_method': 1, 'oidc_api_version': None, 'access_token_expiration_minutes': None, 'post_logout_redirect_uri': None, 'oidc_encryption_key': '', 'redirect_uri': 'https://example.onelogin.com/oidc/2/me\\nhttps://oauth-redirect.googleusercontent.com/r/xxxx-bac44\\n', 'login_url': '', 'oidc_application_type': 0}
        test_app.connector_id = 108419
        test_app.created_at = datetime.datetime(2020, 3, 19, 12, 42, 28, 492000, tzinfo=tzutc())
        test_app.description = ""
        test_app.icon_url = "/images/missing_connector_icon/square/original.png"
        test_app.id = 1101579
        test_app.name = "App Example 1"
        test_app.notes = ""
        test_app.parameters = {'groups': {'values': None, 'user_attribute_macros': None, 'default_values': None, 'label': 'Groups', 'user_attribute_mappings': 'member_of', 'id': 237825, 'skip_if_blank': False, 'provisioned_entitlements': False, 'attributes_transformations': 'group_list'}, 'postalcode': {'values': None, 'user_attribute_macros': '', 'default_values': None, 'label': 'postalcode', 'user_attribute_mappings': 'custom_attribute_postalcode', 'id': 347099, 'skip_if_blank': False, 'provisioned_entitlements': False, 'attributes_transformations': None}, 'countrycode': {'values': None, 'user_attribute_macros': '', 'default_values': None, 'label': 'countrycode', 'user_attribute_mappings': 'custom_attribute_countrycode', 'id': 347098, 'skip_if_blank': False, 'provisioned_entitlements': False, 'attributes_transformations': None}}
        test_app.policy_id = None
        test_app.provisioning = {'enabled': False, 'status': 'Not Available'}
        test_app.role_ids = [285779]
        test_app.sso = {'client_secret': '45064cec7a487dbe28da8b6adedited6bb21b97dcedited9e56c4ce0c7f139e', 'client_id': '043c7280-4c0d-edited-0a9cc8ac984edited10'}
        test_app.tab_id = 310191
        test_app.updated_at = datetime.datetime(2020, 6, 12, 23, 39, 18, 23000, tzinfo=tzutc())
        test_app.visible = True
        return test_app

    def getTestBrandAppsV2(self):
        test_app = OneLoginApp({})
        test_app.allow_assumed_signin = None
        test_app.auth_method = 2
        test_app.auth_method_description = "SAML2.0"
        test_app.brand_id = None
        test_app.configuration = None
        test_app.connector_id = 3001
        test_app.created_at = datetime.datetime(2020, 9, 8, 22, 24, 19, 551000, tzinfo=tzutc())
        test_app.description = "Mom’s Friendly Robot Company"
        test_app.icon_url = None
        test_app.id = 1455
        test_app.name = "Mom Corp"
        test_app.notes = None
        test_app.parameters = None
        test_app.policy_id = None
        test_app.role_ids = None
        test_app.tab_id = None
        test_app.updated_at = datetime.datetime(2020, 9, 11, 19, 35, 8, 288000, tzinfo=tzutc())
        test_app.visible = True
        return test_app

    def testAppAttributes(self):
        """
        Tests the constructor method of the OneLoginApp class
        Build a OneLoginApp object and check if all the required expected attributes
        exist as described in the OneLoginApp Resource of the OneLogin API
        """
        app = OneLoginApp(data={})
        expected_required_attributes = ["connector_id", "icon_url", "id", "name"]

        for attr in expected_required_attributes:
            self.assertTrue(hasattr(app, attr), "OneLoginApp has no attribute '{}'".format(attr))

    def testAppsV1Payload(self):
        app = OneLoginApp(self.apps_v1_payload)
        expected_app = self.getTestAppsV1()
        self.assertEqual(app.__dict__, expected_app.__dict__)

    def testAppsV2Payload(self):
        app = OneLoginApp(self.apps_v2_payload)
        expected_app = self.getTestAppsV2()
        self.assertEqual(app.__dict__, expected_app.__dict__)

    def testAppV2Payload(self):
        app = OneLoginApp(self.apps_v2_payload)
        expected_app = self.getTestAppV2()
        self.assertEqual(app.__dict__, expected_app.__dict__)

    def testAppV2_2Payload(self):
        app = OneLoginApp(self.app_v2_payload_2)
        expected_app = self.getTestAppV2_2()
        self.assertEqual(app.__dict__, expected_app.__dict__)

    def testBrandAppsV2Payload(self):
        app = OneLoginApp(self.brand_apps_v2_paylad)
        expected_app = self.getTestBrandAppsV2()
        self.assertEqual(app.__dict__, expected_app.__dict__)
