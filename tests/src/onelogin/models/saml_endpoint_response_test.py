# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.mfa import MFA
from onelogin.api.models.saml_endpoint_response import SAMLEndpointResponse

import unittest


class OneLogin_API_Model_SAMLEndpointResponse_Test(unittest.TestCase):

    def testSAMLEndpointResponse(self):
        """
        Tests the constructor method of the SAMLEndpointResponse class
        Build a SAMLEndpointResponse object and check if all the expected attributes exist
        as described in the SAMLEndpointResponse Resource of the OneLogin API
        """
        saml_endpoint_response = SAMLEndpointResponse("pending", "SMS token sent to your mobile device. Authentication pending.")
        expected_attributes = ['type', 'message', "mfa", "saml_response"]

        for attr in expected_attributes:
            self.assertTrue(hasattr(saml_endpoint_response, attr), "SAMLEndpointResponse has no attribute '{}'".format(attr))

    def testSAMLEndpointResponse(self):
        saml_endpoint_response = SAMLEndpointResponse("pending", "SMS token sent to your mobile device. Authentication pending.")
        self.assertEqual(saml_endpoint_response.type, "pending")
        self.assertEqual(saml_endpoint_response.message, "SMS token sent to your mobile device. Authentication pending.")
        self.assertIsNone(saml_endpoint_response.mfa)
        self.assertIsNone(saml_endpoint_response.saml_response)

        saml_endpoint_response = SAMLEndpointResponse("success", "MFA is required for this user")
        saml_endpoint_response.mfa = MFA({"state_token": "5xxx604x8xx9x694xx860173xxx3x78x3x870x56", "devices": [{"device_id": 666666, "device_type": "Google Authenticator"}], "callback_url": "https://api.us.onelogin.com/api/1/saml_assertion/verify_factor", "user": {"lastname": "Zhang", "username": "hzhang123", "email": "hazel.zhang@onelogin.com", "firstname": "Hazel", "id": 88888888}})
        self.assertEqual(saml_endpoint_response.type, "success")
        self.assertEqual(saml_endpoint_response.message, "MFA is required for this user")
        self.assertTrue(isinstance(saml_endpoint_response.mfa, MFA))
        self.assertIsNone(saml_endpoint_response.saml_response)
        
        saml_endpoint_response = SAMLEndpointResponse("success", "Success")
        saml_endpoint_response.saml_response = "DQo8c2FtbHA6UmVzcG9uc2UgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgSUQ9IkdPU0FNTFIxMjkwMTE3NDU3MTc5NCIgVmVyc2lvbj0iMi4wIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIiBEZXN0aW5hdGlvbj0ie3JlY2lwaWVudH0iPg0KICA8c2FtbHA6U3RhdHVzPg0KICAgIDxzYW1scDpTdGF0dXNDb2RlIFZhbHVlPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6c3RhdHVzOlN1Y2Nlc3MiLz48L3NhbWxwOlN0YXR1cz4NCiAgPHNhbWw6QXNzZXJ0aW9uIHhtbG5zOnhzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgVmVyc2lvbj0iMi4wIiBJRD0icGZ4YTQ2NTc0ZGYtYjNiMC1hMDZhLTIzYzgtNjM2NDEzMTk4NzcyIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIj4NCiAgICA8c2FtbDpJc3N1ZXI"
        self.assertEqual(saml_endpoint_response.type, "success")
        self.assertEqual(saml_endpoint_response.message, "Success")
        self.assertIsNone(saml_endpoint_response.mfa)
        self.assertEqual(saml_endpoint_response.saml_response, "DQo8c2FtbHA6UmVzcG9uc2UgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgSUQ9IkdPU0FNTFIxMjkwMTE3NDU3MTc5NCIgVmVyc2lvbj0iMi4wIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIiBEZXN0aW5hdGlvbj0ie3JlY2lwaWVudH0iPg0KICA8c2FtbHA6U3RhdHVzPg0KICAgIDxzYW1scDpTdGF0dXNDb2RlIFZhbHVlPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6c3RhdHVzOlN1Y2Nlc3MiLz48L3NhbWxwOlN0YXR1cz4NCiAgPHNhbWw6QXNzZXJ0aW9uIHhtbG5zOnhzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgVmVyc2lvbj0iMi4wIiBJRD0icGZ4YTQ2NTc0ZGYtYjNiMC1hMDZhLTIzYzgtNjM2NDEzMTk4NzcyIiBJc3N1ZUluc3RhbnQ9IjIwMTAtMTEtMThUMjE6NTc6MzdaIj4NCiAgICA8c2FtbDpJc3N1ZXI")
