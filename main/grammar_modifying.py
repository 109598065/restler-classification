import os
from main.file_handling import FileHandling
from main.similarity import Similarity
from main.string_modifying import StringModifying


class GrammarModifying:
    def __init__(self, file_name, backup_file_name):
        self._file_name = file_name
        self._backup_file_name = backup_file_name
        self._categories = [
            'id',
            'name',
            'description',
            'time_zone',
            'url',
            'language',
            'location',
            'media_type',
            'color',
            'email',
            'query',
            'path',
            'domain'
        ]
        self._threshold = 0.5

    def execute(self):
        lines = FileHandling().read(self._file_name)
        if not os.path.exists(self._backup_file_name):
            os.rename(self._file_name, self._backup_file_name)

        string_modifying = StringModifying(Similarity(self._categories, self._threshold))
        lines = string_modifying.modify_http_get(lines)
        lines = string_modifying.modify_http_post(lines)
        lines = string_modifying.modify_all_path_parameter_to_id_category(lines)
        FileHandling.write(self._file_name, lines)
