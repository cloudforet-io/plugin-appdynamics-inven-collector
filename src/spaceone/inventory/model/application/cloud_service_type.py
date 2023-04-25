import os
from spaceone.inventory.libs.utils import *
from spaceone.inventory.libs.schema.metadata.dynamic_widget import CardWidget, ChartWidget
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, \
    EnumDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta
from spaceone.inventory.conf.cloud_service_conf import ASSET_URL

current_dir = os.path.abspath(os.path.dirname(__file__))

ag_count_by_account_conf = os.path.join(current_dir, 'widget/application_count_by_account.yaml')
ag_total_count_conf = os.path.join(current_dir, 'widget/application_total_count.yaml')

cst_aplication = CloudServiceTypeResource()
cst_aplication.name = 'Application'
cst_aplication.group = 'Applications'
cst_aplication.service_code = 'Cisco.Appdynamics/application'
cst_aplication.labels = ['Application']
cst_aplication.is_major = True
cst_aplication.is_primary = True
cst_aplication.tags = {
    'spaceone:icon': f'{ASSET_URL}/application.svg',
}

cst_aplication._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Id', 'data.id'),
        TextDyField.data_source('Description', 'data.description'),
        TextDyField.data_source('AccountGuid', 'data.account_guid'),
    ],
    search=[
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='Id',
                        key='data.id',
                        data_type='integer'),
        SearchField.set(name='Description',
                        key='data.description'),
    ],
    widget=[
        ChartWidget.set(**get_data_from_yaml(ag_count_by_account_conf)),
        CardWidget.set(**get_data_from_yaml(ag_total_count_conf))
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_aplication}),
]
