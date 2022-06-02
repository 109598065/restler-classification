import unittest
import os
from pathlib import Path
from grammar.main.utility.file_handling import FileHandling


class FileHandlingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        path = '../test_file/grammar_shutterstock.py'
        backup_path = path.replace('.py', '_backup.py')
        self._file_name = Path(__file__).parent.absolute().joinpath(path)
        self._backup_file_name = Path(__file__).parent.absolute().joinpath(backup_path)

    def test_read(self):
        lines = FileHandling().read(self._file_name)
        self.assertTrue(lines)
        self.assertEqual('""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""\n', lines[0])

    def test_write(self):
        lines = FileHandling().read(self._file_name)
        try:
            FileHandling.write(self._backup_file_name, lines)
            self.assertTrue(Path.exists(self._backup_file_name))
            f = open(self._backup_file_name)
            content = f.readline()
            f.close()
        finally:
            os.remove(self._backup_file_name)
        self.assertEqual('""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""\n', content)


if __name__ == '__main__':
    unittest.main()
