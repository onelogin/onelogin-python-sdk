from onelogin.paths.api_2_apps_app_id.get import ApiForget
from onelogin.paths.api_2_apps_app_id.put import ApiForput
from onelogin.paths.api_2_apps_app_id.delete import ApiFordelete


class Api2AppsAppId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
