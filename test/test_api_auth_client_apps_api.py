# coding: utf-8

import unittest

import onelogin
from onelogin.api.api_auth_client_apps_api import APIAuthClientAppsApi  # noqa: E501
from onelogin.rest import ApiException


class TestAPIAuthClientAppsApi(unittest.TestCase):
    """APIAuthClientAppsApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.api_auth_client_apps_api.APIAuthClientAppsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_client_app(self):
        """Test case for add_client_app

        Add Client App  # noqa: E501
        """
        pass

    def test_delete_client_app(self):
        """Test case for delete_client_app

        Remove Client App  # noqa: E501
        """
        pass

    def test_list_client_apps(self):
        """Test case for list_client_apps

        List Clients Apps  # noqa: E501
        """
        pass

    def test_update_client_app(self):
        """Test case for update_client_app

        Update Client App  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
