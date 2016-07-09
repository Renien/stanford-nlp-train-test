from unittest import TestCase
from stanford_nlp_train_test import GenerateProps
from stanford_nlp_train_test import Util


class TestGenerateProps(TestCase):
    def test_update_props_file(self):
        Util.load_conf('./conf/properties.json')
        gen_props = GenerateProps(Util.conf)
        gen_props.update_props_file()
        self.assertEqual(len(gen_props.conf), 13)
