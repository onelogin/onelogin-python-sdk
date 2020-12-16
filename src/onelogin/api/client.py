#!/usr/bin/python

""" OneLoginClient class

Copyright (c) 2017, OneLogin, Inc.
All rights reserved.

OneLoginClient class of the OneLogin's Python SDK.

"""

import datetime
from dateutil import tz
import requests
from defusedxml.ElementTree import fromstring

from onelogin.api.util.urlbuilder import UrlBuilder
from onelogin.api.util.constants import Constants
from onelogin.api.models.app import App
from onelogin.api.models.auth_factor import AuthFactor
from onelogin.api.models.event import Event
from onelogin.api.models.embed_app import EmbedApp
from onelogin.api.models.event_type import EventType
from onelogin.api.models.factor_enrollment_response import FactorEnrollmentResponse
from onelogin.api.models.group import Group
from onelogin.api.models.mfa import MFA
from onelogin.api.models.mfa_token import MFAToken
from onelogin.api.models.onelogin_app import OneLoginApp
from onelogin.api.models.onelogin_token import OneLoginToken
from onelogin.api.models.otp_device import OTP_Device
from onelogin.api.models.privilege import Privilege
from onelogin.api.models.rate_limit import RateLimit
from onelogin.api.models.role import Role
from onelogin.api.models.saml_endpoint_response import SAMLEndpointResponse
from onelogin.api.models.session_token_info import SessionTokenInfo
from onelogin.api.models.session_token_mfa_info import SessionTokenMFAInfo
from onelogin.api.models.statement import Statement
from onelogin.api.models.user import User
from onelogin.api.version import __version__


