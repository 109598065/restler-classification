import os
import unittest
from pathlib import Path
from main.file_handling import FileHandling
from main.grammar_modifying import GrammarModifying


class GrammarModifyingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._file_name = Path("test_file/grammar_shutterstock.py")
        self._backup_file_name = Path("test_file/grammar_shutterstock_backup.py")

    def test_modify(self):
        grammar_modifying = GrammarModifying(self._file_name, self._backup_file_name)
        grammar_modifying.execute()
        self.assertTrue(os.path.exists(self._file_name))
        self.assertTrue(os.path.exists(self._backup_file_name))
        lines = FileHandling().read(self._file_name)
        self.assertEqual('    primitives.restler_fuzzable_color("fuzzstring", quoted=False),\n', lines[191])
        os.remove(self._file_name)
        os.rename(self._backup_file_name, self._file_name)


if __name__ == '__main__':
    unittest.main()
