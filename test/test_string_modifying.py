import unittest
import configuration
from main.similarity import Similarity
from main.string_modifying import StringModifying


class StringModifyingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._classification_table = configuration.classification_table

    def test_http_get_modify_customize_string_with_similarity(self):
        line1 = '     primitives.restler_static_string("desc="),'
        line2 = '     primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        lines = [line1, line2]

        string_modifying = StringModifying(Similarity(self._classification_table, 0.5))
        lines = string_modifying.modify_http_get(lines)
        self.assertTrue(lines)
        self.assertEqual('     primitives.restler_static_string("desc="),', lines[0])
        self.assertEqual('     primitives.restler_fuzzable_description("fuzzstring", quoted=False),', lines[1])

    def test_http_post_modify_customize_string_with_similarity(self):
        line1 = 'primitives.restler_static_string("""'
        line2 = '"items":'
        line3 = '['
        line4 = '    {'
        line5 = '        "desc":"""),'
        line6 = 'primitives.restler_fuzzable_string("fuzzstring", quoted=True),'
        lines = [line1, line2, line3, line4, line5, line6]

        string_modifying = StringModifying(Similarity(self._classification_table, 0.5))
        lines = string_modifying.modify_http_post(lines)
        self.assertTrue(lines)
        self.assertEqual('primitives.restler_static_string("""', lines[0])
        self.assertEqual('"items":', lines[1])
        self.assertEqual('[', lines[2])
        self.assertEqual('    {', lines[3])
        self.assertEqual('        "desc":"""),', lines[4])
        self.assertEqual('primitives.restler_fuzzable_description("fuzzstring", quoted=True),', lines[5])

    def test_http_get_modify_customize_non_classification_string_with_similarity(self):
        line1 = '     primitives.restler_static_string("apple="),'
        line2 = '     primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        lines = [line1, line2]

        string_modifying = StringModifying(Similarity(self._classification_table, 0.5))
        lines = string_modifying.modify_http_get(lines)
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

        string_modifying = StringModifying(Similarity(self._classification_table, 0.5))
        lines = string_modifying.modify_http_post(lines)
        self.assertTrue(lines)
        self.assertEqual('primitives.restler_static_string("""', lines[0])
        self.assertEqual('"items":', lines[1])
        self.assertEqual('[', lines[2])
        self.assertEqual('    {', lines[3])
        self.assertEqual('        "apple":"""),', lines[4])
        self.assertEqual('primitives.restler_fuzzable_string("fuzzstring", quoted=True),', lines[5])

    def test_modify_all_path_parameter_to_id_classification(self):
        line1 = 'primitives.restler_static_string("contributors"),'
        line2 = 'primitives.restler_static_string("/"),'
        line3 = 'primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        line4 = 'primitives.restler_static_string("/"),'
        lines = [line1, line2, line3, line4]

        string_modifying = StringModifying(Similarity(self._classification_table, 0.5))
        lines = string_modifying.modify_all_path_parameter_to_id_classification(lines)
        self.assertTrue(lines)
        self.assertEqual('primitives.restler_static_string("contributors"),', lines[0])
        self.assertEqual('primitives.restler_static_string("/"),', lines[1])
        self.assertEqual('primitives.restler_fuzzable_id("fuzzstring", quoted=False),', lines[2])
        self.assertEqual('primitives.restler_static_string("/"),', lines[3])


if __name__ == '__main__':
    unittest.main()
