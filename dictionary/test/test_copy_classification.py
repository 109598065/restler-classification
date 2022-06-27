import unittest
from dictionary.main.copy_classification.custom_value_list.domain import domains
from dictionary.main.copy_classification.custom_value_list.id import ids
from dictionary.main.copy_classification.custom_value_list.ip import ips
from dictionary.main.copy_classification.custom_value_list.path import paths


class CopyClassificationTestCase(unittest.TestCase):
    def test_ip(self):
        self.assertTrue('8.8.8.8' in ips)
        self.assertTrue(len(ips) > 50)
        for _ in ips:
            self.assertTrue(isinstance(_, str))

    def test_domain(self):
        self.assertTrue('wikipedia.org' in domains)
        self.assertTrue(len(domains) > 40)
        for _ in domains:
            self.assertTrue(isinstance(_, str))

    def test_id(self):
        self.assertTrue('fuzzstring' in ids)
        self.assertTrue(len(ids) > 30)
        for _ in ids:
            self.assertTrue(isinstance(_, str))

    def test_path(self):
        self.assertTrue('C:\\' in paths)
        self.assertTrue(len(ids) > 20)
        for _ in paths:
            self.assertTrue(isinstance(_, str))


if __name__ == '__main__':
    unittest.main()
