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
