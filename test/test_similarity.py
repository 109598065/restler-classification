import unittest
from main.similarity import Similarity


class SimilarityTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._categories = [
            'id',
            'name',
            'description',
            'time_zone',
            'url',
            'language',
            'location',
            'media_type',
            'color',
            'email',
            'query',
            'path',
            'domain'
        ]

    def test_normal_type(self):
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual('description', similarity.classify('desc'))

    def test_non_type(self):
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual('string', similarity.classify('contribute'))


if __name__ == '__main__':
    unittest.main()
