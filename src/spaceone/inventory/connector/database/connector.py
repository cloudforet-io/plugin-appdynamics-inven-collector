import logging
import requests

from spaceone.inventory.libs.connector import AppdynamicsConnector
from spaceone.inventory.error.custom import *
__all__ = ['DatabaseConnector']
_LOGGER = logging.getLogger(__name__)


class DatabaseConnector(AppdynamicsConnector):
    """
    https://docs.appdynamics.com/appd/22.x/22.3/en/extend-appdynamics/appdynamics-apis/database-visibility-api
    
    * Collectors
    * Database Servers
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_connect(kwargs.get('secret_data'))

    def list_all_servers(self):
        # GET /controller/rest/databases/servers
        PATH = "/controller/rest/databases/servers"
        return self.make_request(PATH)
