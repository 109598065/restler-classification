import re
from difflib import SequenceMatcher


class Similarity:
    def __init__(self, classification_table, threshold):
        self._classification_table = classification_table
        self._threshold = threshold

    def classify(self, word):
        split_words = self._compound_word_processing(word)
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

    def _compound_word_processing(self, word):
        snake_case_words = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
        split_words = snake_case_words.split('_')
        split_words.append(snake_case_words)
        return split_words


