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


if __name__ == '__main__':
    unittest.main()
