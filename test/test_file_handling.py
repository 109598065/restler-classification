import unittest
import os
import uuid
from pathlib import Path
from main.file_handling import FileHandling


class FileHandlingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        path = 'test_file/grammar_shutterstock.py'
        backup_path = path.replace('.py', '_backup_' + str(uuid.uuid1()) + '.py')
        self._file_name = Path(path)
        self._backup_file_name = Path(backup_path)

    def test_read(self):
        lines = FileHandling().read(self._file_name)
        self.assertTrue(lines)
        self.assertEqual('""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""\n', lines[0])

    def test_write(self):
        lines = FileHandling().read(self._file_name)
        FileHandling.write(self._backup_file_name, lines)
        self.assertTrue(os.path.exists(self._backup_file_name))

        f = open(self._backup_file_name)
        self.assertEqual('""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""\n', f.readline())
        f.close()
        os.remove(self._backup_file_name)


if __name__ == '__main__':
    unittest.main()
