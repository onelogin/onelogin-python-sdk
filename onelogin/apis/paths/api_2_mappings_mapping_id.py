from onelogin.paths.api_2_mappings_mapping_id.get import ApiForget
from onelogin.paths.api_2_mappings_mapping_id.put import ApiForput
from onelogin.paths.api_2_mappings_mapping_id.delete import ApiFordelete


class Api2MappingsMappingId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
