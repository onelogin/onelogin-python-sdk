#!/usr/bin/python


class SAMLEndpointResponse(object):
    def __init__(self, status_type, status_message):
        self.type = status_type
        self.message = status_message
        self.mfa = None
        self.saml_response = None
