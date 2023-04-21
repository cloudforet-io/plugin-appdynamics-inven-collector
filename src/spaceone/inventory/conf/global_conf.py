CONNECTORS = {
    'AppdynamicsConnector': {
        'backend': 'spaceone.inventory.libs.connector.AppdynamicsConnector',
    },
}

LOG = {
    'filters': {
        'masking': {
            'rules': {
                'Collector.collect': [
                    'secret_data'
                ]
            }
        }
    }
}

HANDLERS = {
}

ENDPOINTS = {
}
