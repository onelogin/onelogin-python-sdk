# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.
import unittest

try:
    from unittest.mock import Mock  # python 3.3 and above
except ImportError:
    from mock import Mock

from onelogin.api.util.response_handlers import (get_resource_list, get_resource_or_id, get_ids,
                                               extract_error_message_from_response, extract_error_attribute_from_response,
                                               get_after_cursor, get_before_cursor, extract_status_code_from_response,
                                               handle_operation_response, handle_session_token_response, handle_saml_endpoint_response,
                                               op_create_success, op_delete_success, retrieve_apps_from_xml)
from onelogin.api.models.auth_factor import AuthFactor
from onelogin.api.models.embed_app import EmbedApp
from onelogin.api.models.event_type import EventType
from onelogin.api.models.mapping import Mapping
from onelogin.api.models.mfa import MFA
from onelogin.api.models.rate_limit import RateLimit
from onelogin.api.models.role import Role
from onelogin.api.models.saml_endpoint_response import SAMLEndpointResponse
from onelogin.api.models.session_token_info import SessionTokenInfo
from onelogin.api.models.session_token_mfa_info import SessionTokenMFAInfo
from onelogin.api.models.smart_hook import SmartHook
from onelogin.api.models.user import User


class OneLogin_API_Client_Util_ResponseHandlers(unittest.TestCase):

    def mock_response(self, json_data, headers=None, status=200):
        mock_resp = Mock()
        mock_resp.status_code = status
        mock_resp.json = Mock(
            return_value=json_data
        )
        mock_resp.headers = headers
        return mock_resp

    def testGetResourceList(self):
        json_data = {'data': [{'description': 'App %app% added to role %role%', 'id': 1, 'name': 'APP_ADDED_TO_ROLE'},
                              {'description': 'App %app% removed from role %role%', 'id': 2, 'name': 'APP_REMOVED_FROM_ROLE'},
                              {'description': '%actor_user% assumed %user%', 'id': 3, 'name': 'USER_ASSUMED_USER'},
                              {'description': 'Assigned %role% to user %user%', 'id': 4, 'name': 'USER_ASSIGNED_ROLE'},
                              {'description': '%user% logged into OneLogin', 'id': 5, 'name': 'USER_LOGGED_INTO_ONELOGIN'},
                              {'description': '%user% failed authentication', 'id': 6, 'name': 'USER_FAILED_ONELOGIN_LOGIN'}],
                     'status': {'code': 200, 'error': False, 'message': 'Success', 'type': 'success'}
        }                              
        resources = get_resource_list(EventType, json_data, None, 1)

        self.assertEqual(len(resources), 6)
        self.assertTrue(isinstance(resources[0], EventType))
        self.assertEqual(resources[0].id, 1)
        self.assertEqual(resources[0].name, "APP_ADDED_TO_ROLE")
        self.assertEqual(resources[0].description, 'App %app% added to role %role%')

        resources = get_resource_list(EventType, json_data, None, 2)
        self.assertEqual(len(resources), 0)

    def testGetResourceListWithIndex(self):
        json_data = {'data': {'auth_factors': [{'name': 'OneLogin Voice', 'factor_id': 24567}]},
                     'status': {'message': 'Success', 'type': 'success', 'error': False, 'code': 200}}
        resources = get_resource_list(AuthFactor, json_data, "auth_factors", 1)
        self.assertEqual(len(resources), 1)
        self.assertTrue(isinstance(resources[0], AuthFactor))
        self.assertEqual(resources[0].id, 24567)
        self.assertEqual(resources[0].name, 'OneLogin Voice')

        resources = get_resource_list(AuthFactor, json_data, None, 1)
        self.assertEqual(len(resources), 0)

    def testGetResourceListWithoutIndex(self):
        json_data = [{'factor_id': 24564, 'name': 'OneLogin Protect', 'auth_factor_name': 'OneLogin'},
                     {'factor_id': 32233, 'name': 'Duo Security', 'auth_factor_name': 'Duo Security'},
                     {'factor_id': 24568, 'name': 'Authenticator', 'auth_factor_name': 'Google Authenticator'},
                     {'factor_id': 43302, 'name': 'YubiKey', 'auth_factor_name': 'YubiKey'}]
        resources = get_resource_list(AuthFactor, json_data, None, 2)
        self.assertEqual(len(resources), 4)
        self.assertTrue(isinstance(resources[0], AuthFactor))
        self.assertEqual(resources[0].id, 24564)
        self.assertEqual(resources[0].name, "OneLogin Protect")
        self.assertEqual(resources[0].auth_factor_name, "OneLogin")

        resources = get_resource_list(AuthFactor, json_data, None, 1)
        self.assertEqual(len(resources), 0)

    def testGetResourceListEmptyData(self):
        resources = get_resource_list(SmartHook, None, None, 1)
        self.assertEqual(len(resources), 0)

        resources = get_resource_list(SmartHook, [], None, 1)
        self.assertEqual(len(resources), 0)

        resources = get_resource_list(SmartHook, None, None, 2)
        self.assertEqual(len(resources), 0)

        resources = get_resource_list(SmartHook, [], None, 2)
        self.assertEqual(len(resources), 0)

        resources = get_resource_list(SmartHook, [], 'index', 2)
        self.assertEqual(len(resources), 0)

    def testGetResourceOrId(self):
        data_json = None
        resource = get_resource_or_id(User, data_json, 1)
        self.assertIsNone(resource)

        data_json = None
        resource = get_resource_or_id(User, data_json, 2)
        self.assertIsNone(resource)

        data_json = {'status': {'code': 200, 'error': False, 'message': 'Success', 'type': 'success'}, 'data': [{'last_login': '2020-04-16T17:46:22.943Z', 'trusted_idp_id': None, 'distinguished_name': None, 'invalid_login_attempts': 0, 'invitation_sent_at': None, 'userprincipalname': None, 'title': '', 'manager_ad_id': None, 'updated_at': '2020-04-16T17:46:22.954Z', 'preferred_locale_code': None, 'directory_id': None, 'custom_attributes': {'loyaltylevel': '', 'postalcode': None, 'countrycode': ''}, 'comment': '', 'locale_code': None, 'activated_at': '2019-10-25T18:28:32.205Z', 'manager_user_id': None, 'firstname': 'firstname_test', 'phone': '+34000000000', 'member_of': None, 'department': '', 'password_changed_at': '2020-04-16T09:33:32.915Z', 'openid_name': 'testuser', 'external_id': None, 'group_id': None, 'company': '', 'username': '', 'created_at': '2019-10-25T18:26:34.932Z', 'samaccountname': None, 'email': 'test@example.com', 'role_id': None, 'status': 1, 'id': 60308064, 'locked_until': None, 'state': 1, 'lastname': 'lastname_test'}]}
        resource = get_resource_or_id(User, data_json, 1)
        self.assertTrue(isinstance(resource, User))
        self.assertEqual(resource.id, 60308064)
        self.assertEqual(resource.firstname, "firstname_test")
        self.assertEqual(resource.lastname, "lastname_test")
        self.assertEqual(resource.email, "test@example.com")

        data_json = {"status": {"error": False, "code": 200, "type": "success", "message": "Success"}, "data": {"X-RateLimit-Limit": 5000, "X-RateLimit-Remaining": 4988, "X-RateLimit-Reset": 832}}
        resource = get_resource_or_id(RateLimit, data_json, 1)
        self.assertTrue(isinstance(resource, RateLimit))

        data_json = {'preferred_locale_code': None, 'password_changed_at': '2020-04-16T09:33:32.915Z', 'invalid_login_attempts': 0, 'status': 1, 'locked_until': None, 'manager_user_id': None, 'firstname': 'firstname_test', 'comment': '', 'activated_at': '2019-10-25T18:28:32.205Z', 'state': 1, 'role_ids': [], 'username': '', 'phone': '+34000000000', 'directory_id': None, 'external_id': None, 'id': 60308064, 'title': '', 'company': '', 'created_at': '2019-10-25T18:26:34.932Z', 'samaccountname': None, 'member_of': None, 'invitation_sent_at': None, 'distinguished_name': None, 'group_id': None, 'department': '', 'manager_ad_id': None, 'userprincipalname': None, 'email': 'test@example.com', 'updated_at': '2020-04-16T17:46:22.954Z', 'last_login': '2020-04-16T17:46:22.943Z', 'custom_attributes': {'countrycode': '', 'postalcode': None, 'loyaltylevel': ''}, 'lastname': 'lastname_test', 'trusted_idp_id': None}
        resource = get_resource_or_id(User, data_json, 2)
        self.assertTrue(isinstance(resource, User))
        self.assertEqual(resource.id, 60308064)
        self.assertEqual(resource.firstname, "firstname_test")
        self.assertEqual(resource.lastname, "lastname_test")
        self.assertEqual(resource.email, "test@example.com")

        data_json = [{'id': 452448}]
        resource_id = get_resource_or_id(Role, data_json, 2)
        self.assertFalse(isinstance(resource_id, Role))
        self.assertTrue(isinstance(resource_id, int))

        data_json = {'id': 45244822}
        resource_id = get_resource_or_id(Mapping, data_json, 2)
        self.assertFalse(isinstance(resource_id, Mapping))
        self.assertTrue(isinstance(resource_id, int))

        data_json = [{'id': 452448}]
        resource_id = get_resource_or_id(Role, data_json, 2)
        self.assertFalse(isinstance(resource_id, User))
        self.assertTrue(isinstance(resource_id, int))

    def testGetIds(self):
        data_json = None
        result = get_ids(data_json)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(result, [])

        data_json = [{'id': 452448}]
        result = get_ids(data_json)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(result, [452448])

        data_json = [{"id": 760112}, {"id": 1029591}]
        result = get_ids(data_json)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(result, [760112, 1029591])

        data_json = [760112, 1029591]
        result = get_ids(data_json)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(result, [760112, 1029591])

    def testExtractErrorMessageFromResponse(self):
        data_json = None
        response = self.mock_response(data_json, status=400)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, '')

        data_json = {"status": {"error": True, "code": 400,"type": "bad request", "message": "grant_type is incorrect/absent"}}
        response = self.mock_response(data_json, status=400)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "grant_type is incorrect/absent")

        data_json = {"status": { "error": True, "code": 400, "type": "bad request", "message": { "description": "last is not a valid attribute for user model", "attribute": "last"}}}
        response = self.mock_response(data_json, status=400)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "last is not a valid attribute for user model")

        data_json = {"message": "Unauthorized", "statusCode": 401, "name": "UnauthorizedError"}
        response = self.mock_response(data_json, status=401)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "Unauthorized")

        data_json = {"message": "Validation failed: The associated Policy with ID 0 could not be found", "statusCode": 422, "name": "UnprocessableEntityError"}
        response = self.mock_response(data_json, status=422)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "Validation failed: The associated Policy with ID 0 could not be found")

        data_json = {"message": "Invalid sort field: created_at", "field": "created_at", "name": "UnprocessableEntityFieldError", "statusCode": 422}
        response = self.mock_response(data_json, status=422)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "Invalid sort field: created_at")

        data_json = {"code": 422, "message": "Validation Failed", "errors": [{"field": "enabled", "message": ["Required field is missing"]}]}
        response = self.mock_response(data_json, status=422)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "Validation Failed")

        data_json = {"code": 422, "message": "Validation Failed", "errors": [{"field": "enabled", "message": ["Required field is missing"]},{"field": "id", "message": ["Field is not allowed"]}]}
        response = self.mock_response(data_json, status=422)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "Validation Failed")

        data_json = {"status": {"error": True, "code": 400, "type": "bad request", "message": {"attribute": "id", "description": "ID is incorrect"}}}
        response = self.mock_response(data_json, status=400)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "ID is incorrect")

        data_json = {"message": "unknown attribute: employee_number", "name": "BadRequestError", "statusCode": 400}
        response = self.mock_response(data_json, status=400)
        message = extract_error_message_from_response(response)
        self.assertEqual(message, "unknown attribute: employee_number")

    def testExtractErrorAttributeFromResponse(self):
        data_json = None
        response = self.mock_response(data_json, status=401)
        message = extract_error_attribute_from_response(response)
        self.assertEqual(message, None)

        data_json = {"message": "Unauthorized", "statusCode": 401, "name": "UnauthorizedError"}
        response = self.mock_response(data_json, status=401)
        message = extract_error_attribute_from_response(response)
        self.assertEqual(message, None)

        data_json = {"status": { "error": True, "code": 400, "type": "bad request", "message": { "description": "last is not a valid attribute for user model", "attribute": "last"}}}
        response = self.mock_response(data_json, status=400)
        attribute = extract_error_attribute_from_response(response)
        self.assertEqual(attribute, "last")

        data_json = {"message": "Invalid sort field: created_at", "field": "created_at", "name": "UnprocessableEntityFieldError", "statusCode": 422}
        response = self.mock_response(data_json, status=422)
        message = extract_error_attribute_from_response(response)
        self.assertEqual(message, "created_at")

        data_json = {"code": 422, "message": "Validation Failed", "errors": [{"field": "enabled", "message": ["Required field is missing"]}]}
        response = self.mock_response(data_json, status=422)
        message = extract_error_attribute_from_response(response)
        self.assertEqual(message, "Field: enabled - Required field is missing")

        data_json = {"code": 422, "message": "Validation Failed", "errors": [{"field": "enabled", "message": ["Required field is missing"]},{"field": "id", "message": ["Field is not allowed"]}]}
        response = self.mock_response(data_json, status=422)
        message = extract_error_attribute_from_response(response)
        self.assertEqual(message, "Field: enabled - Required field is missing. Field: id - Field is not allowed")

        data_json = {"status": {"error": True, "code": 400, "type": "bad request", "message": {"attribute": "id", "description": "ID is incorrect"}}}
        response = self.mock_response(data_json, status=400)
        message = extract_error_attribute_from_response(response)
        self.assertEqual(message, "id")

        data_json = {"message": "unknown attribute: employee_number", "name": "BadRequestError", "statusCode": 400}
        response = self.mock_response(data_json, status=400)
        message = extract_error_attribute_from_response(response)
        self.assertEqual(message, "employee_number")

    def testGetAfterCursor(self):
        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"pagination":{"before_cursor":None,"after_cursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","previous_link":None,"next_link":"https://api.us.onelogin.com/api/1/users?after_cursor=xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ"},"data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, status=400)
        cursor = get_after_cursor(response, 1)
        self.assertEqual(cursor, "xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ")

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"pagination":{"after_cursor":None,"before_cursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","next_link":None,"previous_link":"https://api.us.onelogin.com/api/1/users?before_cursor=xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ"},"data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, status=400)
        cursor = get_after_cursor(response, 1)
        self.assertEqual(cursor, None)

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"afterCursor":None, "beforeCursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","data":[{"id":1},{"id":2}]}
        response = self.mock_response(data_json, status=400)
        cursor = get_after_cursor(response, 1)
        self.assertEqual(cursor, None)

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"beforeCursor":None, "afterCursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","data":[{"id":1},{"id":2}]}
        response = self.mock_response(data_json, status=400)
        cursor = get_after_cursor(response, 1)
        self.assertEqual(cursor, "xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ")

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"pagination":{"before_cursor":None,"after_cursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","previous_link":None,"next_link":"https://api.us.onelogin.com/api/1/users?after_cursor=xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ"},"data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, {"content-type":"json/application"}, status=400)
        cursor = get_after_cursor(response, 2)
        self.assertEqual(cursor, None)

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"pagination":{"after_cursor":None,"before_cursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","next_link":None,"previous_link":"https://api.us.onelogin.com/api/1/users?before_cursor=xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ"},"data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, {"content-type":"json/application"}, status=400)
        cursor = get_after_cursor(response, 2)
        self.assertEqual(cursor, None)

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"}, "data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, {"content-type":"json/application", 'total-count': '17', 'page-items': '10', 'after-cursor': 'bGltaXQ9MTAmcGFnZT0y', 'total-pages': '2', 'current-page': '1'}, status=400)
        cursor = get_after_cursor(response, 2)
        self.assertEqual(cursor, "bGltaXQ9MTAmcGFnZT0y")

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"}, "data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, {"content-type":"json/application", 'total-count': '17', 'page-items': '10', 'before-cursor': 'bGltaXQ9MTAmcGFnZT0x', 'total-pages': '2', 'current-page': '2'}, status=400)
        cursor = get_after_cursor(response, 2)
        self.assertEqual(cursor, None)

    def testGetBeforeCursor(self):
        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"pagination":{"before_cursor":None,"after_cursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","previous_link":None,"next_link":"https://api.us.onelogin.com/api/1/users?after_cursor=xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ"},"data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, status=400)
        cursor = get_before_cursor(response, 1)
        self.assertEqual(cursor, None)

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"pagination":{"after_cursor":None,"before_cursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","next_link":None,"previous_link":"https://api.us.onelogin.com/api/1/users?before_cursor=xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ"},"data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, status=400)
        cursor = get_before_cursor(response, 1)
        self.assertEqual(cursor, "xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ")

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"afterCursor":None, "beforeCursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","data":[{"id":1},{"id":2}]}
        response = self.mock_response(data_json, status=400)
        cursor = get_before_cursor(response, 1)
        self.assertEqual(cursor, "xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ")

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"},"beforeCursor":None, "afterCursor":"xxxxb3VudF9pZDo6Oi0tIyNpZDo6OjY3NzI0NzQ","data":[{"id":1},{"id":2}]}
        response = self.mock_response(data_json, status=400)
        cursor = get_before_cursor(response, 1)
        self.assertEqual(cursor, None)

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"}, "data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, {"content-type":"json/application", 'total-count': '17', 'page-items': '10', 'after-cursor': 'bGltaXQ9MTAmcGFnZT0y', 'total-pages': '2', 'current-page': '1'}, status=400)
        cursor = get_before_cursor(response, 2)
        self.assertEqual(cursor, None)

        data_json = {"status":{"error":False, "code":200, "type":"success", "message":"Success"}, "data":[{"id":1, "name": "C-Executive"},{"id":2, "name": "Contractor"}]}
        response = self.mock_response(data_json, {"content-type":"json/application", 'total-count': '17', 'page-items': '10', 'before-cursor': 'bGltaXQ9MTAmcGFnZT0x', 'total-pages': '2', 'current-page': '2'}, status=400)
        cursor = get_before_cursor(response, 2)
        self.assertEqual(cursor, "bGltaXQ9MTAmcGFnZT0x")

    def testExtractStatusCodeFromResponse(self):
        data_json = {"statusCode": 401, "name": "UnauthorizedError", "message": "The request requires user authentication."}
        response = self.mock_response(data_json, status=401)
        status_code = extract_status_code_from_response(response)
        self.assertEqual(status_code, 401)

        data_json = None
        response = self.mock_response(data_json, status=204)
        status_code = extract_status_code_from_response(response)
        self.assertEqual(status_code, '')

    def testHandleOperationResponse(self):
        data_json = None
        response = self.mock_response(data_json, status=400)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"status": {"error": True, "code": 400,"type": "bad request", "message": "grant_type is incorrect/absent"}}
        response = self.mock_response(data_json, status=400)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"status": { "error": True, "code": 400, "type": "bad request", "message": { "description": "last is not a valid attribute for user model", "attribute": "last"}}}
        response = self.mock_response(data_json, status=400)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"message": "Unauthorized", "statusCode": 401, "name": "UnauthorizedError"}
        response = self.mock_response(data_json, status=401)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"message": "Validation failed: The associated Policy with ID 0 could not be found", "statusCode": 422, "name": "UnprocessableEntityError"}
        response = self.mock_response(data_json, status=422)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"message": "Invalid sort field: created_at", "field": "created_at", "name": "UnprocessableEntityFieldError", "statusCode": 422}
        response = self.mock_response(data_json, status=422)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"code": 422, "message": "Validation Failed", "errors": [{"field": "enabled", "message": ["Required field is missing"]}]}
        response = self.mock_response(data_json, status=422)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"code": 422, "message": "Validation Failed", "errors": [{"field": "enabled", "message": ["Required field is missing"]},{"field": "id", "message": ["Field is not allowed"]}]}
        response = self.mock_response(data_json, status=422)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"status": {"error": True, "code": 400, "type": "bad request", "message": {"attribute": "id", "description": "ID is incorrect"}}}
        response = self.mock_response(data_json, status=400)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"message": "unknown attribute: employee_number", "name": "BadRequestError", "statusCode": 400}
        response = self.mock_response(data_json, status=400)
        result = handle_operation_response(response)
        self.assertFalse(result)

        data_json = {"status": {"error": False, "code": 200, "type": "success", "message": "Success"}, "data": [{}]}
        response = self.mock_response(data_json, status=400)
        result = handle_operation_response(response)
        self.assertTrue(result)

    def testHandleSessionTokenResponse(self):
        data_json = None
        response = self.mock_response(data_json, status=200)
        session_token = handle_session_token_response(response)
        self.assertIsNone(session_token)

        data_json = {"status": {"type": "success", "message": "Success", "code": 200, "error": False}, "data": [{"status": "Authenticated","user": {"username": "kinua", "email": "kinua.wong@company.com", "firstname": "Kinua", "id": 88888888, "lastname": "Wong"},"return_to_url": None,"expires_at": "2016/01/07 05:56:21 +0000", "session_token": "9x8869x31134x7906x6x54474x21x18xxx90857x"}]}
        response = self.mock_response(data_json, status=200)
        session_token = handle_session_token_response(response)
        self.assertTrue(isinstance(session_token, SessionTokenInfo))

        data_json = {"status": {"type": "success", "code": 200, "message": "MFA is required for this user","error": False},"data": [{"user": {"email": "jennifer.hasenfus@onelogin.com", "username": "jhasenfus", "firstname": "Jennifer", "lastname": "Hasenfus", "id": 88888888},
                     "state_token": "xf4330878444597bd3933d4247cc1xxxxxxxxxxx", "callback_url": "https://api.us.onelogin.com/api/1/login/verify_factor", "devices": [
                     {"device_type": "OneLogin OTP SMS","device_id": 111111}]}]}
        response = self.mock_response(data_json, status=200)
        session_token = handle_session_token_response(response)
        self.assertTrue(isinstance(session_token, SessionTokenMFAInfo))

        data_json = {"status": {"message": "invalid"}, "data":[]}
        response = self.mock_response(data_json, status=200)
        with self.assertRaises(Exception):
            session_token = handle_session_token_response(response)

    def testHandleSamlEndpointResponse(self):
        data_json = None
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, None)
        self.assertIsNone(saml_endpoint_response)

        data_json = None
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 1)
        self.assertIsNone(saml_endpoint_response)

        data_json = None
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 2)
        self.assertIsNone(saml_endpoint_response)

        data_json = {"status": { "type": "success", "message": "Success", "error": False, "code": 200}, "data": "DQo8c2FtbHA6UmVzcG9uc2UgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgSUQ9IkdPU0FNTFIxMjkwMTE3NDU3MTc5NCIgVmVyc2lvbj0iMi4wIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIiBEZXN0aW5hdGlvbj0ie3JlY2lwaWVudH0iPg0KICA8c2FtbHA6U3RhdHVzPg0KICAgIDxzYW1scDpTdGF0dXNDb2RlIFZhbHVlPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6c3RhdHVzOlN1Y2Nlc3MiLz48L3NhbWxwOlN0YXR1cz4NCiAgPHNhbWw6QXNzZXJ0aW9uIHhtbG5zOnhzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgVmVyc2lvbj0iMi4wIiBJRD0icGZ4YTQ2NTc0ZGYtYjNiMC1hMDZhLTIzYzgtNjM2NDEzMTk4NzcyIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIj4NCiAgICA8c2FtbDpJc3N1ZXI"}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, None)
        self.assertIsNone(saml_endpoint_response)

        data_json = {"status": { "type": "success", "message": "Success", "error": False, "code": 200}, "data": "DQo8c2FtbHA6UmVzcG9uc2UgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgSUQ9IkdPU0FNTFIxMjkwMTE3NDU3MTc5NCIgVmVyc2lvbj0iMi4wIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIiBEZXN0aW5hdGlvbj0ie3JlY2lwaWVudH0iPg0KICA8c2FtbHA6U3RhdHVzPg0KICAgIDxzYW1scDpTdGF0dXNDb2RlIFZhbHVlPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6c3RhdHVzOlN1Y2Nlc3MiLz48L3NhbWxwOlN0YXR1cz4NCiAgPHNhbWw6QXNzZXJ0aW9uIHhtbG5zOnhzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgVmVyc2lvbj0iMi4wIiBJRD0icGZ4YTQ2NTc0ZGYtYjNiMC1hMDZhLTIzYzgtNjM2NDEzMTk4NzcyIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIj4NCiAgICA8c2FtbDpJc3N1ZXI"}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 1)
        self.assertTrue(isinstance(saml_endpoint_response, SAMLEndpointResponse))
        self.assertIsNone(saml_endpoint_response.mfa)
        self.assertTrue(saml_endpoint_response.saml_response is not None)

        data_json = {"status": { "type": "success", "message": "Success", "error": False, "code": 200}, "data": "DQo8c2FtbHA6UmVzcG9uc2UgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgSUQ9IkdPU0FNTFIxMjkwMTE3NDU3MTc5NCIgVmVyc2lvbj0iMi4wIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIiBEZXN0aW5hdGlvbj0ie3JlY2lwaWVudH0iPg0KICA8c2FtbHA6U3RhdHVzPg0KICAgIDxzYW1scDpTdGF0dXNDb2RlIFZhbHVlPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6c3RhdHVzOlN1Y2Nlc3MiLz48L3NhbWxwOlN0YXR1cz4NCiAgPHNhbWw6QXNzZXJ0aW9uIHhtbG5zOnhzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgVmVyc2lvbj0iMi4wIiBJRD0icGZ4YTQ2NTc0ZGYtYjNiMC1hMDZhLTIzYzgtNjM2NDEzMTk4NzcyIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIj4NCiAgICA8c2FtbDpJc3N1ZXI"}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 2)
        self.assertIsNone(saml_endpoint_response)

        data_json = {"status": {"type": "success", "message": "MFA is required for this user", "code": 200, "error": False}, "data": [{"state_token": "5xxx604x8xx9x694xx860173xxx3x78x3x870x56", "devices": [{"device_id": 666666,"device_type": "Google Authenticator"}],"callback_url": "https://api.us.onelogin.com/api/1/saml_assertion/verify_factor", "user": {"lastname": "Zhang", "username": "hzhang123", "email": "hazel.zhang@onelogin.com", "firstname": "Hazel", "id": 88888888 }}]}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 1)
        self.assertTrue(isinstance(saml_endpoint_response, SAMLEndpointResponse))
        self.assertTrue(isinstance(saml_endpoint_response.mfa, MFA))
        self.assertIsNone(saml_endpoint_response.saml_response)

        data_json = {"status": {"type": "success", "message": "MFA is required for this user", "code": 200, "error": False}, "data": [{"state_token": "5xxx604x8xx9x694xx860173xxx3x78x3x870x56", "devices": [{"device_id": 666666,"device_type": "Google Authenticator"}],"callback_url": "https://api.us.onelogin.com/api/1/saml_assertion/verify_factor", "user": {"lastname": "Zhang", "username": "hzhang123", "email": "hazel.zhang@onelogin.com", "firstname": "Hazel", "id": 88888888 }}]}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 2)
        self.assertIsNone(saml_endpoint_response)

        data_json = {"status": {"type": "pending", "message": "SMS token sent to your mobile device. Authentication pending.", "error": False, "code": 200}}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 1)
        self.assertTrue(isinstance(saml_endpoint_response, SAMLEndpointResponse))
        self.assertIsNone(saml_endpoint_response.mfa)
        self.assertIsNone(saml_endpoint_response.saml_response)

        data_json = {"data": "DQo8c2FtbHA6UmVzcG9uc2UgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgSUQ9IkdPU0FNTFIxMjkwMTE3NDU3MTc5NCIgVmVyc2lvbj0iMi4wIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIiBEZXN0aW5hdGlvbj0ie3JlY2lwaWVudH0iPg0KICA8c2FtbHA6U3RhdHVzPg0KICAgIDxzYW1scDpTdGF0dXNDb2RlIFZhbHVlPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6c3RhdHVzOlN1Y2Nlc3MiLz48L3NhbWxwOlN0YXR1cz4NCiAgPHNhbWw6QXNzZXJ0aW9uIHhtbG5zOnhzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgVmVyc2lvbj0iMi4wIiBJRD0icGZ4YTQ2NTc0ZGYtYjNiMC1hMDZhLTIzYzgtNjM2NDEzMTk4NzcyIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIj4NCiAgICA8c2FtbDpJc3N1ZXI", "message": "Success"}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 1)
        self.assertIsNone(saml_endpoint_response)

        data_json = {"data": "DQo8c2FtbHA6UmVzcG9uc2UgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgSUQ9IkdPU0FNTFIxMjkwMTE3NDU3MTc5NCIgVmVyc2lvbj0iMi4wIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIiBEZXN0aW5hdGlvbj0ie3JlY2lwaWVudH0iPg0KICA8c2FtbHA6U3RhdHVzPg0KICAgIDxzYW1scDpTdGF0dXNDb2RlIFZhbHVlPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6c3RhdHVzOlN1Y2Nlc3MiLz48L3NhbWxwOlN0YXR1cz4NCiAgPHNhbWw6QXNzZXJ0aW9uIHhtbG5zOnhzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgVmVyc2lvbj0iMi4wIiBJRD0icGZ4YTQ2NTc0ZGYtYjNiMC1hMDZhLTIzYzgtNjM2NDEzMTk4NzcyIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIj4NCiAgICA8c2FtbDpJc3N1ZXI", "message": "Success"}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 2)
        self.assertTrue(isinstance(saml_endpoint_response, SAMLEndpointResponse))
        self.assertIsNone(saml_endpoint_response.mfa)
        self.assertTrue(saml_endpoint_response.saml_response is not None)

        data_json = {"state_token": "5xxx604x8xx9x694xx860173xxx3x78x3x870x56", "message": "MFA is required for this user", "devices": [{"device_id": 666666, "device_type": "Google Authenticator"}], "callback_url": "https://api.us.onelogin.com/api/2/saml_assertion/verify_factor", "user": {"lastname": "Zhang", "username": "hzhang123", "email": "hazel.zhang@onelogin.com", "firstname": "Hazel", "id": 88888888}}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 1)
        self.assertIsNone(saml_endpoint_response)

        data_json = {"state_token": "5xxx604x8xx9x694xx860173xxx3x78x3x870x56", "message": "MFA is required for this user", "devices": [{"device_id": 666666, "device_type": "Google Authenticator"}], "callback_url": "https://api.us.onelogin.com/api/2/saml_assertion/verify_factor", "user": {"lastname": "Zhang", "username": "hzhang123", "email": "hazel.zhang@onelogin.com", "firstname": "Hazel", "id": 88888888}}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 2)
        self.assertTrue(isinstance(saml_endpoint_response, SAMLEndpointResponse))
        self.assertTrue(isinstance(saml_endpoint_response.mfa, MFA))
        self.assertIsNone(saml_endpoint_response.saml_response)

        data_json = {'message': 'MFA is required for this user', 'devices': [{'device_type': 'OneLogin Protect', 'device_id': 8022082}, {'device_type': 'OneLogin SMS', 'device_id': 8022200}, {'device_type': 'Google Authenticator', 'device_id': 8022235}, {'device_type': 'Yubico YubiKey', 'device_id': 8022575}], 'callback_url': 'https://api.us.onelogin.com/api/2/saml_assertion/verify_factor', 'state_token': 'ec9a65807794d46eb95a002aaefc9fe9ca86fe85', 'user': {'username': 'testlogin@example.com', 'lastname': 'login', 'firstname': 'test', 'email': 'testlogin@example.com', 'id': 115269114}}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 2)
        self.assertTrue(isinstance(saml_endpoint_response, SAMLEndpointResponse))
        self.assertTrue(isinstance(saml_endpoint_response.mfa, MFA))
        self.assertIsNone(saml_endpoint_response.saml_response)

        data_json = {'message': 'SMS token sent to your mobile device. Authentication pending.'}
        response = self.mock_response(data_json, status=200)
        saml_endpoint_response = handle_saml_endpoint_response(response, 2)
        self.assertTrue(isinstance(saml_endpoint_response, SAMLEndpointResponse))
        self.assertIsNone(saml_endpoint_response.mfa)
        self.assertIsNone(saml_endpoint_response.saml_response)

    def testOpCreateSuccess(self):
        self.assertTrue(op_create_success(200))
        self.assertTrue(op_create_success(201))
        self.assertFalse(op_create_success(202))
        self.assertFalse(op_create_success(204))
        self.assertFalse(op_create_success(400))
        self.assertFalse(op_create_success(404))
        self.assertFalse(op_create_success(412))
        self.assertFalse(op_create_success(500))

    def testOpDeleteSuccess(self):
        self.assertTrue(op_delete_success(200))
        self.assertTrue(op_delete_success(202))
        self.assertTrue(op_delete_success(204))
        self.assertFalse(op_delete_success(201))
        self.assertFalse(op_delete_success(400))
        self.assertFalse(op_delete_success(404))
        self.assertFalse(op_delete_success(412))
        self.assertFalse(op_delete_success(500))

    def testRetrieveAppsFromXml(self):
        apps_xml = """<apps>
  <app>
    <id>123456</id>
    <icon>https://assets.com/images/icons/square/netflix/mobile_50.png?11111</icon>
    <name>NetFlix</name>
    <provisioned>1</provisioned>
    <extension_required>true</extension_required>
    <personal>false</personal>
    <login_id>44444</login_id>
  </app>
  <!--clip-->
  <app>
    <id>654321</id>
    <icon>https://assets.com/images/icons/square/aws/mobile_50.png?22222</icon>
    <name>AWS DynamoDB</name>
    <provisioned>0</provisioned>
    <extension_required>false</extension_required>
    <personal>false</personal>
    <login_id>55555</login_id>
  </app>
</apps>"""
        apps = retrieve_apps_from_xml(EmbedApp, apps_xml)
        self.assertTrue(isinstance(apps, list))
        self.assertTrue(isinstance(apps[0], EmbedApp))
        self.assertEqual(len(apps), 2)
