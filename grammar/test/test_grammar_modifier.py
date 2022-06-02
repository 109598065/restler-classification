import os
import unittest
from pathlib import Path
from grammar.main.utility.file_handling import FileHandling
from grammar.main.grammar_modifier import GrammarModifier


class GrammarModifierTestCase(unittest.TestCase):
    def setUp(self) -> None:
        source = 'test_file/grammar_shutterstock.py'
        target = 'test_file/grammar_shutterstock_classification.py'
        self._source = Path(__file__).parent.absolute().joinpath(source)
        self._target = Path(__file__).parent.absolute().joinpath(target)

    def test_modify(self):
        try:
            grammar_modifier = GrammarModifier(self._source, self._target)
            grammar_modifier.execute_default_similarity(0.8)
            self.assertTrue(Path.exists(self._source))
            self.assertTrue(Path.exists(self._target))
            lines = FileHandling().read(self._source)
        finally:
            os.remove(self._target)
        self.assertEqual('    primitives.restler_fuzzable_color("fuzzstring", quoted=False),\n', lines[191])


if __name__ == '__main__':
    unittest.main()
