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

    def test_belong_the_category(self):
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual('description', similarity.classify('desc'))

    def test_not_belong_any_category(self):
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual('string', similarity.classify('contribute'))

    def test_compound_word_processing(self):
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual(['media', 'type', 'media_type'], similarity._compound_word_processing('media_type'))

    def test_compound_word_direct_classify(self):
        word = 'media_type'
        similarity = Similarity(self._categories, 0.9)
        self.assertEqual('media_type', similarity.classify(word))

    def test_snake_case_word(self):
        word = 'subscription_id'
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual('id', similarity.classify(word))

    def test_camel_case_word(self):
        word = 'subscriptionId'
        similarity = Similarity(self._categories, 0.5)
        self.assertEqual('id', similarity.classify(word))


if __name__ == '__main__':
    unittest.main()
