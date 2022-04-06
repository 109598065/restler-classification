import unittest
import configuration
from main.grammar.similarity import Similarity
from main.grammar.string_modifier import StringModifier
from main.grammar.word2vec import Word2vec


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
        line1 = '# Endpoint: /timezone/{area}/{location}/{region}, method: Get'
        line2 = 'request = requests.Request(['
        line3 = '    primitives.restler_static_string("GET "),'
        line4 = '    primitives.restler_basepath("/api/"),'
        line5 = '    primitives.restler_static_string("/"),'
        line6 = '    primitives.restler_static_string("timezone"),'
        line7 = '    primitives.restler_static_string("/"),'
        line8 = '    primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        line9 = '    primitives.restler_static_string("/"),'
        line10 = '    primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        line11 = '    primitives.restler_static_string("/"),'
        line12 = '    primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        line13 = '    primitives.restler_static_string(" HTTP/1.1\r\n"),'
        line14 = '    primitives.restler_static_string("Accept: application/json\r\n"),'
        line15 = '    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),'
        line16 = '    primitives.restler_refreshable_authentication_token("authentication_token_tag"),'
        line17 = '   primitives.restler_static_string("\r\n"),'
        line18 = ''
        line19 = '],'
        line20 = '   requestId="/timezone/{area}/{location}/{region}"'
        line21 = ')'
        line22 = 'req_collection.add_request(request)'
        lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18, line19, line20, line21, line22]

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier.modify_path_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('    primitives.restler_fuzzable_area("fuzzstring", quoted=False),', lines[7])
        self.assertEqual('    primitives.restler_fuzzable_location("fuzzstring", quoted=False),', lines[9])
        self.assertEqual('    primitives.restler_fuzzable_region("fuzzstring", quoted=False),', lines[11])

    def test_modify_path_parameter_with_overmuch_parameter(self):
        line1 = '# Endpoint: /timezone/{area}/{location}.txt, method: Get'
        line2 = 'request = requests.Request(['
        line3 = '    primitives.restler_static_string("GET "),'
        line4 = '    primitives.restler_basepath("/api/"),'
        line5 = '    primitives.restler_static_string("/"),'
        line6 = '    primitives.restler_static_string("timezone"),'
        line7 = '    primitives.restler_static_string("/"),'
        line8 = '    primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        line9 = '    primitives.restler_static_string(" HTTP/1.1\r\n"),'
        line10 = '    primitives.restler_static_string("Accept: application/json\r\n"),'
        line11 = '    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),'
        line12 = '    primitives.restler_refreshable_authentication_token("authentication_token_tag"),'
        line13 = '    primitives.restler_static_string("\r\n"),'
        line14 = ''
        line15 = '],'
        line16 = '    requestId="/timezone/{area}/{location}.txt"'
        line17 = ')'
        line18 = 'req_collection.add_request(request)'

        lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14,
                 line15, line16, line17, line18]

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier.modify_path_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('    primitives.restler_fuzzable_area("fuzzstring", quoted=False),', lines[7])

    def test_http_get_modify_customize_string_with_word2vec_similarity(self):
        line1 = '     primitives.restler_static_string("id="),'
        line2 = '     primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
        lines = [line1, line2]

        string_modifier = StringModifier(Word2vec(self._classification_table))
        lines = string_modifier.modify_query_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('     primitives.restler_static_string("id="),', lines[0])
        self.assertEqual('     primitives.restler_fuzzable_id("fuzzstring", quoted=False),', lines[1])


if __name__ == '__main__':
    unittest.main()
