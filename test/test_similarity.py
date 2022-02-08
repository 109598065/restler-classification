import unittest
from main.similarity import Similarity


class SimilarityTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._categories = [
            'description',
            'datetime',
            'time zone',
            'date',
            'url',
            'username',
            'language',
            'location',
            'media type',
            'color',
            'email',
            'query',
            'file path',
            'domain name'
        ]

    def test_normal_type(self):
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual('description', similarity.classify('desc'))

    def test_non_type(self):
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual('string', similarity.classify('contribute'))


if __name__ == '__main__':
    unittest.main()
