from onelogin.paths.api_2_hooks_hook_id.get import ApiForget
from onelogin.paths.api_2_hooks_hook_id.put import ApiForput
from onelogin.paths.api_2_hooks_hook_id.delete import ApiFordelete


class Api2HooksHookId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
