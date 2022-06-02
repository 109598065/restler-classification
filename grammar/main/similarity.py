import re
from difflib import SequenceMatcher
from grammar.main.utility.word_processing import compound_word_processing


class Similarity:
    def __init__(self, classification_table, threshold):
        self._classification_table = classification_table
        self._threshold = threshold

    def classify(self, word):
        split_words = compound_word_processing(word)
        max_similar = 0.0
        classification = ''

        for split_word in split_words:
            for key, values in self._classification_table.items():
                for value in values:
                    similar = SequenceMatcher(None, value, split_word).ratio()
                    if similar >= max_similar:
                        max_similar = similar
                        classification = key

        if max_similar > self._threshold:
            return classification
        return None
