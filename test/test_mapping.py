# coding: utf-8

import unittest
import datetime

import onelogin
from onelogin.models.mapping import Mapping  # noqa: E501
from onelogin.models.condition import Condition
from onelogin.models.action_obj import ActionObj
from onelogin.rest import ApiException

class TestMapping(unittest.TestCase):
    """Mapping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Mapping
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Mapping`
        """
        model = onelogin.models.mapping.Mapping()  # noqa: E501
        if include_optional :
            return Mapping(
                id = 56, 
                name = '', 
                enabled = True, 
                match = 'all', 
                position = 56, 
                conditions = [
                    onelogin.models.condition.condition(
                        source = 'last_login', 
                        operator = '>', 
                        value = '90', )
                    ], 
                actions = [
                    onelogin.models.action_obj.action_obj(
                        action = '', 
                        value = [
                            '2'
                            ], )
                    ]
            )
        else :
            return Mapping(
                name = '',
                enabled = True,
                match = 'all',
                position = 56,
                conditions = [
                    onelogin.models.condition.condition(
                        source = 'last_login', 
                        operator = '>', 
                        value = '90', )
                    ],
                actions = [
                    onelogin.models.action_obj.action_obj(
                        action = '', 
                        value = [
                            '2'
                            ], )
                    ],
        )
        """

    def testMapping(self):
        """Test Mapping"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

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

    def test_from_dict_with_id(self):
        """Test that Mapping can be deserialized from a dict containing an id."""
        result = Mapping.from_dict(self._make_mapping_data(include_id=True))
        self.assertIsInstance(result, Mapping)
        self.assertEqual(result.id, 456)
        self.assertEqual(result.name, "Test Mapping")

    def test_from_dict_without_id(self):
        """Test that Mapping can be deserialized from a dict that omits id (create request)."""
        result = Mapping.from_dict(self._make_mapping_data(include_id=False))
        self.assertIsInstance(result, Mapping)
        self.assertIsNone(result.id)
        self.assertEqual(result.name, "Test Mapping")

    def test_from_dict_with_id_only_partial_create_response(self):
        """Test that Mapping.from_dict accepts create response payloads that only include id."""
        result = Mapping.from_dict({"id": 456})
        self.assertIsInstance(result, Mapping)
        self.assertEqual(result.id, 456)
        self.assertIsNone(result.name)
        self.assertIsNone(result.enabled)
        self.assertIsNone(result.match)
        self.assertIsNone(result.position)
        self.assertIsNone(result.conditions)
        self.assertIsNone(result.actions)

    def test_from_dict_partial_non_id_only_still_raises(self):
        """Fallback must not mask genuinely malformed payloads."""
        from pydantic import ValidationError
        with self.assertRaises(ValidationError):
            Mapping.from_dict({"id": 1, "name": "Partial"})

    def test_from_dict_empty_dict_still_raises(self):
        """Empty payloads should not be treated as id-only."""
        from pydantic import ValidationError
        with self.assertRaises(ValidationError):
            Mapping.from_dict({})

    def test_from_dict_id_null_still_raises(self):
        """`{\"id\": null}` is an obviously broken response and must raise."""
        from pydantic import ValidationError
        with self.assertRaises(ValidationError):
            Mapping.from_dict({"id": None})

    def test_from_dict_none(self):
        """Test that from_dict handles None gracefully."""
        result = Mapping.from_dict(None)
        self.assertIsNone(result)

    def test_from_dict_with_null_position(self):
        """Disabled mappings return null for position; Mapping must accept None."""
        data = self._make_mapping_data(include_id=True)
        data["position"] = None
        result = Mapping.from_dict(data)
        self.assertIsInstance(result, Mapping)
        self.assertIsNone(result.position)

    def test_from_dict_without_position(self):
        """position should be optional; omitting it from the dict is valid."""
        data = self._make_mapping_data(include_id=True)
        del data["position"]
        result = Mapping.from_dict(data)
        self.assertIsInstance(result, Mapping)
        self.assertIsNone(result.position)

    def test_to_dict_excludes_none_position(self):
        """to_dict must omit position when it is None so update requests don't send it."""
        m = Mapping(
            name="Disabled Mapping",
            enabled=False,
            match="all",
            position=None,
            conditions=[Condition(source="last_login", operator=">", value="90")],
            actions=[ActionObj(action="set_status", value=["2"])],
        )
        self.assertIsNone(m.position)
        d = m.to_dict()
        self.assertNotIn("position", d)

    def test_to_dict_excludes_none_id(self):
        """Test that to_dict omits id when it is None, preventing 'Field not allowed' errors."""
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

if __name__ == '__main__':
    unittest.main()
