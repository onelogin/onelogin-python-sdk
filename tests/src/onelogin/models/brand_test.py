# -*- coding: utf-8 -*-

# Copyright (c) 2021, OneLogin, Inc.
# All rights reserved.
from onelogin.api.models.brand import Brand
import unittest

import sys
if sys.version_info[0] >= 3:
    unicode = str

# noinspection PySetFunctionToLiteral
class OneLogin_API_Model_Brand_Test(unittest.TestCase):

    brand_v2_payload = { "id": 912, "enabled": True, "name": "ACME"}

    def getTestBrandsV2(self):
        test_brand = Brand({})
        test_brand.id = 912
        test_brand.enabled = True
        test_brand.name = "ACME"
        return test_brand

    def testBrand(self):
        """
        Tests the constructor method of the Brand class
        Build a Brand object and check if all the expected attributes exist
        as described in the Brand Resource of the OneLogin API
        """
        brand = Brand(data={})
        expected_attributes = ['id', 'name', "enabled"]

        for attr in expected_attributes:
            self.assertTrue(hasattr(brand, attr), "Brand has no attribute '{}'".format(attr))

    def testBrandV2Payload(self):
        brand = Brand(self.brand_v2_payload);
        self.assertEqual(unicode(brand), unicode(self.getTestBrandsV2()))
