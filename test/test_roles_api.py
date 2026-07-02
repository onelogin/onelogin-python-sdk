# coding: utf-8

import json
import unittest
from unittest.mock import MagicMock, patch

import onelogin
from onelogin.api.roles_api import RolesApi  # noqa: E501
from onelogin.models.create_role201_response_inner import CreateRole201ResponseInner
from onelogin.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.roles_api.RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_role_admins(self):
        """Test case for add_role_admins

        Add Role Admins  # noqa: E501
        """
        pass

    def test_add_role_users(self):
        """Test case for add_role_users

        Add Role Users  # noqa: E501
        """
        pass

    def test_create_role(self):
        """Test case for create_role

        Create Role  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete Role by ID  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get Role by ID  # noqa: E501
        """
        pass

    def test_get_role_admins(self):
        """Test case for get_role_admins

        Get Role Admins  # noqa: E501
        """
        pass

    def test_get_role_apps(self):
        """Test case for get_role_apps

        Get all Apps assigned to Role  # noqa: E501
        """
        pass

    def test_get_role_by_id(self):
        """Test case for get_role_by_id

        Get Role by ID  # noqa: E501
        """
        pass

    def test_get_role_by_name(self):
        """Test case for get_role_by_name

        Get Role by Name  # noqa: E501
        """
        pass

    def test_get_role_users(self):
        """Test case for get_role_users

        Get Role Users  # noqa: E501
        """
        pass

    def test_list_roles(self):
        """Test case for list_roles

        List Roles  # noqa: E501
        """
        pass

    def test_remove_role_admins(self):
        """Test case for remove_role_admins

        Remove Role Admins  # noqa: E501
        """
        pass

    def test_remove_role_users(self):
        """Test case for remove_role_users

        Remove Role Users  # noqa: E501
        """
        pass

    def test_set_role_apps(self):
        """Test case for set_role_apps

        Set Role Apps  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update Role  # noqa: E501
        """
        pass

    def _make_urllib3_response(self, status, body):
        """Build a mock urllib3 response for HTTP-layer testing."""
        mock_resp = MagicMock()
        mock_resp.status = status
        mock_resp.reason = 'OK'
        mock_resp.data = json.dumps(body).encode('utf-8')
        mock_resp.headers = {'Content-Type': 'application/json'}
        return mock_resp

    def test_create_role_deserializes_single_object(self):
        """create_role must deserialize the API's single-object 201 response.

        The API returns {"id": 123} — not a list. Before the fix, the SDK
        declared List[CreateRole201ResponseInner] which caused the deserializer
        to iterate over dict keys, passing the string 'id' to from_dict and
        raising a pydantic ValidationError.
        """
        mock_resp = self._make_urllib3_response(201, {"id": 123456})
        with patch.object(
            self.api.api_client.rest_client.pool_manager, 'request',
            return_value=mock_resp
        ):
            result = self.api.create_role()
        self.assertIsInstance(result, CreateRole201ResponseInner)
        self.assertEqual(result.id, 123456)

    def test_create_role_response_type_is_not_list(self):
        """create_role must return a single CreateRole201ResponseInner, not a list."""
        mock_resp = self._make_urllib3_response(201, {"id": 7})
        with patch.object(
            self.api.api_client.rest_client.pool_manager, 'request',
            return_value=mock_resp
        ):
            result = self.api.create_role()
        self.assertNotIsInstance(result, list)

    def _make_empty_204_response(self):
        mock_resp = MagicMock()
        mock_resp.status = 204
        mock_resp.reason = 'No Content'
        mock_resp.data = b''
        mock_resp.headers = {}
        return mock_resp

    def _sent_body(self, mock_request):
        """Return the JSON-decoded body the SDK actually sent."""
        return json.loads(mock_request.call_args.kwargs['body'])

    def test_remove_role_users_sends_raw_array(self):
        """remove_role_users must send a raw JSON array of user ids.

        The API rejects the object form with 400 'Expected array in request'
        (GitHub issue #134): DELETE /api/2/roles/{role_id}/users parses its
        body with a strict array parser.
        """
        with patch.object(
            self.api.api_client.rest_client.pool_manager, 'request',
            return_value=self._make_empty_204_response()
        ) as mock_request:
            self.api.remove_role_users('789', [123, 456])
        self.assertEqual(self._sent_body(mock_request), [123, 456])

    def test_remove_role_users_unwraps_legacy_request_model(self):
        """The deprecated RemoveRoleUsersRequest form must still serialize to a raw array."""
        legacy = onelogin.RemoveRoleUsersRequest(user_id=[123, 456])
        with patch.object(
            self.api.api_client.rest_client.pool_manager, 'request',
            return_value=self._make_empty_204_response()
        ) as mock_request:
            self.api.remove_role_users('789', legacy)
        self.assertEqual(self._sent_body(mock_request), [123, 456])

    def test_remove_role_admins_sends_raw_array(self):
        """remove_role_admins shares the same raw-array body requirement."""
        with patch.object(
            self.api.api_client.rest_client.pool_manager, 'request',
            return_value=self._make_empty_204_response()
        ) as mock_request:
            self.api.remove_role_admins('789', [42])
        self.assertEqual(self._sent_body(mock_request), [42])


if __name__ == '__main__':
    unittest.main()
