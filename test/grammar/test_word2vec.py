import unittest
import configuration
from main.grammar.word2vec import Word2vec


class Word2VecTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._classification_table = configuration.string_classification_table

    def test_belong_the_classification(self):
        word2vec = Word2vec(self._classification_table, 0.75)
        self.assertEqual('id', word2vec.classify('id'))


if __name__ == '__main__':
    unittest.main()
