import unittest
import configuration
from main.grammar.similarity import Similarity
from main.grammar.string_modifier import StringModifier


class StringModifierTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._classification_table = configuration.string_classification_table

    def test_http_get_modify_customize_string_with_similarity(self):
        line1 = '     primitives.restler_static_string("id="),'
        line2 = '     primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        lines = [line1, line2]

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier.modify_query_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('     primitives.restler_static_string("id="),', lines[0])
        self.assertEqual('     primitives.restler_fuzzable_id("fuzzstring", quoted=False),', lines[1])

    def test_http_post_modify_customize_string_with_similarity(self):
        line1 = 'primitives.restler_static_string("""'
        line2 = '"items":'
        line3 = '['
        line4 = '    {'
        line5 = '        "id":"""),'
        line6 = 'primitives.restler_fuzzable_string("fuzzstring", quoted=True),'
        lines = [line1, line2, line3, line4, line5, line6]

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier.modify_body_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('primitives.restler_static_string("""', lines[0])
        self.assertEqual('"items":', lines[1])
        self.assertEqual('[', lines[2])
        self.assertEqual('    {', lines[3])
        self.assertEqual('        "id":"""),', lines[4])
        self.assertEqual('primitives.restler_fuzzable_id("fuzzstring", quoted=True),', lines[5])

    def test_http_get_modify_customize_non_classification_string_with_similarity(self):
        line1 = '     primitives.restler_static_string("apple="),'
        line2 = '     primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        lines = [line1, line2]

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier.modify_query_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('     primitives.restler_static_string("apple="),', lines[0])
        self.assertEqual('     primitives.restler_fuzzable_string("fuzzstring", quoted=False),', lines[1])

    def test_http_post_modify_customize_non_classification_string_with_similarity(self):
        line1 = 'primitives.restler_static_string("""'
        line2 = '"items":'
        line3 = '['
        line4 = '    {'
        line5 = '        "apple":"""),'
        line6 = 'primitives.restler_fuzzable_string("fuzzstring", quoted=True),'
        lines = [line1, line2, line3, line4, line5, line6]

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier.modify_body_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('primitives.restler_static_string("""', lines[0])
        self.assertEqual('"items":', lines[1])
        self.assertEqual('[', lines[2])
        self.assertEqual('    {', lines[3])
        self.assertEqual('        "apple":"""),', lines[4])
        self.assertEqual('primitives.restler_fuzzable_string("fuzzstring", quoted=True),', lines[5])

    def test_modify_path_parameter(self):
        lines = [line1, line2, line3, line4]

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier.modify_path_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('primitives.restler_static_string("contributors"),', lines[0])
        self.assertEqual('primitives.restler_static_string("/"),', lines[1])
        self.assertEqual('primitives.restler_fuzzable_id("fuzzstring", quoted=False),', lines[2])
        self.assertEqual('primitives.restler_static_string("/"),', lines[3])


if __name__ == '__main__':
    unittest.main()
