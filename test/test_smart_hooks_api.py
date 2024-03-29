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
from onelogin.api.smart_hooks_api import SmartHooksApi  # noqa: E501
from onelogin.rest import ApiException


class TestSmartHooksApi(unittest.TestCase):
    """SmartHooksApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.smart_hooks_api.SmartHooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_environment_variable(self):
        """Test case for create_environment_variable

        Create Environment Variable  # noqa: E501
        """
        pass

    def test_create_hook(self):
        """Test case for create_hook

        Create Smart Hook  # noqa: E501
        """
        pass

    def test_delete_environment_variable(self):
        """Test case for delete_environment_variable

        Delete Environment Variable  # noqa: E501
        """
        pass

    def test_delete_hook(self):
        """Test case for delete_hook

        Delete Smart Hook by ID  # noqa: E501
        """
        pass

    def test_get_environment_variable(self):
        """Test case for get_environment_variable

        Get Environment Variable  # noqa: E501
        """
        pass

    def test_get_hook(self):
        """Test case for get_hook

        Get Smart Hook by ID  # noqa: E501
        """
        pass

    def test_get_logs(self):
        """Test case for get_logs

        Get Smart Hook Logs  # noqa: E501
        """
        pass

    def test_list_environment_variables(self):
        """Test case for list_environment_variables

        List Environment Variables  # noqa: E501
        """
        pass

    def test_list_hooks(self):
        """Test case for list_hooks

        List all Smart Hooks  # noqa: E501
        """
        pass

    def test_update_environment_variable(self):
        """Test case for update_environment_variable

        Update Environment Variable  # noqa: E501
        """
        pass

    def test_update_hook(self):
        """Test case for update_hook

        Update Smart Hook by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
