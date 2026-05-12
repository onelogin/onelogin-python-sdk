# coding: utf-8

import unittest

import onelogin
from onelogin.api.apps_api import AppsApi  # noqa: E501
from onelogin.rest import ApiException


class TestAppsApi(unittest.TestCase):
    """AppsApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.apps_api.AppsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_app(self):
        """Test case for create_app

        Create App  # noqa: E501
        """
        pass

    def test_delete_app(self):
        """Test case for delete_app

        Delete App  # noqa: E501
        """
        pass

    def test_delete_app_parameter(self):
        """Test case for delete_app_parameter

        Delete Parameter from App  # noqa: E501
        """
        pass

    def test_get_app(self):
        """Test case for get_app

        Get App  # noqa: E501
        """
        pass

    def test_get_app_users(self):
        """Test case for get_app_users

        Get App Users  # noqa: E501
        """
        pass

    def test_list_apps(self):
        """Test case for list_apps

        List Apps  # noqa: E501
        """
        pass

    def test_list_connectors(self):
        """Test case for list_connectors

        List Connectors  # noqa: E501
        """
        pass

    def test_update_app(self):
        """Test case for update_app

        Update App  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
