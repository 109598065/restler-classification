import unittest
from grammar.main.similarity import Similarity
from grammar.test.test_file.classification_table import string_classification_table


class SimilarityTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._classification_table = string_classification_table

    def test_belong_the_classification(self):
        similarity = Similarity(self._classification_table, 0.8)
        self.assertEqual('id', similarity.classify('id'))

    def test_not_belong_any_classification(self):
        similarity = Similarity(self._classification_table, 0.8)
        self.assertEqual(None, similarity.classify('apple'))

    def test_compound_word_direct_classify(self):
        word = 'media_type'
        similarity = Similarity(self._classification_table, 0.9)
        self.assertEqual('media_type', similarity.classify(word))

    def test_snake_case_word_classify(self):
        word = 'subscription_id'
        similarity = Similarity(self._classification_table, 0.8)
        self.assertEqual('id', similarity.classify(word))

    def test_camel_case_word_classify(self):
        word = 'subscriptionId'
        similarity = Similarity(self._classification_table, 0.8)
        self.assertEqual('id', similarity.classify(word))

    def test_multiple_keywords_mapping_to_classification(self):
        word = 'username'
        similarity = Similarity(self._classification_table, 0.9)
        self.assertEqual('name', similarity.classify(word))


if __name__ == '__main__':
    unittest.main()
