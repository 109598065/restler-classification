import re
from difflib import SequenceMatcher


class Similarity:
    def __init__(self, categories, threshold):
        self._categories = categories
        self._threshold = threshold

    def classify(self, word):
        snake_case_words = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
        split_words = snake_case_words.split('_')

        max_similar = 0.0
        classification = ''

        for category in self._categories:
            for split_word in split_words:
                similar = SequenceMatcher(None, category, split_word).ratio()
                if similar > max_similar:
                    max_similar = similar
                    classification = category

        if max_similar > self._threshold:
            return classification
        return 'string'
