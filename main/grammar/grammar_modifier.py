import os
import configuration
from main.grammar.file_handling import FileHandling
from main.grammar.similarity import Similarity
from main.grammar.string_modifier import StringModifier
from main.grammar.word2vec import Word2vec


class GrammarModifier:
    def __init__(self, file_name, backup_file_name):
        self._file_name = file_name
        self._backup_file_name = backup_file_name

    def execute_similarity(self, threshold):
        classification_table = configuration.string_classification_table
        lines = FileHandling().read(self._file_name)
        if not os.path.exists(self._backup_file_name):
            os.rename(self._file_name, self._backup_file_name)

        string_modifier = StringModifier(Similarity(classification_table, threshold))
        lines = string_modifier.modify_query_parameter(lines)
        lines = string_modifier.modify_body_parameter(lines)
        lines = string_modifier.modify_path_parameter(lines)
        FileHandling.write(self._file_name, lines)

    # todo
    def execute_word2vec_similarity(self):
        classification_table = configuration.string_classification_table
        lines = FileHandling().read(self._file_name)
        if not os.path.exists(self._backup_file_name):
            os.rename(self._file_name, self._backup_file_name)

        string_modifier = StringModifier(Word2vec(classification_table))
        lines = string_modifier.modify_query_parameter(lines)
        lines = string_modifier.modify_body_parameter(lines)
        lines = string_modifier.modify_path_parameter(lines)
        FileHandling.write(self._file_name, lines)

    