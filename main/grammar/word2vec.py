import gensim.downloader

model = gensim.downloader.load('glove-twitter-25')  # todo


class Word2vec:
    def __init__(self, classification_table):
        self._classification_table = classification_table
        self._model = model

    def classify(self, word):
        max_similar = -1
        classification = ''

        for key in self._classification_table.keys():
            if key in self._model and word in self._model:  # todo update
                similar = self._model.similarity(w1=key, w2=word)
                if similar >= max_similar:
                    max_similar = similar
                    classification = key

        if classification == '':
            return None
        return classification
