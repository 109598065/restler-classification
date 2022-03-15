import os
import unittest
import uuid
from pathlib import Path
from main.file_handling import FileHandling
from main.grammar_modifier import GrammarModifier


class GrammarModifierTestCase(unittest.TestCase):
    def setUp(self) -> None:
        path = 'test_file/grammar_shutterstock.py'
        backup_path = path.replace('.py', '_backup_' + str(uuid.uuid1()) + '.py')
        self._file_name = Path(path)
        self._backup_file_name = Path(backup_path)

    def test_modify(self):
        grammar_modifier = GrammarModifier(self._file_name, self._backup_file_name)
        grammar_modifier.execute_similarity(0.8)
        self.assertTrue(os.path.exists(self._file_name))
        self.assertTrue(os.path.exists(self._backup_file_name))
        lines = FileHandling().read(self._file_name)
        self.assertEqual('    primitives.restler_fuzzable_color("fuzzstring", quoted=False),\n', lines[191])
        os.remove(self._file_name)
        os.rename(self._backup_file_name, self._file_name)


if __name__ == '__main__':
    unittest.main()
