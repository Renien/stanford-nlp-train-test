from unittest import TestCase
from stanford_nlp_train_test import Util


class TestLoadConf(TestCase):
    def test_load_conf(self):
        Util.load_conf('./conf/properties.json')
        self.assertEqual(len(Util.conf), 13)
