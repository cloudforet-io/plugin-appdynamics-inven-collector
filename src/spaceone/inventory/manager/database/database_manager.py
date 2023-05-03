import time
import logging
from spaceone.inventory.libs.manager import AppdynamicsManager
from spaceone.inventory.libs.schema.base import ReferenceModel
from spaceone.inventory.connector.database import DatabaseConnector
from spaceone.inventory.model.database.cloud_service import *
from spaceone.inventory.model.database.cloud_service_type import CLOUD_SERVICE_TYPES
from spaceone.inventory.model.database.data import *

_LOGGER = logging.getLogger(__name__)


class DatabaseManager(AppdynamicsManager):
    connector_name = 'DatabaseConnector'
    cloud_service_types = CLOUD_SERVICE_TYPES

    def collect_cloud_service(self, params):
        """
                Args:
                    params (dict):
                        - 'options' : 'dict'
                        - 'schema' : 'str'
                        - 'secret_data' : 'dict'
                        - 'filter' : 'dict'
                        - 'zones' : 'list'
                        - 'subscription_info' :  'dict'
                Response:
                    CloudServiceResponse (list) : list of database data resource information
                    ErrorResourceResponse (list) : list of error resource information
                """

        _LOGGER.debug(f'** Database START **')

        start_time = time.time()

        database_conn: DatabaseConnector = self.locator.get_connector(self.connector_name, **params)
        databases_responses = []
        error_responses = []

        controller_url = self._get_controller_url(params['secret_data'])
        databases_list = database_conn.list_all_servers()
        for database in databases_list:

            try:
                database_dict = self.convert_nested_dictionary(database)
                db_id = database['id']  # id is primary key, dbserver_id
                """
                # Tiers
                database_dict['tiers'] = database_conn.list_tiers(db_id)

                # Backends
                database_dict["backends"] = database_conn.list_backends(db_id)
                """

                database_data = Database(database_dict, strict=False)
                database_resource = DatabaseResource({
                    'data': database_data,
                    'reference': self._create_reference(controller_url, db_id),
                    'name': database_data.name,
                })

                databases_responses.append(DatabaseResponse({'resource': database_resource}))

                pass
            except Exception as e:
                _LOGGER.error(f'[list_databases] {e}', exc_info=True)
#                error_response = self.generate_resource_error_response(e, 'Network', 'DatabaseGateway', database_id)
#                error_responses.append(error_response)

        _LOGGER.debug(f'** Database Finished {time.time() - start_time} Seconds **')
        return databases_responses, error_responses


    def _create_reference(self, controller_url, id):
        """ Create reference data for update_resource
      
        URI: controller_url/controller/rest/databases/servers/{dbserver_id}

        URL format exmaple:
            https://CONTROLLER_URL/controller/#/location=DB_MONITORING_SERVER_DASHBOARD&timeRange=last_1_hour.BEFORE_NOW.-1.-1.60&dbServerId=59
        Args:
            controller_url (str): controller url
            id (str): dbServerId
        """
        result = {
                "resource_id": f"{controller_url}/controller/rest/databases/servers/{id}",
                "external_link": f"{controller_url}/controller/#/location=DB_MONITORING_SERVER_DASHBOARD&timeRange=last_1_hour.BEFORE_NOW.-1.-1.60&dbServerId={id}"
            }
        return result

    def _get_controller_url(self, secret_data):
        """ Get controller url from secret data
        """
        return secret_data.get("controller", "CONTROLLER_URL")
