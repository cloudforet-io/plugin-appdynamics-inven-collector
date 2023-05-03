import time
import logging
from spaceone.inventory.libs.manager import AppdynamicsManager
from spaceone.inventory.libs.schema.base import ReferenceModel
from spaceone.inventory.connector.application import ApplicationConnector
from spaceone.inventory.model.application.cloud_service import *
from spaceone.inventory.model.application.cloud_service_type import CLOUD_SERVICE_TYPES
from spaceone.inventory.model.application.data import *

_LOGGER = logging.getLogger(__name__)


class ApplicationManager(AppdynamicsManager):
    connector_name = 'ApplicationConnector'
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
                    CloudServiceResponse (list) : list of application data resource information
                    ErrorResourceResponse (list) : list of error resource information
                """

        _LOGGER.debug(f'** Application START **')

        start_time = time.time()

        application_conn: ApplicationConnector = self.locator.get_connector(self.connector_name, **params)
        applications_responses = []
        error_responses = []

        controller_url = self._get_controller_url(params['secret_data'])
        account_name = self._get_account_name(params['secret_data'])
        applications_list = application_conn.list_all_applications()
        for application in applications_list:

            try:
                application_dict = self.convert_nested_dictionary(application)
                app_id = application['id']  # id is primary key
                # Biz-transactions
                application_dict['business_transactions'] = application_conn.list_business_transactions(app_id)

                # Tiers
                application_dict['tiers'] = application_conn.list_tiers(app_id)

                # Backends
                application_dict["backends"] = application_conn.list_backends(app_id)

                application_data = Application(application_dict, strict=False)
                application_resource = ApplicationResource({
                    'data': application_data,
                    'reference': self._create_reference(controller_url, app_id),
                    'name': application_data.name,
                    'account': account_name,
                })
                # _LOGGER.debug(f'[APPLICATION GATEWAYS INFO] {application_resource.to_primitive()}')

                applications_responses.append(ApplicationResponse({'resource': application_resource}))

                pass
            except Exception as e:
                _LOGGER.error(f'[list_applications] {e}', exc_info=True)
#                error_response = self.generate_resource_error_response(e, 'Network', 'ApplicationGateway', application_id)
#                error_responses.append(error_response)

        _LOGGER.debug(f'** Application Finished {time.time() - start_time} Seconds **')
        return applications_responses, error_responses

    def _create_reference(self, controller_url, id):
        """ Create reference data for update_resource
      
        URI: controller_url/controller/rest/applications/{id}

        URL format exmaple:
            controller_url/controller/#/location=APP_DASHBOARD&timeRange=last_1_hour.BEFORE_NOW.-1.-1.60&application=439&dashboardMode=force
        Args:
            controller_url (str): controller url
            id (str): application ID
        """
        result = {
                "resource_id": f"{controller_url}/controller/rest/applications/{id}",
                "external_link": f"{controller_url}/controller/#/location=APP_DASHBOARD&timeRange=last_1_hour.BEFORE_NOW.-1.-1.60&application={id}&dashboardMode=force"
            }
        return result

    def _get_controller_url(self, secret_data):
        """ Get controller url from secret data
        """
        return secret_data.get("controller", "CONTROLLER_URL")

    def _get_account_name(self, secret_data):
        """ Get account name from secret data
        """
        return secret_data.get("account_name", "ACCOUNT_NAME")
