import logging
import requests

from spaceone.inventory.libs.connector import AppdynamicsConnector
from spaceone.inventory.error.custom import *
__all__ = ['ApplicationConnector']
_LOGGER = logging.getLogger(__name__)


class ApplicationConnector(AppdynamicsConnector):
    """
    https://docs.appdynamics.com/appd/22.x/22.3/en/extend-appdynamics/appdynamics-apis/application-model-api
    
    * Applications
    * Business Transaction
    * Tiers
    * Registered Backends
    * Node Information
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_connect(kwargs.get('secret_data'))

    def list_all_applications(self):
        # GET /controller/rest/applications
        PATH = "/controller/rest/applications"
        return self.make_request(PATH)

    def list_tiers(self, app_id):
        # GET /controller/rest/applications/<app_id>/tiers
        PATH = f"/controller/rest/applications/{app_id}/tiers"
        return self.make_request(PATH)

    def list_backends(self, app_id):
        # GET /controller/rest/applications/<app_id>/backends
        PATH = f"/controller/rest/applications/{app_id}/backends"
        return self.make_request(PATH)

    def list_business_transactions(self, app_id):
        # GET /controller/rest/applications/<app_id>/business-transactions
        PATH = f"/controller/rest/applications/{app_id}/business-transactions"
        return self.make_request(PATH)
