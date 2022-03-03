import os
import configuration
from main.file_handling import FileHandling
from main.similarity import Similarity
from main.string_modifying import StringModifying


class GrammarModifying:
    def __init__(self, file_name, backup_file_name):
        self._file_name = file_name
        self._backup_file_name = backup_file_name
        self._classification_table = configuration.classification_table
        self._threshold = 0.70

    def execute(self):
        lines = FileHandling().read(self._file_name)
        if not os.path.exists(self._backup_file_name):
            os.rename(self._file_name, self._backup_file_name)

        string_modifying = StringModifying(Similarity(self._classification_table, self._threshold))
        lines = string_modifying.modify_http_get(lines)
        lines = string_modifying.modify_http_post(lines)
        lines = string_modifying.modify_all_path_parameter_to_id_classification(lines)
        FileHandling.write(self._file_name, lines)
    