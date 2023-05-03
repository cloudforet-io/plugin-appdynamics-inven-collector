import os
from spaceone.inventory.libs.utils import *
from spaceone.inventory.libs.schema.metadata.dynamic_widget import CardWidget, ChartWidget
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, \
    EnumDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta
from spaceone.inventory.conf.cloud_service_conf import ASSET_URL

current_dir = os.path.abspath(os.path.dirname(__file__))

ag_count_by_account_conf = os.path.join(current_dir, 'widget/object_count_by_account.yaml')
ag_total_count_conf = os.path.join(current_dir, 'widget/object_total_count.yaml')

cst_object = CloudServiceTypeResource()
cst_object.name = 'Database'
cst_object.group = 'Databases'
cst_object.service_code = 'Cisco.Appdynamics/Database'
cst_object.labels = ['Database']
cst_object.is_major = True
cst_object.is_primary = True
cst_object.tags = {
    'spaceone:icon': f'{ASSET_URL}/database.svg',
}

cst_object._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        # Example
        TextDyField.data_source('Id', 'data.id'),
        TextDyField.data_source('Description', 'data.description'),
        # Add More
    ],
    search=[
        # Example
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='Id',
                        key='data.id',
                        data_type='integer'),
        SearchField.set(name='Description',
                        key='data.description'),
        # Add More
    ],
    widget=[
        ChartWidget.set(**get_data_from_yaml(ag_count_by_account_conf)),
        CardWidget.set(**get_data_from_yaml(ag_total_count_conf))
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_object}),
]
