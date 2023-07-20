# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from onelogin.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    OAUTH2 = "OAuth2"
    API_AUTHORIZATION_SERVER = "API Authorization Server"
    API_AUTH_SCOPES = "API Auth: Scopes"
    API_AUTH_CLAIMS = "API Auth: Claims"
    API_AUTH_CLIENT_APPS = "API Auth: Client Apps"
    APPS = "Apps"
    APP_RULES = "App Rules"
    BRANDING_SERVICE = "Branding Service"
    BRANDING_SERVICE_TEMPLATES = "Branding Service: Templates"
    BRANDING_SERVICE_SMTP = "Branding Service: SMTP"
    EVENTS = "Events"
    GROUPS = "Groups"
    INVITE_LINKS = "Invite Links"
    MULTI_FACTOR_AUTHENTICATION = "Multi Factor Authentication"
    MULTI_FACTOR_AUTHENTICATION_V1 = "Multi Factor Authentication V1"
    PRIVILEGES = "Privileges"
    ROLES = "Roles"
    SAML_ASSERTIONS = "SAML Assertions"
    USERS_V1 = "Users V1"
    USERS_V2 = "Users V2"
    USER_MAPPINGS = "User Mappings"
    VIGILANCE_AI = "Vigilance AI"
    SMART_HOOKS = "Smart Hooks"
