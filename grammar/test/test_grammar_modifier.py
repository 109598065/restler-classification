import os
import unittest
from pathlib import Path
from grammar.main.file_handling import FileHandling
from grammar.main.grammar_modifier import GrammarModifier


class GrammarModifierTestCase(unittest.TestCase):
    def setUp(self) -> None:
        path = 'test_file/grammar_shutterstock.py'
        backup_path = path.replace('.py', '_backup.py')
        self._file_name = Path(__file__).parent.absolute().joinpath(path)
        self._backup_file_name = Path(__file__).parent.absolute().joinpath(backup_path)

    def test_modify(self):
        try:
            grammar_modifier = GrammarModifier(self._file_name, self._backup_file_name)
            grammar_modifier.execute_similarity(0.8)
            self.assertTrue(Path.exists(self._file_name))
            self.assertTrue(Path.exists(self._backup_file_name))
            lines = FileHandling().read(self._file_name)
        finally:
            os.remove(self._file_name)
            os.rename(self._backup_file_name, self._file_name)
        self.assertEqual('    primitives.restler_fuzzable_color("fuzzstring", quoted=False),\n', lines[191])


if __name__ == '__main__':
    unittest.main()
