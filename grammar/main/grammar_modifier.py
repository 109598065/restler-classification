import configuration
from grammar.main.utility.file_handling import FileHandling
from grammar.main.similarity import Similarity
from grammar.main.string_modifier import StringModifier
from grammar.main.word2vec import Word2vec


class GrammarModifier:
    def __init__(self, source, target):
        self._source = source
        self._target = target
        self._classification_table = configuration.string_classification_table

    def execute_default_similarity(self, threshold):
        classification = Similarity(self._classification_table, threshold)
        self._execute(classification)

    def execute_word2vec_similarity(self, threshold):
        classification = Word2vec(self._classification_table, threshold)
        self._execute(classification)

    def _execute(self, classification):
        try:
            lines = FileHandling().read(self._source)
            string_modifier = StringModifier(classification)
            lines = string_modifier.execute(lines)
            FileHandling.write(self._target, lines)
        except OSError as e:
            print(e)
