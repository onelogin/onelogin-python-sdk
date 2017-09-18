# -*- coding: utf-8 -*-

""" Settings class

Copyright (c) 2017, OneLogin, Inc.
All rights reserved.

Settings class of the OneLogin's Python SDK.

"""

import os

from configparser import ConfigParser


class Settings(object):
    """

    Handles the settings of the OneLogin's Python SDK.

    """

    ONELOGIN_PROPERTIES_FILE = "onelogin.sdk.ini"
    CLIENT_ID_KEY = "onelogin.sdk.client_id"
    CLIENT_SECRET_KEY = "onelogin.sdk.client_secret"
    REGION = "onelogin.sdk.region"

    def __init__(self, path=None):
        """

        Create a new instance of Settings.

        :param path: Path where the sdk config file is located.
        :type path: string

        """
        if not path:
            path = os.path.dirname(os.path.abspath(__file__))

        if not path.endswith('/'):
            path += '/'

        filename = path + self.ONELOGIN_PROPERTIES_FILE

        if not os.path.isfile(filename):
            raise Exception("Onelogin settings file not found at %s" % filename)

        config = ConfigParser()
        config.read(filename)
        if 'Credentials' in config:
            self.client_id = config['Credentials'].get(self.CLIENT_ID_KEY, None)
            self.client_secret = config['Credentials'].get(self.CLIENT_SECRET_KEY, None)
            self.region = config['Credentials'].get(self.REGION, 'us')
        else:
            raise Exception("Credentials section not found at Onelogin settings file: %s" % filename)

    def get_url(self, base, obj_id=None):
        if obj_id is None:
            return base % (self.region)
        else:
            return base % (self.region, obj_id)
