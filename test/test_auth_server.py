# coding: utf-8

import unittest

from onelogin.models.auth_server import AuthServer
from onelogin.models.auth_server_configuration import AuthServerConfiguration


class TestAuthServer(unittest.TestCase):
    """AuthServer model tests — focused on the nullable-description bug class."""

    def _make_payload(self, description="A description"):
        return {
            "id": 123,
            "name": "Test API",
            "description": description,
            "configuration": {
                "resource_identifier": "https://example.com/api",
                "audiences": ["https://example.com/api"],
                "access_token_expiration_minutes": 10,
                "refresh_token_expiration_minutes": 480,
            },
        }

    def test_from_dict_with_description(self):
        result = AuthServer.from_dict(self._make_payload(description="A real description"))
        self.assertIsInstance(result, AuthServer)
        self.assertEqual(result.description, "A real description")

    def test_from_dict_with_null_description(self):
        """Auth servers (apps with auth_type=9) can have apps.description = NULL."""
        result = AuthServer.from_dict(self._make_payload(description=None))
        self.assertIsInstance(result, AuthServer)
        self.assertIsNone(result.description)

    def test_from_dict_without_description(self):
        data = self._make_payload()
        del data["description"]
        result = AuthServer.from_dict(data)
        self.assertIsInstance(result, AuthServer)
        self.assertIsNone(result.description)

    def test_to_dict_excludes_none_description(self):
        config = AuthServerConfiguration(
            resource_identifier="https://example.com/api",
            audiences=["https://example.com/api"],
            access_token_expiration_minutes=10,
            refresh_token_expiration_minutes=480,
        )
        server = AuthServer(name="Test API", description=None, configuration=config)
        d = server.to_dict()
        self.assertNotIn("description", d)


if __name__ == "__main__":
    unittest.main()
