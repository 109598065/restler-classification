import json
import os
import shutil
import unittest
import uuid
from pathlib import Path
from main.dictionary.dictionary_modifier import DictionaryModifier


class DictionaryModifierTestCase(unittest.TestCase):
    def test_dictionary_modifier(self):
        try:
            original_json_path = 'test_file/dict.json'
            original_json_path_backup = original_json_path.replace('.json', '_backup_' + str(uuid.uuid1()) + '.json')
            original_json_name = Path(__file__).parent.absolute().joinpath(original_json_path)
            original_json_name_backup = Path(__file__).parent.absolute().joinpath(original_json_path_backup)
            shutil.copyfile(original_json_name, original_json_name_backup)

            dictionary_file_path = 'test_file/mapping.json'
            dictionary_file_name = Path(__file__).parent.absolute().joinpath(dictionary_file_path)

            dictionary_modifier = DictionaryModifier(original_json_name, dictionary_file_name)
            dictionary_modifier.execute()

            with open(original_json_name) as f:
                data = json.load(f)

            self.assertTrue('Asia' in data['restler_fuzzable_time_zone'])
            self.assertTrue('Europe' in data['restler_fuzzable_time_zone'])
            self.assertFalse('fuzzstring' in data['restler_fuzzable_time_zone'])
        finally:
            os.remove(original_json_name)
            os.rename(original_json_name_backup, original_json_name)


if __name__ == '__main__':
    unittest.main()
