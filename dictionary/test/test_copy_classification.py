import unittest
from dictionary.main.copy_classification.custom_value_list.domain import domains
from dictionary.main.copy_classification.custom_value_list.ip import ips


class CopyClassificationTestCase(unittest.TestCase):
    def test_ip(self):
        self.assertTrue('8.8.8.8' in ips)
        self.assertTrue(len(ips) > 50)

    def test_domain(self):
        self.assertTrue('wikipedia.org' in domains)
        self.assertTrue(len(domains) > 40)


if __name__ == '__main__':
    unittest.main()
