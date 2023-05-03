from schematics.types import ModelType, StringType, PolyModelType, FloatType, DateTimeType

from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, DateTimeDyField, EnumDyField, \
    ListDyField, SizeField, StateItemDyField
from spaceone.inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout, TableDynamicLayout, \
    ListDynamicLayout, SimpleTableDynamicLayout
from spaceone.inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta
# TODO: append data
from spaceone.inventory.model.database.data import Database

'''
APPLICATION
'''
# TAB - Default
database_info_meta = ItemDynamicLayout.set_fields('Database', fields=[
    TextDyField.data_source('Name', 'name', options={
        'is_optional': True
    }),
    TextDyField.data_source('ID', 'data.id'),
    TextDyField.data_source('Description', 'data.description'),
])

"""
# TAB = Biz-transactions
biz_tnxs_table_meta = SimpleTableDynamicLayout.set_fields('Business Transactions',
                                                        root_path='data.business_transactions',
                                                        fields=[
                                                            TextDyField.data_source('Name', 'name'),
                                                            TextDyField.data_source('Entry Point Type', 'entry_point_type'),
                                                            TextDyField.data_source('Tier Name', 'tier_name'),
                                                            TextDyField.data_source('Background', 'background')
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
"""

object_meta = CloudServiceMeta.set_layouts(
    [database_info_meta])

class DatabaseResource(CloudServiceResource):
    cloud_service_group = StringType(default='Databases')
    cloud_service_type = StringType(default='Database')
    data = ModelType(Database)
    _metadata = ModelType(CloudServiceMeta, default=object_meta, serialized_name='metadata')
    name = StringType()
    account = StringType()


class DatabaseResponse(CloudServiceResponse):
    resource = PolyModelType(DatabaseResource)
