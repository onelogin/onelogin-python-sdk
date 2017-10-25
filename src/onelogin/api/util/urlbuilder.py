# -*- coding: utf-8 -*-

""" Settings class

Copyright (c) 2017, OneLogin, Inc.
All rights reserved.

UrlBuilder class of the OneLogin's Python SDK.

"""


class UrlBuilder(object):
    """

    Builds the API URL endpoints for the OneLogin's Python SDK.

    """

    region = 'us'

    def __init__(self, region='us'):
        self.region = region

    def get_url(self, base, obj_id=None, extra_id=None):
        if obj_id is None:
            return base % (self.region)
        elif extra_id is None:
            return base % (self.region, obj_id)
        else:
            return base % (self.region, obj_id, extra_id)
