from onelogin.paths.api_2_branding_email_settings.get import ApiForget
from onelogin.paths.api_2_branding_email_settings.put import ApiForput
from onelogin.paths.api_2_branding_email_settings.delete import ApiFordelete


class Api2BrandingEmailSettings(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
