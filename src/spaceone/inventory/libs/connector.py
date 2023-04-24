import os
import logging
import requests

from urllib.parse import urljoin, urlencode
from spaceone.core.connector import BaseConnector

DEFAULT_SCHEMA = 'appdynamics_client_secret'
_LOGGER = logging.getLogger(__name__)


class AppdynamicsConnector(BaseConnector):

    def __init__(self, **kwargs):
        """
        kwargs
            - schema
            - options
            - secret_data

        secret_data(dict)
            - type: ..
            - project_id: ...
            - token_uri: ...
            - ...
        """

        super().__init__(transaction=None, connector_conf=None)

    def set_connect(self, secret_data):
        # URL: /controller/api/oauth/access_token
        # create access_token
        # secret_data
        # client_name, account_name, client_secret, controller
        PATH = "/controller/api/oauth/access_token"
        BASE_URL = secret_data.get("controller", None)
        self.base_url = BASE_URL
        if BASE_URL is None:
            # ERROR no controller
            # TODO: Return ERROR
            pass
        client_name = secret_data.get("client_name", None)
        account_name = secret_data.get("account_name", None)
        client_secret = secret_data.get("client_secret", None)
        if client_name is None or account_name is None or client_secret is None:
            # secret_data is not complete
            # TODO: Return ERROR
            pass
        client_id = f'{client_name}@{account_name}'
        params = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
        full_url = urljoin(BASE_URL , PATH)
        response = requests.post(full_url, data=params)
        if response.status_code == 200:
            self.access_token=response.json()["access_token"]
        else:
            # fail to get access token
            # TODO
            pass

    def verify(self, **kwargs):
        # TODO
        return "ACTIVE"

    def make_request(self, path):
        headers = {
                "Authorization" : f"Bearer {self.access_token}"
                }
        full_url = urljoin(self.base_url, path)
        response = requests.get(full_url + "?output=JSON", headers=headers)
        if response.status_code == 200:
            print("******* response ******")
            print(response.json())
            return response.json()
        # fail to request
        # TODO
        print(f"Failed {full_url}")
