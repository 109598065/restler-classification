import json


class DictionaryModifier:
    def __init__(self, original_json_file_path, dictionary_file_path):
        self._original_json_file_path = original_json_file_path
        self._dictionary_value_file_path = dictionary_file_path

    def execute(self):
        with open(self._original_json_file_path) as f:
            original_data = json.load(f)

        with open(self._dictionary_value_file_path) as f:
            dictionary_data = json.load(f)

        for i in dictionary_data:
            if i in original_data:
                original_data[i] = []
                for j in dictionary_data[i]:
                    original_data[i].append(j)

        with open(self._original_json_file_path, 'w') as f:
            json.dump(original_data, f, indent=4)
