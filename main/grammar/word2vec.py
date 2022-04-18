import re
import gensim.downloader

model = gensim.downloader.load('glove-twitter-25')  # todo


class Word2vec:
    def __init__(self, classification_table, threshold):
        self._classification_table = classification_table
        self._threshold = threshold
        self._model = model

    def classify(self, word):
        split_words = self._compound_word_processing(word)
        max_similar = -1
        classification = ''

        for split_word in split_words:
            for key in self._classification_table.keys():
                if key in self._model and split_word in self._model:  # todo: update
                    similar = self._model.similarity(w1=key, w2=split_word)
                    if similar >= max_similar:
                        max_similar = similar
                        classification = key

        if max_similar > self._threshold and classification != '':
            return classification
        return None

    def _compound_word_processing(self, word):  # todo
        snake_case_words = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
        split_words = snake_case_words.split('_')
        split_words.append(snake_case_words)
        return split_words
