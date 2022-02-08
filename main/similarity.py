from difflib import SequenceMatcher


class Similarity:
    def __init__(self, categories, threshold):
        self._categories = categories
        self._threshold = threshold

    def classify(self, parameter):
        max_similar = 0.0
        classification = ''

        for category in self._categories:
            similar = SequenceMatcher(None, category, parameter).ratio()
            if similar > max_similar:
                max_similar = similar
                classification = category

        if max_similar > self._threshold:
            return classification
        return 'string'
