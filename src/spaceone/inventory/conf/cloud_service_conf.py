MAX_WORKER = 20
SUPPORTED_FEATURES = ['garbage_collection']
SUPPORTED_SCHEDULES = ['hours']
SUPPORTED_RESOURCE_TYPE = ['inventory.CloudService', 'inventory.CloudServiceType']
FILTER_FORMAT = []

ASSET_URL = 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/appdynamics'

CLOUD_SERVICE_GROUP_MAP = {
    'Application': 'ApplicationManager',
    'Database': 'DatabaseManager',
}
