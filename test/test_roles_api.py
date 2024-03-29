# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import onelogin
from onelogin.api.roles_api import RolesApi  # noqa: E501
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


if __name__ == '__main__':
    unittest.main()
