import os
import unittest
import json

from spaceone.core.unittest.result import print_data
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.core import config
from spaceone.core import utils
from spaceone.core.transaction import Transaction
from spaceone.tester import TestCase, print_json


class TestCollector(TestCase):

    @classmethod
    def setUpClass(cls):
        appd_cred = os.environ.get('APPD_CRED')
        test_config = utils.load_yaml_from_file(appd_cred)

        cls.schema = 'cisco_client_secret'
        cls.appd_credentials = test_config
        super().setUpClass()

    def test_init(self):
        v_info = self.inventory.Collector.init({'options': {}})
        print_json(v_info)

    def test_verify(self):
        options = {
        }
        v_info = self.inventory.Collector.verify({'options': options, 'secret_data': self.appd_credentials})
        print_json(v_info)

    def test_collect(self):
        options = {
            'cloud_service_types': ['Application','Database'],
            'cloud_service_types': ['Database'],
        }
        # options = {}
        filter = {}
        resource_stream = self.inventory.Collector.collect({'options': options, 'secret_data': self.appd_credentials,
                                                            'filter': filter})

        for res in resource_stream:
            print_json(res)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
