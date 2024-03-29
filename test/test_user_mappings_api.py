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
from onelogin.api.user_mappings_api import UserMappingsApi  # noqa: E501
from onelogin.rest import ApiException


class TestUserMappingsApi(unittest.TestCase):
    """UserMappingsApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.user_mappings_api.UserMappingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_mapping(self):
        """Test case for create_mapping

        Create Mapping  # noqa: E501
        """
        pass

    def test_delete_mapping(self):
        """Test case for delete_mapping

        Delete Mapping  # noqa: E501
        """
        pass

    def test_get_mapping(self):
        """Test case for get_mapping

        Get Mapping  # noqa: E501
        """
        pass

    def test_list_mapping_action_values(self):
        """Test case for list_mapping_action_values

        List Actions Values  # noqa: E501
        """
        pass

    def test_list_mapping_conditions(self):
        """Test case for list_mapping_conditions

        List Conditions  # noqa: E501
        """
        pass

    def test_list_mapping_conditions_operators(self):
        """Test case for list_mapping_conditions_operators

        List Conditions Operators  # noqa: E501
        """
        pass

    def test_list_mapping_contion_values(self):
        """Test case for list_mapping_contion_values

        List Conditions Values  # noqa: E501
        """
        pass

    def test_list_mappings(self):
        """Test case for list_mappings

        List Mappings  # noqa: E501
        """
        pass

    def test_list_mappings_actions(self):
        """Test case for list_mappings_actions

        List Actions  # noqa: E501
        """
        pass

    def test_sort_mappings(self):
        """Test case for sort_mappings

        Bulk Sort  # noqa: E501
        """
        pass

    def test_update_mapping(self):
        """Test case for update_mapping

        Update Mapping  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
