from schematics.types import ModelType, StringType, PolyModelType, FloatType, DateTimeType

from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, DateTimeDyField, EnumDyField, \
    ListDyField, SizeField, StateItemDyField
from spaceone.inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout, TableDynamicLayout, \
    ListDynamicLayout, SimpleTableDynamicLayout
from spaceone.inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta
from spaceone.inventory.model.application.data import Application

'''
APPLICATION
'''
# TAB - Default
application_info_meta = ItemDynamicLayout.set_fields('Application', fields=[
    TextDyField.data_source('Name', 'name', options={
        'is_optional': True
    }),
    TextDyField.data_source('ID', 'data.id'),
    TextDyField.data_source('Description', 'data.description'),
    TextDyField.data_source('Account GUID', 'data.account_guid'),
])

# TAB - Tiers
tiers_table_meta = SimpleTableDynamicLayout.set_fields('Tiers',
                                                        root_path='data.tiers',
                                                        fields=[
                                                            TextDyField.data_source('Name', 'name'),
                                                            TextDyField.data_source('Agent Type', 'agent_type'),
                                                            TextDyField.data_source('Type', 'type'),
                                                            TextDyField.data_source('Number of Nodes', 'number_of_nodes')
                                                        ])
# TAB = Backend
backends_table_meta = SimpleTableDynamicLayout.set_fields('Backends',
                                                        root_path='data.backends',
                                                        fields=[
                                                            TextDyField.data_source('Name', 'name'),
                                                            TextDyField.data_source('Exit Point Type', 'exit_point_type')
                                                        ])

application_meta = CloudServiceMeta.set_layouts(
    [application_info_meta, tiers_table_meta, backends_table_meta])

class ApplicationResource(CloudServiceResource):
    cloud_service_group = StringType(default='Applications')
    cloud_service_type = StringType(default='Application')
    data = ModelType(Application)
    _metadata = ModelType(CloudServiceMeta, default=application_meta, serialized_name='metadata')
    name = StringType()
    account = StringType()


class ApplicationResponse(CloudServiceResponse):
    resource = PolyModelType(ApplicationResource)
