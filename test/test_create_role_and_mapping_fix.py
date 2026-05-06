# coding: utf-8

"""
    OneLogin API Python SDK

    Tests for the pydantic validation fixes for create_role and create_mapping responses.
"""


import unittest
from unittest.mock import patch

from onelogin.models.create_role201_response_inner import CreateRole201ResponseInner
from onelogin.models.mapping import Mapping
from onelogin.models.condition import Condition
from onelogin.models.action_obj import ActionObj
from onelogin.api.roles_api import RolesApi
from onelogin.api.user_mappings_api import UserMappingsApi


class TestCreateRoleResponseFix(unittest.TestCase):
    """Tests for the create_role response type fix.

    The server returns {"id": 123} (a dict), but the SDK previously expected
    List[CreateRole201ResponseInner]. Iterating over a dict's keys passed the
    string 'id' to from_dict, causing a pydantic ValidationError.
    """

    def test_create_role201_response_inner_from_dict(self):
        """Test that CreateRole201ResponseInner can be deserialized from a dict."""
        response_data = {"id": 123456}
        result = CreateRole201ResponseInner.from_dict(response_data)
        self.assertIsInstance(result, CreateRole201ResponseInner)
        self.assertEqual(result.id, 123456)

    def test_create_role201_response_inner_from_dict_none(self):
        """Test that from_dict handles None gracefully."""
        result = CreateRole201ResponseInner.from_dict(None)
        self.assertIsNone(result)

    def test_create_role_api_response_type_is_single_object(self):
        """
        Test that create_role API method returns CreateRole201ResponseInner
        (not List[CreateRole201ResponseInner]) when called with a mocked response.
        """
        expected_result = CreateRole201ResponseInner.from_dict({"id": 123456})
        api = RolesApi()

        with patch.object(api.api_client, 'call_api', return_value=expected_result):
            result = api.create_role()
            self.assertIsInstance(result, CreateRole201ResponseInner)
            self.assertEqual(result.id, 123456)

    def test_create_role_response_types_map(self):
        """
        Test that the response_types_map for create_role uses
        'CreateRole201ResponseInner' (not 'List[CreateRole201ResponseInner]').
        """
        api = RolesApi()
        expected_result = CreateRole201ResponseInner.from_dict({"id": 123456})

        with patch.object(api.api_client, 'call_api', return_value=expected_result) as mock_call_api:
            api.create_role()
            call_args = mock_call_api.call_args
            response_types_map = call_args[1]['response_types_map']
            self.assertEqual(response_types_map['201'], 'CreateRole201ResponseInner')


class TestCreateMappingResponseFix(unittest.TestCase):
    """Tests for the create_mapping response type fix.

    The server returns a single Mapping dict, but the SDK previously expected
    List[Mapping]. Iterating over a dict's keys passed the string 'id' to
    from_dict, causing a pydantic ValidationError.
    """

    def _make_mapping_data(self, include_id=True):
        data = {
            "name": "Test Mapping",
            "enabled": True,
            "match": "all",
            "position": 1,
            "conditions": [{"source": "last_login", "operator": ">", "value": "90"}],
            "actions": [{"action": "set_status", "value": ["1"]}],
        }
        if include_id:
            data["id"] = 456
        return data

    def test_mapping_from_dict_with_id(self):
        """Test that Mapping can be deserialized from a dict with an id."""
        result = Mapping.from_dict(self._make_mapping_data(include_id=True))
        self.assertIsInstance(result, Mapping)
        self.assertEqual(result.id, 456)
        self.assertEqual(result.name, "Test Mapping")

    def test_mapping_from_dict_without_id(self):
        """Test that Mapping can be deserialized from a dict without an id."""
        result = Mapping.from_dict(self._make_mapping_data(include_id=False))
        self.assertIsInstance(result, Mapping)
        self.assertIsNone(result.id)
        self.assertEqual(result.name, "Test Mapping")

    def test_mapping_from_dict_none(self):
        """Test that from_dict handles None gracefully."""
        result = Mapping.from_dict(None)
        self.assertIsNone(result)

    def test_mapping_to_dict_excludes_none_id(self):
        """Test that to_dict excludes id when it is None (for create requests)."""
        m = Mapping(
            name="Test Mapping",
            enabled=True,
            match="all",
            position=1,
            conditions=[Condition(source="last_login", operator=">", value="90")],
            actions=[ActionObj(action="set_status", value=["1"])],
        )
        self.assertIsNone(m.id)
        d = m.to_dict()
        self.assertNotIn("id", d)

    def test_create_mapping_api_response_type_is_single_object(self):
        """
        Test that create_mapping API method returns Mapping (not List[Mapping])
        when called with a mocked response.
        """
        expected_result = Mapping.from_dict(self._make_mapping_data())
        api = UserMappingsApi()

        with patch.object(api.api_client, 'call_api', return_value=expected_result):
            result = api.create_mapping()
            self.assertIsInstance(result, Mapping)
            self.assertEqual(result.id, 456)
            self.assertEqual(result.name, "Test Mapping")

    def test_create_mapping_response_types_map(self):
        """
        Test that the response_types_map for create_mapping uses
        'Mapping' (not 'List[Mapping]').
        """
        expected_result = Mapping.from_dict(self._make_mapping_data())
        api = UserMappingsApi()

        with patch.object(api.api_client, 'call_api', return_value=expected_result) as mock_call_api:
            api.create_mapping()
            call_args = mock_call_api.call_args
            response_types_map = call_args[1]['response_types_map']
            self.assertEqual(response_types_map['201'], 'Mapping')


if __name__ == '__main__':
    unittest.main()
