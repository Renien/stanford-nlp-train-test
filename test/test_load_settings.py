from unittest import TestCase
from stanford_nlp_train_test import Util


class TestLoad_settings(TestCase):
    def test_load_settings(self):
        Util.load_settings()
        self.assertEqual(len(Util.settings), 12)
