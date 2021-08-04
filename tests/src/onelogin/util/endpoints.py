# -*- coding: utf-8 -*-

# Copyright (c) 2017, OneLogin, Inc.
# All rights reserved.

import unittest

from onelogin.api.client import OneLoginClient
from onelogin.api.util.endpoints import Endpoints
from onelogin.api.util.constants import Constants


class OneLogin_API_Util_Endpoints_Test(unittest.TestCase):

    def testEndpointEntries(self):
            """
            Verifies that the values introduced are valid
            """

            constants_dict = dict(Constants.__dict__)
            # Remove special endpoint
            del constants_dict['EMBED_APP_URL']
            del constants_dict['TOKEN_REFRESH_URL']
            del constants_dict['TOKEN_REQUEST_URL']
            del constants_dict['TOKEN_REVOKE_URL']
            del constants_dict['GET_RATE_URL']
            # Remove other constants
            del constants_dict['VALID_ACTIONS']
            # Remove entries starting with V2_
            dict_keys = list(constants_dict.keys())
            for key in dict_keys:
                if (key.startswith("V2_") or key.startswith("__")):
                    del constants_dict[key]

            endpoint_list = list(Endpoints.matrix.keys())
            constants_list = list(constants_dict)

            self.assertEqual(len(set(endpoint_list) - set(constants_list)), 0)
            self.assertEqual(len(set(constants_list) - set(endpoint_list)), 0)

            available_resources = OneLoginClient.api_configuration.keys()
            resources = []
            for key, value in Endpoints.matrix.items():
                self.assertEqual(len(Endpoints.matrix.get(key)), 1)
                self.assertTrue(isinstance(value,dict))
                self.assertEqual(len(value), 1)
                resource = list(value.keys())[0]
                if not resource in resources:
                    resources.append(resource)
                self.assertTrue(resource in available_resources)
                self.assertTrue(isinstance(value[resource], list))
                self.assertTrue(len(value[resource]) > 0)

            self.assertEqual(len(set(available_resources) - set(resources)), 0)
            self.assertEqual(len(set(resources) - set(available_resources)), 0)
