import typing_extensions

from onelogin.apis.tags import TagValues
from onelogin.apis.tags.o_auth2_api import OAuth2Api
from onelogin.apis.tags.api_authorization_server_api import APIAuthorizationServerApi
from onelogin.apis.tags.api_auth_scopes_api import APIAuthScopesApi
from onelogin.apis.tags.api_auth_claims_api import APIAuthClaimsApi
from onelogin.apis.tags.api_auth_client_apps_api import APIAuthClientAppsApi
from onelogin.apis.tags.apps_api import AppsApi
from onelogin.apis.tags.app_rules_api import AppRulesApi
from onelogin.apis.tags.branding_service_api import BrandingServiceApi
from onelogin.apis.tags.branding_service_templates_api import BrandingServiceTemplatesApi
from onelogin.apis.tags.branding_service_smtp_api import BrandingServiceSMTPApi
from onelogin.apis.tags.events_api import EventsApi
from onelogin.apis.tags.groups_api import GroupsApi
from onelogin.apis.tags.invite_links_api import InviteLinksApi
from onelogin.apis.tags.multi_factor_authentication_api import MultiFactorAuthenticationApi
from onelogin.apis.tags.multi_factor_authentication_v1_api import MultiFactorAuthenticationV1Api
from onelogin.apis.tags.privileges_api import PrivilegesApi
from onelogin.apis.tags.roles_api import RolesApi
from onelogin.apis.tags.saml_assertions_api import SAMLAssertionsApi
from onelogin.apis.tags.users_v1_api import UsersV1Api
from onelogin.apis.tags.users_v2_api import UsersV2Api
from onelogin.apis.tags.user_mappings_api import UserMappingsApi
from onelogin.apis.tags.vigilance_ai_api import VigilanceAIApi
from onelogin.apis.tags.smart_hooks_api import SmartHooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.OAUTH2: OAuth2Api,
        TagValues.API_AUTHORIZATION_SERVER: APIAuthorizationServerApi,
        TagValues.API_AUTH_SCOPES: APIAuthScopesApi,
        TagValues.API_AUTH_CLAIMS: APIAuthClaimsApi,
        TagValues.API_AUTH_CLIENT_APPS: APIAuthClientAppsApi,
        TagValues.APPS: AppsApi,
        TagValues.APP_RULES: AppRulesApi,
        TagValues.BRANDING_SERVICE: BrandingServiceApi,
        TagValues.BRANDING_SERVICE_TEMPLATES: BrandingServiceTemplatesApi,
        TagValues.BRANDING_SERVICE_SMTP: BrandingServiceSMTPApi,
        TagValues.EVENTS: EventsApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.INVITE_LINKS: InviteLinksApi,
        TagValues.MULTI_FACTOR_AUTHENTICATION: MultiFactorAuthenticationApi,
        TagValues.MULTI_FACTOR_AUTHENTICATION_V1: MultiFactorAuthenticationV1Api,
        TagValues.PRIVILEGES: PrivilegesApi,
        TagValues.ROLES: RolesApi,
        TagValues.SAML_ASSERTIONS: SAMLAssertionsApi,
        TagValues.USERS_V1: UsersV1Api,
        TagValues.USERS_V2: UsersV2Api,
        TagValues.USER_MAPPINGS: UserMappingsApi,
        TagValues.VIGILANCE_AI: VigilanceAIApi,
        TagValues.SMART_HOOKS: SmartHooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.OAUTH2: OAuth2Api,
        TagValues.API_AUTHORIZATION_SERVER: APIAuthorizationServerApi,
        TagValues.API_AUTH_SCOPES: APIAuthScopesApi,
        TagValues.API_AUTH_CLAIMS: APIAuthClaimsApi,
        TagValues.API_AUTH_CLIENT_APPS: APIAuthClientAppsApi,
        TagValues.APPS: AppsApi,
        TagValues.APP_RULES: AppRulesApi,
        TagValues.BRANDING_SERVICE: BrandingServiceApi,
        TagValues.BRANDING_SERVICE_TEMPLATES: BrandingServiceTemplatesApi,
        TagValues.BRANDING_SERVICE_SMTP: BrandingServiceSMTPApi,
        TagValues.EVENTS: EventsApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.INVITE_LINKS: InviteLinksApi,
        TagValues.MULTI_FACTOR_AUTHENTICATION: MultiFactorAuthenticationApi,
        TagValues.MULTI_FACTOR_AUTHENTICATION_V1: MultiFactorAuthenticationV1Api,
        TagValues.PRIVILEGES: PrivilegesApi,
        TagValues.ROLES: RolesApi,
        TagValues.SAML_ASSERTIONS: SAMLAssertionsApi,
        TagValues.USERS_V1: UsersV1Api,
        TagValues.USERS_V2: UsersV2Api,
        TagValues.USER_MAPPINGS: UserMappingsApi,
        TagValues.VIGILANCE_AI: VigilanceAIApi,
        TagValues.SMART_HOOKS: SmartHooksApi,
    }
)
