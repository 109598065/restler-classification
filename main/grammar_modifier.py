import os
import configuration
from main.file_handling import FileHandling
from main.similarity import Similarity
from main.string_modifier import StringModifier


class GrammarModifier:
    def __init__(self, file_name, backup_file_name):
        self._file_name = file_name
        self._backup_file_name = backup_file_name

    def execute_similarity(self, threshold):
        lines = FileHandling().read(self._file_name)
        if not os.path.exists(self._backup_file_name):
            os.rename(self._file_name, self._backup_file_name)

        string_modifier = StringModifier(Similarity(classification_table, threshold))
        lines = string_modifier.modify_http_get(lines)
        lines = string_modifier.modify_http_post(lines)
        lines = string_modifier.modify_all_path_parameter_to_id_classification(lines)
        FileHandling.write(self._file_name, lines)
    