class OneLoginClient(object):
    '''

    The OneLoginClient makes the API calls to the Onelogin's platform described
    at https://developers.onelogin.com/api-docs/1/getting-started/dev-overview.

    '''

    client_id = None
    client_secret = None

    CUSTOM_USER_AGENT = "onelogin-python-sdk %s" % __version__

    def __init__(self, client_id, client_secret, region='us', max_results=1000, default_timeout=(10, 60)):
        """

        Create a new instance of OneLoginClient.

        :param client_id: API Credentials client_id
        :type client_id: string
        :param client_secret: API Credentials client_secret
        :type client_secret: string
        :param region: OneLogin region, either us or eu
        :type region: string
        :param max_results: Maximum number of results returned by list operations
        :type max_results: int
        :param default_timeout: a request timeout
        See http://docs.python-requests.org/en/master/user/advanced/#timeouts
        :type default_timeout: (float, float)

        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.max_results = max_results
        self.url_builder = UrlBuilder(region)
        self.user_agent = self.CUSTOM_USER_AGENT
        self.access_token = self.refresh_token = self.expiration = None
        self.error = None
        self.error_description = None
        self.error_attribute = None
        self.requests_timeout = default_timeout

    def set_timeout(self, timeout=None):
        """

        Changes the timeout used when placing requests with the execute_call method
        :param timeout: a request timeout
        See http://docs.python-requests.org/en/master/user/advanced/#timeouts

        """
        self.requests_timeout = timeout

    def clean_error(self):
        """

        Clean any previous error registered at the client.

        """
        self.error = None
        self.error_description = None
        self.error_attribute = None

    def get_url(self, base, obj_id=None, extra_id=None):
        return self.url_builder.get_url(base, obj_id, extra_id)

    def extract_error_message_from_response(self, response):
        message = ''
        content = response.json()
        if content:
            if 'status' in content:
                status = content['status']
                if 'message' in status:
                    if isinstance(status['message'], dict):
                        if 'description' in status['message']:
                            message = status['message']['description']
                    else:
                        message = status['message']
                elif 'type' in status:
                    message = status['type']
            elif 'message' in content:
                message = content['message']
            elif 'name' in content:
                message = content['name']
        return message

    def extract_error_attribute_from_response(self, response):
        attribute = None
        content = response.json()
        if content and 'status' in content:
            status = content['status']
            if 'message' in status:
                if isinstance(status['message'], dict):
                    if 'attribute' in status['message']:
                        attribute = status['message']['attribute']
        return attribute

    def get_after_cursor(self, response):
        after_cursor = None
        content = response.json()
        if content:
            if 'pagination' in content and 'after_cursor' in content['pagination']:
                after_cursor = content['pagination']['after_cursor']
            elif 'afterCursor' in content:
                after_cursor = content['afterCursor']
        return after_cursor

    def get_before_cursor(self, response):
        before_cursor = None
        content = response.json()
        if content:
            if 'pagination' in content and 'before_cursor' in content['pagination']:
                before_cursor = content['pagination']['before_cursor']
            elif 'beforeCursor' in content:
                before_cursor = content['beforeCursor']
        return before_cursor

    def handle_session_token_response(self, response):
        session_token = None
        content = response.json()
        if content and 'status' in content and 'message' in content['status'] and 'data' in content:
            if content['status']['message'] == "Success":
                session_token = SessionTokenInfo(content['data'][0])
            elif content['status']['message'] == "MFA is required for this user":
                session_token = SessionTokenMFAInfo(content['data'][0])
            else:
                raise Exception("Status Message type not reognized: %s" % content['status']['message'])
        return session_token

    def handle_saml_endpoint_response(self, response):
        saml_endpoint_response = None
        try:
            content = response.json()
            if content and 'status' in content and 'message' in content['status'] and 'type' in content['status']:
                status_type = content['status']['type']
                status_message = content['status']['message']
                saml_endpoint_response = SAMLEndpointResponse(status_type, status_message)
                if 'data' in content:
                    if status_message == 'Success':
                        saml_endpoint_response.saml_response = content['data']
                    else:
                        mfa = MFA(content['data'][0])
                        saml_endpoint_response.mfa = mfa
        except:
            pass
        return saml_endpoint_response

    def handle_operation_response(self, response):
        result = False
        try:
            content = response.json()
            if content and isinstance(content, dict):
                if 'status' in content and 'type' in content['status'] and content['status']['type'] == "success":
                    result = True
                elif 'success' in content and content['success']:
                    result = True
        except:
            pass
        return result

    def extract_status_code_from_response(self, response):
        status_code = ''
        content = response.json()
        if content and 'statusCode' in content:
            status_code = content['statusCode']

        return status_code

    def retrieve_apps_from_xml(self, xml_content):
        root = fromstring(xml_content)
        node_list = root.findall("./app")
        attributes = {"id", "icon", "name", "provisioned", "extension_required", "personal", "login_id"}
        apps = []
        for node in node_list:
            app_data = {
                child.tag: child.text
                for child in node
                if child.tag in attributes
            }
            apps.append(EmbedApp(app_data))
        return apps

    def is_expired(self):
        return self.expiration is not None and datetime.datetime.now(tz.tzutc()) > self.expiration

    def prepare_token(self):
        if self.access_token is None:
            self.get_access_token()
        elif self.is_expired():
            self.regenerate_token()

    def remove_stored_token(self):
        self.access_token = None
        self.refresh_token = None
        self.expiration = None

    def get_headers(self, bearer=True):
        return {
            'Content-Type': 'application/json',
            'User-Agent': self.user_agent
        }

    def get_authorized_headers(self, bearer=True, headers=None):
        if bearer:
            # Removed the ":"
            authorization = "bearer %s" % self.access_token
        else:
            authorization = "client_id:%s, client_secret:%s" % (self.client_id, self.client_secret)

        if headers is None:
            headers = self.get_headers()

        headers.update({'Authorization': authorization})
        return headers

    # OAuth 2.0 Tokens Methods
    def get_access_token(self):
        """

        Generates an access token and refresh token that you may use to
        call Onelogin's API methods.

        Returns the generated OAuth Token info
        :return: OAuth Token info
        :rtype: OneLoginToken

        See https://developers.onelogin.com/api-docs/1/oauth20-tokens/generate-tokens Generate Tokens documentation.

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.TOKEN_REQUEST_URL)

            data = {
                'grant_type': 'client_credentials'
            }

            headers = self.get_authorized_headers(bearer=False)

            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                data = response.json()
                if 'status' in data:
                    self.error = str(data['status']['code'])
                    self.error_description = self.extract_error_message_from_response(response)
                else:
                    token = OneLoginToken(response.json())
                    self.access_token = token.access_token
                    self.refresh_token = token.refresh_token
                    self.expiration = token.created_at + datetime.timedelta(seconds=token.expires_in)
                    return token
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def regenerate_token(self):
        """

        Refreshing tokens provides a new set of access and refresh tokens.

        Returns the refreshed OAuth Token info
        :return: OAuth Token info
        :rtype: OneLoginToken

        See https://developers.onelogin.com/api-docs/1/oauth20-tokens/refresh-tokens Refresh Tokens documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.TOKEN_REQUEST_URL)
            headers = self.get_headers()

            data = {
                'grant_type': 'refresh_token',
                'access_token': self.access_token,
                'refresh_token': self.refresh_token
            }

            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                data = response.json()
                if 'status' in data:
                    self.error = str(data['status']['code'])
                    self.error_description = self.extract_error_message_from_response(response)
                else:
                    token = OneLoginToken(response.json())
                    self.access_token = token.access_token
                    self.refresh_token = token.refresh_token
                    self.expiration = token.created_at + datetime.timedelta(seconds=token.expires_in)
                    return token
            else:
                if response.status_code == 401:
                    self.remove_stored_token()
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def revoke_token(self):
        """

        Revokes an access token and refresh token pair.

        See https://developers.onelogin.com/api-docs/1/oauth20-tokens/revoke-tokens Revoke Tokens documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.TOKEN_REVOKE_URL)
            headers = self.get_authorized_headers(bearer=False)

            data = {
                'access_token': self.access_token,
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                self.access_token = None
                self.refresh_token = None
                self.expiration = None
                return True
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                return False
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
            return False

    def get_rate_limits(self):
        """

        Gets current rate limit details about an access token.

        Returns the rate limit info
        :return: rate limit info
        :rtype: RateLimit

        See https://developers.onelogin.com/api-docs/1/oauth20-tokens/get-rate-limit Get Rate Limit documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_RATE_URL)

            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    rate_limit = RateLimit(json_data['data'])
                    return rate_limit
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    # User Methods
    def get_users(self, query_parameters=None, max_results=None):
        """

        Gets a list of User resources.

        :param query_parameters: Parameters to filter the result of the list
        :type query_parameters: dict

        :param max_results: Limit the number of users returned (optional)
        :type max_results: int

        Returns the list of users
        :return: users list
        :rtype: list[User]

        See https://developers.onelogin.com/api-docs/1/users/get-users Get Users documentation

        """
        self.clean_error()

        if max_results is None:
            max_results = self.max_results

        try:
            url = self.get_url(Constants.GET_USERS_URL)

            users = []
            response = None
            after_cursor = None
            while (not response) or (len(users) < max_results and after_cursor):
                response = self.execute_call('get', url, params=query_parameters)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data and json_data.get('data', None):
                        for user_data in json_data['data']:
                            if user_data and len(users) < max_results:
                                users.append(User(user_data))
                            else:
                                return users
                    after_cursor = self.get_after_cursor(response)
                    if after_cursor:
                        if not query_parameters:
                            query_parameters = {}
                        query_parameters['after_cursor'] = after_cursor
                else:
                    self.error = str(response.status_code)
                    self.error_description = self.extract_error_message_from_response(response)
                    break

            return users
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_user(self, user_id):
        """

        Gets User by ID.

        :param user_id: Id of the user
        :type user_id: int

        Returns the user identified by the id
        :return: user
        :rtype: User

        See https://developers.onelogin.com/api-docs/1/users/get-user-by-id Get User by ID documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_USER_URL, user_id)

            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return User(json_data['data'][0])
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_user_apps(self, user_id):
        """

        Gets a list of apps accessible by a user, not including personal apps.

        :param user_id: Id of the user
        :type user_id: int

        Returns the apps user identified by the id
        :return: App list of the user
        :rtype: list[App]

        See https://developers.onelogin.com/api-docs/1/users/get-apps-for-user Get Apps for a User documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_APPS_FOR_USER_URL, user_id)

            apps = []
            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    for app_data in json_data['data']:
                        if app_data:
                            apps.append(App(app_data))
                return apps
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_user_roles(self, user_id):
        """

        Gets a list of role IDs that have been assigned to a user.

        :param user_id: Id of the user
        :type user_id: int

        Returns the role ids of the user identified by the id
        :return: role ids
        :rtype: list[int]

        See https://developers.onelogin.com/api-docs/1/users/get-roles-for-user Get Roles for a User documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_ROLES_FOR_USER_URL, user_id)

            role_ids = []
            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    role_ids = json_data['data'][0]
                return role_ids
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_custom_attributes(self):
        """

        Gets a list of all custom attribute fields (also known as custom user fields) that have been defined for OL account.

        Returns the custom attributes of the account
        :return: custom attribute list
        :rtype: list[str]

        See https://developers.onelogin.com/api-docs/1/users/get-custom-attributes Get Custom Attributes documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_CUSTOM_ATTRIBUTES_URL)

            custom_attributes = []
            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    custom_attributes = json_data['data'][0]
                return custom_attributes
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def create_user(self, user_params):
        """

        Creates an user

        :param user_params: User data (firstname, lastname, email, username, company,
                                       department, directory_id, distinguished_name,
                                       external_id, group_id, invalid_login_attempts,
                                       locale_code, manager_ad_id, member_of,
                                       openid_name, phone, samaccountname, title,
                                       userprincipalname)
        :type user_params: dict

        Returns the created user
        :return: user
        :rtype: User

        See https://developers.onelogin.com/api-docs/1/users/create-user Create User documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.CREATE_USER_URL)

            response = self.execute_call('post', url, json=user_params)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return User(json_data['data'][0])
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def update_user(self, user_id, user_params):
        """

        Updates an user

        :param user_id: Id of the user
        :type user_id: int

        :param user_params: User data (firstname, lastname, email, username, company,
                                       department, directory_id, distinguished_name,
                                       external_id, group_id, invalid_login_attempts,
                                       locale_code, manager_ad_id, member_of,
                                       openid_name, phone, samaccountname, title,
                                       userprincipalname)
        :type user_params: dict

        Returns the modified user
        :return: user
        :rtype: User

        See https://developers.onelogin.com/api-docs/1/users/update-user Update User by ID documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.UPDATE_USER_URL, user_id)

            response = self.execute_call('put', url, json=user_params)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return User(json_data['data'][0])
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def assign_role_to_user(self, user_id, role_ids):
        """

        Assigns Roles to User

        :param user_id: Id of the user
        :type user_id: int

        :param role_ids: List of role ids to be added
        :type user_params: integer array

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/assign-role-to-user Assign Role to User documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.ADD_ROLE_TO_USER_URL, user_id)

            data = {
                'role_id_array': role_ids
            }

            response = self.execute_call('put', url, json=data)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def remove_role_from_user(self, user_id, role_ids):
        """

        Remove Role from User

        :param user_id: Id of the user
        :type user_id: int

        :param role_ids: List of role ids to be removed
        :type role_ids: integer array

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/remove-role-from-user Remove Role from User documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.DELETE_ROLE_TO_USER_URL, user_id)

            data = {
                'role_id_array': role_ids
            }

            response = self.execute_call('put', url, json=data)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def set_password_using_clear_text(self, user_id, password, password_confirmation, validate_policy=False):
        """

        Sets Password by ID Using Cleartext

        :param user_id: Id of the user
        :type user_id: int

        :param password: Set to the password value using cleartext.
        :type password: string

        :param password_confirmation: Ensure that this value matches the password value exactly.
        :type password_confirmation: string

        :param validate_policy: Defaults to false. This will validate the password against the users OneLogin password policy..
        :type validate_policy: boolean

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/set-password-in-cleartext Set Password by ID Using Cleartext documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.SET_PW_CLEARTEXT, user_id)

            data = {
                'password': password,
                'password_confirmation': password_confirmation,
                'validate_policy': validate_policy
            }

            response = self.execute_call('put', url, json=data)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def set_password_using_hash_salt(self, user_id, password, password_confirmation, password_algorithm, password_salt=None):
        """

        Set Password by ID Using Salt and SHA-256

        :param user_id: Id of the user
        :type user_id: int

        :param password: Set to the password value using a SHA-256-encoded value.
        :type password: string

        :param password_confirmation: Ensure that this value matches the password value exactly.
        :type password_confirmation: string

        :param password_algorithm: Set to salt+sha256.
        :type password_algorithm: string

        :param password_salt: (Optional) To provide your own salt value.
        :type password_salt: string

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/set-password-using-sha-256 Set Password by ID Using Salt and SHA-256 documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.SET_PW_SALT, user_id)

            data = {
                'password': password,
                'password_confirmation': password_confirmation,
                'password_algorithm': password_algorithm
            }
            if password_salt:
                data["password_salt"] = password_salt

            response = self.execute_call('put', url, json=data)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def set_state_to_user(self, user_id, state):
        """

        Set the State for a user.

        :param user_id: Id of the user
        :type user_id: int

        :param state: Set to the state value. Valid values: 0-3
        :type state: int

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/set-state Set User State documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.SET_STATE_TO_USER_URL, user_id)

            data = {
                'state': state
            }

            response = self.execute_call('put', url, json=data)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def set_custom_attribute_to_user(self, user_id, custom_attributes):
        """

        Set Custom Attribute Value

        :param user_id: Id of the user
        :type user_id: int

        :param custom_attributes: Provide one or more key value pairs composed of the custom attribute field shortname and the value that you want to set the field to.
        :type custom_attributes: dict

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/set-custom-attribute Set Custom Attribute Value documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.SET_CUSTOM_ATTRIBUTE_TO_USER_URL, user_id)

            data = {
                'custom_attributes': custom_attributes
            }

            response = self.execute_call('put', url, json=data)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def log_user_out(self, user_id):
        """

        Log a user out of any and all sessions.

        :param user_id: Id of the user to be logged out
        :type user_id: int

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/log-user-out Log User Out documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.LOG_USER_OUT_URL, user_id)

            response = self.execute_call('put', url)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def lock_user(self, user_id, minutes):
        """

        Use this call to lock a user's account based on the policy assigned to
        the user, for a specific time you define in the request, or until you
        unlock it.

        :param user_id: Id of the user to be locked.
        :type user_id: int

        :param minutes: Set to the number of minutes for which you want to lock the user account. (0 to delegate on policy)
        :type minutes: int

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/lock-user-account Lock User Account documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.LOCK_USER_URL, user_id)

            data = {
                'locked_until': minutes
            }

            response = self.execute_call('put', url, json=data)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def delete_user(self, user_id):
        """

        Deletes an user

        :param user_id: Id of the user to be deleted
        :type user_id: int

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/users/delete-user Delete User by ID documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.DELETE_USER_URL, user_id)

            response = self.execute_call('delete', url)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    # Generate an access token for a user
    def generate_mfa_token(self, user_id, expires_in=259200, reusable=False):
        """
        Use to generate a temporary MFA token that can be used in place of other MFA tokens for a set time period.
        For example, use this token for account recovery.

        :param user_id: Id of the user
        :type user_id: int

        :param expires_in: Set the duration of the token in seconds.
                          (default: 259200 seconds = 72h) 72 hours is the max value.
        :type expires_in: int

        :param reusable: Defines if the token reusable. (default: false) If set to true, token can be used for multiple apps, until it expires.
        :type reusable: bool

        Returns a mfa token
        :return: return the object if success
        :rtype: MFAToken

        See https://developers.onelogin.com/api-docs/1/multi-factor-authentication/generate-mfa-token Generate MFA Token documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GENERATE_MFA_TOKEN_URL, user_id)

            data = {
                'expires_in': expires_in,
                'reusable': reusable
            }

            response = self.execute_call('post', url, json=data)
            if response.status_code == 201:
                json_data = response.json()
                if json_data:
                    return MFAToken(json_data)
                else:
                    self.error = self.extract_status_code_from_response(response)
                    self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]


    # Custom Login Pages
    def create_session_login_token(self, query_params, allowed_origin=''):
        """

        Generates a session login token in scenarios in which MFA may or may not be required.
        A session login token expires two minutes after creation.

        :param query_params: Query Parameters (username_or_email, password, subdomain, return_to_url,
                                               ip_address, browser_id)
        :type query_params: dict

        :param allowed_origin: Custom-Allowed-Origin-Header. Required for CORS requests only.
                               Set to the Origin URI from which you are allowed to send a request
                               using CORS.
        :type allowed_origin: string

        Returns a session token
        :return: return the object if success
        :rtype: SessionTokenInfo/SessionTokenMFAInfo

        See https://developers.onelogin.com/api-docs/1/users/create-session-login-token Create Session Login Token documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.SESSION_LOGIN_TOKEN_URL)
            headers = self.get_authorized_headers()

            if allowed_origin:
                headers.update({'Custom-Allowed-Origin-Header-1': allowed_origin})

            response = self.execute_call('post', url, headers=headers, json=query_params)

            if response.status_code == 200:
                return self.handle_session_token_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_session_token_verified(self, device_id, state_token, otp_token=None, allowed_origin='', do_not_notify=False):
        """

        Verify a one-time password (OTP) value provided for multi-factor authentication (MFA).

        :param device_id: Provide the MFA device_id you are submitting for verification.
        :type device_id: string

        :param state_token: Provide the state_token associated with the MFA device_id you are submitting for verification.
        :type state_token: string

        :param otp_token: Provide the OTP value for the MFA factor you are submitting for verification.
        :type otp_token: string

        :param allowed_origin: Required for CORS requests only. Set to the Origin URI from which you are allowed to send a request using CORS.
        :type allowed_origin: string

        :param do_not_notify: When verifying MFA via Protect Push, set this to true to stop additional push notifications being sent to the OneLogin Protect device.
        :type do_not_notify: bool

        Returns a session token
        :return: return the object if success
        :rtype: SessionTokenInfo

        See https://developers.onelogin.com/api-docs/1/users/verify-factor Verify Factor documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_TOKEN_VERIFY_FACTOR)
            headers = self.get_authorized_headers()

            if allowed_origin:
                headers.update({'Custom-Allowed-Origin-Header-1': allowed_origin})

            data = {
                'device_id': str(device_id),
                'state_token': state_token,
                'do_not_notify': do_not_notify
            }
            if otp_token:
                data['otp_token'] = otp_token

            response = self.execute_call('post', url, headers=headers, json=data)

            if response.status_code == 200:
                return self.handle_session_token_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    # Onelogin Apps Methods
    def get_apps(self, query_parameters=None, max_results=None):
        """

        Gets a list of all Apps in a OneLogin account.

        :param query_parameters: Parameters to filter the result of the list
        :type query_parameters: dict

        :param max_results: Limit the number of apps returned (optional)
        :type max_results: int

        Returns the list of apps
        :return: app list
        :rtype: list[OneLoginApp]

        See https://developers.onelogin.com/api-docs/1/apps/get-apps Get Apps documentation

        """
        self.clean_error()

        if max_results is None:
            max_results = self.max_results

        try:
            url = self.get_url(Constants.GET_APPS_URL)

            apps = []
            response = None
            after_cursor = None
            while (not response) or (len(apps) < max_results and after_cursor):
                response = self.execute_call('get', url, params=query_parameters)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data and json_data.get('data', None):
                        for app_data in json_data['data']:
                            if app_data and len(apps) < max_results:
                                apps.append(OneLoginApp(app_data))
                            else:
                                return apps

                    after_cursor = self.get_after_cursor(response)
                    if after_cursor:
                        if not query_parameters:
                            query_parameters = {}
                        query_parameters['after_cursor'] = after_cursor
                else:
                    self.error = str(response.status_code)
                    self.error_description = self.extract_error_message_from_response(response)
                    break

            return apps
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    # Role Methods
    def get_roles(self, query_parameters=None, max_results=None):
        """

        Gets a list of Role resources.

        :param query_parameters: Parameters to filter the result of the list
        :type query_parameters: dict

        :param max_results: Limit the number of roles returned (optional)
        :type max_results: int

        Returns the list of roles
        :return: role list
        :rtype: list[Role]

        See https://developers.onelogin.com/api-docs/1/roles/get-roles Get Roles documentation

        """
        self.clean_error()

        if max_results is None:
            max_results = self.max_results

        try:
            url = self.get_url(Constants.GET_ROLES_URL)

            roles = []
            response = None
            after_cursor = None
            while (not response) or (len(roles) < max_results and after_cursor):
                response = self.execute_call('get', url, params=query_parameters)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data and json_data.get('data', None):
                        for role_data in json_data['data']:
                            if role_data and len(roles) < max_results:
                                roles.append(Role(role_data))
                            else:
                                return roles

                    after_cursor = self.get_after_cursor(response)
                    if after_cursor:
                        if not query_parameters:
                            query_parameters = {}
                        query_parameters['after_cursor'] = after_cursor
                else:
                    self.error = str(response.status_code)
                    self.error_description = self.extract_error_message_from_response(response)
                    break

            return roles
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_role(self, role_id):
        """

        Gets Role by ID.

        :param role_id: Id of the Role
        :type role_id: int

        Returns the role identified by the id
        :return: role
        :rtype: Role

        See https://developers.onelogin.com/api-docs/1/roles/get-role-by-id Get Role by ID documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_ROLE_URL, role_id)

            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return Role(json_data['data'][0])
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    # Event Methods
    def get_event_types(self):
        """

        List of all OneLogin event types available to the Events API.

        Returns the list of event type
        :return: event type list
        :rtype: list[EventType]

        See https://developers.onelogin.com/api-docs/1/events/event-types Get Event Types documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_EVENT_TYPES_URL)

            event_types = []
            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    for event_type_data in json_data['data']:
                        if event_type_data:
                            event_types.append(EventType(event_type_data))
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)

            return event_types
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_events(self, query_parameters=None, max_results=None):
        """

        Gets a list of Event resources.

        :param query_parameters: Parameters to filter the result of the list
        :type query_parameters: dict

        :param max_results: Limit the number of events returned (optional)
        :type max_results: int

        Returns the list of events
        :return: event list
        :rtype: list[Event]

        See https://developers.onelogin.com/api-docs/1/events/get-events Get Events documentation

        """
        self.clean_error()

        if max_results is None:
            max_results = self.max_results

        try:
            url = self.get_url(Constants.GET_EVENTS_URL)

            events = []
            response = None
            after_cursor = None
            while (not response) or (len(events) < max_results and after_cursor):
                response = self.execute_call('get', url, params=query_parameters)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data and json_data.get('data', None):
                        for event_data in json_data['data']:
                            if event_data and len(events) < max_results:
                                events.append(Event(event_data))
                            else:
                                return events

                    after_cursor = self.get_after_cursor(response)
                    if after_cursor:
                        if not query_parameters:
                            query_parameters = {}
                        query_parameters['after_cursor'] = after_cursor
                else:
                    self.error = str(response.status_code)
                    self.error_description = self.extract_error_message_from_response(response)
                    break

            return events
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_event(self, event_id):
        """

        Gets Event by ID.

        :param role_id: Id of the Event
        :type role_id: int

        Returns the result of the operation
        :return: event
        :rtype: Event

        See https://developers.onelogin.com/api-docs/1/events/get-event-by-id Get Event by ID documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_EVENT_URL, event_id)

            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return Event(json_data['data'][0])
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def create_event(self, event_params):
        """

        Create an event in the OneLogin event log.

        :param event_params: Event data (event_type_id, account_id, actor_system,
                                         actor_user_id, actor_user_name, app_id,
                                         assuming_acting_user_id, custom_message,
                                         directory_sync_run_id, group_id, group_name,
                                         ipaddr, otp_device_id, otp_device_name,
                                         policy_id, policy_name, role_id, role_name,
                                         user_id, user_name)
        :type event_params: dict

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/events/create-event Create Event documentation

        """
        self.clean_error()
        self.prepare_token()

        try:
            url = self.get_url(Constants.CREATE_EVENT_URL)

            response = self.execute_call('post', url, json=event_params)
            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                self.error_attribute = self.extract_error_attribute_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    # Group Methods
    def get_groups(self, max_results=None):
        """

        Gets a list of Group resources (element of groups limited with the max_results parameter, or client attribute).

        :param max_results: Limit the number of groups returned (optional)
        :type max_results: int

        Returns the list of groups
        :return: group list
        :rtype: list[Group]

        See https://developers.onelogin.com/api-docs/1/groups/get-groups Get Groups documentation

        """
        self.clean_error()

        if max_results is None:
            max_results = self.max_results

        try:
            url = self.get_url(Constants.GET_GROUPS_URL)

            query_parameters = {}
            groups = []
            response = None
            after_cursor = None
            while (not response) or (len(groups) < max_results and after_cursor):
                response = self.execute_call('get', url, params=query_parameters)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data and json_data.get('data', None):
                        for group_data in json_data['data']:
                            if group_data and len(groups) < max_results:
                                groups.append(Group(group_data))
                            else:
                                return groups

                    after_cursor = self.get_after_cursor(response)
                    if after_cursor:
                        query_parameters['after_cursor'] = after_cursor
                else:
                    self.error = str(response.status_code)
                    self.error_description = self.extract_error_message_from_response(response)
                    break

            return groups
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_group(self, group_id):
        """

        Gets Group by ID.

        :param role_id: Id of the group
        :type role_id: int

        Returns the group identified by the id
        :return: group
        :rtype: Group

        See https://developers.onelogin.com/api-docs/1/groups/get-group-by-id Get Group by ID documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_GROUP_URL, group_id)

            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return Group(json_data['data'][0])
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    # SAML Assertion Methods
    def get_saml_assertion(self, username_or_email, password, app_id, subdomain, ip_address=None):
        """

        Generates a SAML Assertion.

        :param username_or_email: username or email of the OneLogin user accessing the app
        :type username_or_email: string

        :param password: Password of the OneLogin user accessing the app
        :type password: string

        :param app_id: App ID of the app for which you want to generate a SAML token
        :type app_id: integer

        :param subdomain: subdomain of the OneLogin account related to the user/app
        :type subdomain: string

        :param ip_address: whitelisted IP address that needs to be bypassed (some MFA scenarios).
        :type ip_address: string

        Returns a SAMLEndpointResponse object with an encoded SAMLResponse
        :return: true if success
        :rtype: SAMLEndpointResponse

        See https://developers.onelogin.com/api-docs/1/saml-assertions/generate-saml-assertion Generate SAML Assertion documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_SAML_ASSERTION_URL)

            data = {
                'username_or_email': username_or_email,
                'password': password,
                'app_id': app_id,
                'subdomain': subdomain,
            }

            if ip_address:
                data['ip_address'] = ip_address

            response = self.execute_call('post', url, json=data)

            if response.status_code == 200:
                return self.handle_saml_endpoint_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_saml_assertion_verifying(self, app_id, device_id, state_token, otp_token=None, url_endpoint=None, do_not_notify=False):
        """

        Verify a one-time password (OTP) value provided for a second factor when multi-factor authentication (MFA) is required for SAML authentication.

        :param app_id: App ID of the app for which you want to generate a SAML token
        :type app_id: integer

        :param devide_id: Provide the MFA device_id you are submitting for verification.
        :type subdomain: integer

        :param state_token: Provide the state_token associated with the MFA device_id you are submitting for verification.
        :type state_token: string

        :param otp_token: Provide the OTP value for the MFA factor you are submitting for verification.
        :type otp_token: string

        :param url_endpoint: Specify an url where return the response.
        :type url_endpoint: string

        :param do_not_notify: When verifying MFA via Protect Push, set this to true to stop additional push notifications being sent to the OneLogin Protect device
        :type do_not_notify: bool

        Returns a SAMLEndpointResponse object with an encoded SAMLResponse
        :return: true if success
        :rtype: SAMLEndpointResponse

        See https://developers.onelogin.com/api-docs/1/saml-assertions/verify-factor Verify Factor documentation

        """
        self.clean_error()

        try:
            if url_endpoint:
                url = url_endpoint
            else:
                url = self.get_url(Constants.GET_SAML_VERIFY_FACTOR)

            data = {
                'app_id': app_id,
                'device_id': str(device_id),
                'state_token': state_token,
                'do_not_notify': do_not_notify
            }

            if otp_token:
                data['otp_token'] = otp_token

            response = self.execute_call('post', url, json=data)

            if response.status_code == 200:
                return self.handle_saml_endpoint_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    # Multi-factor Auth Methods
    def get_factors(self, user_id):
        """

        Returns a list of authentication factors that are available for user enrollment via API.

        :param user_id: Set to the id of the user.
        :type user_id: integer

        :return: AuthFactor list
        :rtype: list[AuthFactor]

        See https://developers.onelogin.com/api-docs/1/multi-factor-authentication/available-factors Get Available Authentication Factors documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_FACTORS_URL, user_id)

            response = self.execute_call('get', url)

            auth_factors = []
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    for auth_factor_data in json_data['data']['auth_factors']:
                        if auth_factor_data:
                            auth_factors.append(AuthFactor(auth_factor_data))
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)

            return auth_factors
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def enroll_factor(self, user_id, factor_id, display_name, number):
        """

        Enroll a user with a given authentication factor.

        :param user_id: Set to the id of the user.
        :type user_id: integer

        :param factor_id: The identifier of the factor to enroll the user with.
        :type factor_id: integer

        :param display_name: A name for the users device.
        :type display_name: string

        :param number: The phone number of the user in E.164 format..
        :type number: string

        :return: MFA device
        :rtype: OTP_Device

        See https://developers.onelogin.com/api-docs/1/multi-factor-authentication/enroll-factor Enroll an Authentication Factor documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.ENROLL_FACTOR_URL, user_id)

            data = {
                'factor_id': int(factor_id),
                'display_name': display_name,
                'number': number
            }

            response = self.execute_call('post', url, json=data)

            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return OTP_Device(json_data['data'][0])
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_enrolled_factors(self, user_id):
        """

        Return a list of authentication factors registered to a particular user for multifactor authentication (MFA)

        :param user_id: Set to the id of the user.
        :type user_id: integer

        :return: OTP_Device list
        :rtype: list[OTP_Device]

        See https://developers.onelogin.com/api-docs/1/multi-factor-authentication/enrolled-factors Get Enrolled Authentication Factors documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_ENROLLED_FACTORS_URL, user_id)

            response = self.execute_call('get', url)

            otp_devices = []
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    otp_devices_data = json_data['data'].get('otp_devices', None)
                    if otp_devices_data:
                        for otp_device_data in otp_devices_data:
                            otp_devices.append(OTP_Device(otp_device_data))
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)

            return otp_devices
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def activate_factor(self, user_id, device_id):
        """

        Triggers an SMS or Push notification containing a One-Time Password (OTP)
        that can be used to authenticate a user with the Verify Factor call.

        :param user_id: Set to the id of the user.
        :type user_id: integer

        :param device_id: Set to the device_id of the MFA device.
        :type device_id: integer

        :return: Info with User Id, Device Id, and otp_device
        :rtype: FactorEnrollmentResponse

        See https://developers.onelogin.com/api-docs/1/multi-factor-authentication/activate-factor Activate an Authentication Factor documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.ACTIVATE_FACTOR_URL, user_id, device_id)

            response = self.execute_call('post', url)

            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return FactorEnrollmentResponse(json_data['data'][0])
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def verify_factor(self, user_id, device_id, otp_token=None, state_token=None):
        """

        Authenticates a one-time password (OTP) code provided by a multifactor authentication (MFA) device.

        :param user_id: Set to the id of the user.
        :type user_id: integer

        :param device_id: Set to the device_id of the MFA device.
        :type device_id: integer

        :param otp_token: OTP code provided by the device or SMS message sent to user.
                          When a device like OneLogin Protect that supports Push has
                          been used you do not need to provide the otp_token.
        :type otp_token: string

        :param state_token: The state_token is returned after a successful request
                            to Enroll a Factor or Activate a Factor.
                            MUST be provided if the needs_trigger attribute from
                            the proceeding calls is set to true.
        :type state_token: string

        :return: true if action succeed
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/multi-factor-authentication/verify-factor Verify an Authentication Factor documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.VERIFY_FACTOR_URL, user_id, device_id)

            data = {}
            if otp_token:
                data['otp_token'] = otp_token
            if state_token:
                data['state_token'] = state_token

            response = self.execute_call('post', url, json=data)

            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def remove_factor(self, user_id, device_id):
        """

        Remove an enrolled factor from a user.

        :param user_id: Set to the id of the user.
        :type user_id: integer

        :param device_id: The device_id of the MFA device.
        :type device_id: integer

        :return: true if action succeed
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/multi-factor-authentication/remove-factor Remove a Factor documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.DELETE_FACTOR_URL, user_id, device_id)

            response = self.execute_call('delete', url)

            if response.status_code == 200:
                return True
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
                return False
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    # Invite Links Methods
    def generate_invite_link(self, email):
        """

        Generates an invite link for a user that you have already created in your OneLogin account.

        :param email: Set to the email address of the user that you want to generate an invite link for.
        :type email: string

        Returns the invitation link
        :return: link
        :rtype: str

        See https://developers.onelogin.com/api-docs/1/invite-links/generate-invite-link Generate Invite Link documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GENERATE_INVITE_LINK_URL)

            data = {
                'email': email
            }

            response = self.execute_call('post', url, json=data)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and json_data.get('data', None):
                    return json_data['data'][0]
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def send_invite_link(self, email, personal_email=None):
        """

        Sends an invite link to a user that you have already created in your OneLogin account.

        :param email: Set to the email address of the user that you want to send an invite link for.
        :type email: string

        :param personal_email: If you want to send the invite email to an email other than the
                               one provided in email, provide it here. The invite link will be
                               sent to this address instead.
        :type personal_email: string

        Returns the result of the operation
        :return: True if the mail with the link was sent
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/invite-links/send-invite-link Send Invite Link documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.SEND_INVITE_LINK_URL)

            data = {
                'email': email
            }

            if personal_email:
                data['personal_email'] = personal_email

            response = self.execute_call('post', url, json=data)
            if response.status_code == 200:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    # Embed Apps Method
    def get_embed_apps(self, token, email):
        """

        Lists apps accessible by a OneLogin user.

        :param token: Provide your embedding token.
        :type token: string

        :param email: Provide the email of the user for which you want to return a list of embeddable apps.
        :type email: string

        Returns the embed apps
        :return: A list of Apps
        :rtype: list[App]

        See https://developers.onelogin.com/api-docs/1/embed-apps/get-apps-to-embed-for-a-user Get Apps to Embed for a User documentation

        """
        self.clean_error()

        try:
            url = Constants.EMBED_APP_URL

            data = {
                'token': token,
                'email': email
            }

            headers = {
                'User-Agent': self.user_agent
            }

            response = requests.get(url, headers=headers, params=data)
            if response.status_code == 200 and response.content:
                return self.retrieve_apps_from_xml(response.content)
            else:
                self.error = str(response.status_code)
                if response.content:
                    self.error_description = response.content
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    # Privilege Methods
    def get_privileges(self):
        """

        Gets a list of the Privileges created in an account.

        Returns the list of privileges
        :return: privileges list
        :rtype: list[Privilege]

        See https://developers.onelogin.com/api-docs/1/privileges/list-privileges List Privileges documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.LIST_PRIVILEGES_URL)

            privileges = []
            response = self.execute_call('get', url)
            if response.status_code == 200:
                json_data = response.json()
                if json_data:
                    for privilege_data in json_data:
                        privileges.append(Privilege(privilege_data))
                else:
                    self.error = self.extract_status_code_from_response(response)
                    self.error_description = self.extract_error_message_from_response(response)

            return privileges
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def create_privilege(self, name, version, statements):
        """

        Creates a Privilege

        :param name: The name of the privilege.
        :type name: string

        :param version: The version for the privilege schema. Set to 2018-05-18.
        :type version: string

        :param statements: A list of statements. Statement object or a dict with the keys Effect, Action and Scope
        :type statements: list[Statement] or list[dict]

        Returns the created privilege
        :return: privilege
        :rtype: Privilege

        See https://developers.onelogin.com/api-docs/1/privileges/create-privilege Create Privilege documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.CREATE_PRIVILEGE_URL)

            statement_data = []
            for statement in statements:
                if isinstance(statement, Statement):
                    statement_data.append({
                        'Effect': statement.effect,
                        'Action': statement.actions,
                        'Scope': statement.scopes

                    })
                elif isinstance(statement, dict) and 'Effect' in statement and 'Action' in statement and 'Scope' in statement:
                    statement_data.append(statement)
                else:
                    self.error = str(400)
                    self.error_description = "statements is invalid. Provide a list of statements. The statement should be an Statement object or dict with the keys Effect, Action and Scope"
                    return

            privilege_data = {
                'name': name,
                'privilege': {
                    'Version': version,
                    'Statement': statement_data
                }
            }

            response = self.execute_call('post', url, json=privilege_data)
            if response.status_code == 201:
                json_data = response.json()
                if json_data and 'id' in json_data:
                    return Privilege(json_data['id'], name, version, statements)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_privilege(self, privilege_id):
        """

        Get a Privilege

        :param privilege_id: The id of the privilege.
        :type privilege_id: string

        Returns the privilege identified by the id
        :return: privilege
        :rtype: Privilege

        See https://developers.onelogin.com/api-docs/1/privileges/get-privilege Get Privilege documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.GET_PRIVILEGE_URL, privilege_id)

            response = self.execute_call('get', url)

            if response.status_code == 200:
                json_data = response.json()
                if json_data and 'id' in json_data:
                    return Privilege(json_data)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def update_privilege(self, privilege_id, name, version, statements):
        """

        Updates a Privilege

        :param privilege_id: The id of the privilege you want to update.
        :type privilege_id: string

        :param name: The name of the privilege.
        :type name: string

        :param version: The version for the privilege schema. Set to 2018-05-18.
        :type version: string

        :param statements: A list of statements. Statement object or a dict with the keys Effect, Action and Scope
        :type statements: list[Statement] or list[dict]

        Returns the modified privilege
        :return: privilege
        :rtype: Privilege

        See https://developers.onelogin.com/api-docs/1/privileges/update-privilege Update Privilege documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.UPDATE_PRIVILEGE_URL, privilege_id)

            statement_data = []
            for statement in statements:
                if isinstance(statement, Statement):
                    statement_data.append({
                        'Effect': statement.effect,
                        'Action': statement.actions,
                        'Scope': statement.scopes
                    })
                elif isinstance(statement, dict) and 'Effect' in statement and 'Action' in statement and 'Scope' in statement:
                    statement_data.append(statement)
                else:
                    self.error = str(400)
                    self.error_description = "statements is invalid. Provide a list of statements. The statement should be an Statement object or dict with the keys Effect, Action and Scope"
                    return

            privilege_data = {
                'name': name,
                'privilege': {
                    'Version': version,
                    'Statement': statement_data,
                }
            }

            response = self.execute_call('put', url, json=privilege_data)
            if response.status_code == 200:
                json_data = response.json()
                if json_data and 'id' in json_data:
                    return Privilege(json_data['id'], name, version, statements)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def delete_privilege(self, privilege_id):
        """

        Deletes a Privilege

        :param privilege_id: The id of the privilege you want to delete.
        :type privilege_id: string

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/privileges/delete-privilege Delete Privilege documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.DELETE_PRIVILEGE_URL, privilege_id)

            response = self.execute_call('delete', url)

            if response.status_code == 204:
                return True
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def get_roles_assigned_to_privilege(self, privilege_id, max_results=None):
        """

        Gets a list of the roles assigned to a privilege.

        :param privilege_id: The id of the privilege.
        :type privilege_id: string

        :param max_results: Limit the number of roles returned (optional)
        :type max_results: int

        Returns the list of roles
        :return: role_ids list
        :rtype: list[int]

        See https://developers.onelogin.com/api-docs/1/privileges/get-roles Get Assigned Roles documentation

        """
        self.clean_error()

        if max_results is None:
            max_results = self.max_results if self.max_results > 1000 else 1000

        try:
            url = self.get_url(Constants.GET_ROLES_ASSIGNED_TO_PRIVILEGE_URL, privilege_id)

            role_ids = []
            response = None
            after_cursor = None
            query_parameters = None
            while (not response) or (len(role_ids) < max_results and after_cursor):
                response = self.execute_call('get', url, params=query_parameters)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data and 'roles' in json_data:
                        if len(role_ids) + len(json_data['roles']) < max_results:
                            role_ids += json_data['roles']
                        elif len(role_ids) + len(json_data['roles']) == max_results:
                            role_ids += json_data['roles']
                            return role_ids
                        else:
                            for role_id in json_data['roles']:
                                if len(role_ids) < max_results:
                                    role_ids.append(role_id)
                                else:
                                    return role_ids

                    after_cursor = self.get_after_cursor(response)
                    if after_cursor:
                        if not query_parameters:
                            query_parameters = {}
                        query_parameters['after_cursor'] = after_cursor
                else:
                    self.error = str(response.status_code)
                    self.error_description = self.extract_error_message_from_response(response)
                    break

            return role_ids
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def assign_roles_to_privilege(self, privilege_id, role_ids):
        """

        Assign one or more roles to a privilege.

        :param privilege_id: The id of the privilege.
        :type privilege_id: string

        :param role_ids: The ids of the roles to be assigned.
        :type role_ids: list

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/privileges/assign-role Assign Roles documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.ASSIGN_ROLES_TO_PRIVILEGE_URL, privilege_id)

            data = {
                'roles': role_ids,
            }

            response = self.execute_call('post', url, json=data)
            if response.status_code == 201:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def remove_role_from_privilege(self, privilege_id, role_id):
        """

        Removes one role from the privilege.

        :param privilege_id: The id of the privilege.
        :type privilege_id: string

        :param role_id: The id of the role to be removed.
        :type role_id: int

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/privileges/remove-role Remove Role documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.REMOVE_ROLE_FROM_PRIVILEGE_URL, privilege_id, role_id)

            response = self.execute_call('delete', url)

            if response.status_code == 204:
                return True
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def get_users_assigned_to_privilege(self, privilege_id, max_results=None):
        """

        Gets a list of the users assigned to a privilege.

        :param privilege_id: The id of the privilege.
        :type privilege_id: string

        :param max_results: Limit the number of users returned (optional)
        :type max_results: int

        Returns the list of users
        :return: user_ids list
        :rtype: list[int]

        See https://developers.onelogin.com/api-docs/1/privileges/get-users Get Assigned Users documentation

        """
        self.clean_error()

        if max_results is None:
            max_results = self.max_results if self.max_results > 1000 else 1000

        try:
            url = self.get_url(Constants.GET_USERS_ASSIGNED_TO_PRIVILEGE_URL, privilege_id)

            user_ids = []
            response = None
            after_cursor = None
            query_parameters = None
            while (not response) or (len(user_ids) < max_results and after_cursor):
                response = self.execute_call('get', url, params=query_parameters)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data and 'users' in json_data:
                        if len(user_ids) + len(json_data['users']) < max_results:
                            user_ids += json_data['users']
                        elif len(user_ids) + len(json_data['users']) == max_results:
                            user_ids += json_data['users']
                            return user_ids
                        else:
                            for user_id in json_data['users']:
                                if len(user_ids) < max_results:
                                    user_ids.append(user_id)
                                else:
                                    return user_ids

                    after_cursor = self.get_after_cursor(response)
                    if after_cursor:
                        if not query_parameters:
                            query_parameters = {}
                        query_parameters['after_cursor'] = after_cursor
                else:
                    self.error = str(response.status_code)
                    self.error_description = self.extract_error_message_from_response(response)
                    break

            return user_ids
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    def assign_users_to_privilege(self, privilege_id, user_ids):
        """

        Assign one or more users to a privilege.

        :param privilege_id: The id of the privilege.
        :type privilege_id: string

        :param user_ids: The ids of the users to be assigned.
        :type user_ids: list

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/privileges/assign-users Assign Users documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.ASSIGN_USERS_TO_PRIVILEGE_URL, privilege_id)

            data = {
                'users': user_ids,
            }

            response = self.execute_call('post', url, json=data)
            if response.status_code == 201:
                return self.handle_operation_response(response)
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def remove_user_from_privilege(self, privilege_id, user_id):
        """

        Removes one user from the privilege.

        :param privilege_id: The id of the privilege.
        :type privilege_id: string

        :param user_id: The id of the user to be removed.
        :type user_id: int

        Returns if the action succeed
        :return: true if success
        :rtype: bool

        See https://developers.onelogin.com/api-docs/1/privileges/remove-user Remove User documentation

        """
        self.clean_error()

        try:
            url = self.get_url(Constants.REMOVE_USER_FROM_PRIVILEGE_URL, privilege_id, user_id)

            response = self.execute_call('delete', url)

            if response.status_code == 204:
                return True
            else:
                self.error = str(response.status_code)
                self.error_description = self.extract_error_message_from_response(response)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    def execute_call(self, method, url, headers=None, params=None, json=None):
        self.prepare_token()

        if headers is None:
            headers = self.get_authorized_headers()

        response = None
        tries = 0
        while (tries < 2):
            if method == 'get':
                response = requests.get(url, headers=headers, params=params, timeout=self.requests_timeout)
            elif method == 'post':
                response = requests.post(url, headers=headers, json=json, timeout=self.requests_timeout)
            elif method == 'put':
                response = requests.put(url, headers=headers, json=json, timeout=self.requests_timeout)
            elif method == 'delete':
                response = requests.delete(url, headers=headers, timeout=self.requests_timeout)
            else:
                break
            if response.status_code == 504 or (response.status_code == 401 and self.extract_error_message_from_response(response) == "Unauthorized"):
                if response.status_code == 401 and self.extract_error_message_from_response(response) == "Unauthorized":
                    if tries == 1:
                        self.access_token = None
                    self.clean_error()
                    self.prepare_token()
                    headers = self.get_authorized_headers(headers=headers)

                tries += 1
            else:
                break

        return response
