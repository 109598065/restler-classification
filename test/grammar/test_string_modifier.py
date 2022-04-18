import unittest
import configuration
from main.grammar.similarity import Similarity
from main.grammar.string_modifier import StringModifier
from main.grammar.word2vec import Word2vec


class StringModifierTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._classification_table = configuration.string_classification_table

    def test_http_get_modify_customize_string_with_similarity(self):
        lines = '''     primitives.restler_static_string("id="),
     primitives.restler_fuzzable_string("fuzzstring", quoted=False),'''
        lines = lines.split('\n')

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier._modify_query_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('     primitives.restler_static_string("id="),', lines[0])
        self.assertEqual('     primitives.restler_fuzzable_id("fuzzstring", quoted=False),', lines[1])

    def test_http_post_modify_customize_string_with_similarity(self):
        lines = '''primitives.restler_static_string("""
"items":
[
    {
        "id":"""),
primitives.restler_fuzzable_string("fuzzstring", quoted=True),'''
        lines = lines.split('\n')

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier._modify_body_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('primitives.restler_static_string("""', lines[0])
        self.assertEqual('"items":', lines[1])
        self.assertEqual('[', lines[2])
        self.assertEqual('    {', lines[3])
        self.assertEqual('        "id":"""),', lines[4])
        self.assertEqual('primitives.restler_fuzzable_id("fuzzstring", quoted=True),', lines[5])

    def test_http_get_modify_customize_non_classification_string_with_similarity(self):
        lines = '''     primitives.restler_static_string("apple="),
     primitives.restler_fuzzable_string("fuzzstring", quoted=False),'''
        lines = lines.split('\n')

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier._modify_query_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('     primitives.restler_static_string("apple="),', lines[0])
        self.assertEqual('     primitives.restler_fuzzable_string("fuzzstring", quoted=False),', lines[1])

    def test_http_post_modify_customize_non_classification_string_with_similarity(self):
        lines = '''primitives.restler_static_string("""
"items":
[
    {
        "apple":"""),
primitives.restler_fuzzable_string("fuzzstring", quoted=True),'''
        lines = lines.split('\n')

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier._modify_body_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('primitives.restler_static_string("""', lines[0])
        self.assertEqual('"items":', lines[1])
        self.assertEqual('[', lines[2])
        self.assertEqual('    {', lines[3])
        self.assertEqual('        "apple":"""),', lines[4])
        self.assertEqual('primitives.restler_fuzzable_string("fuzzstring", quoted=True),', lines[5])

    def test_modify_path_parameter(self):
        lines = '''# Endpoint: /timezone/{area}/{location}/{region}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
   primitives.restler_static_string("\r\n"),

],
   requestId="/timezone/{area}/{location}/{region}"
)
req_collection.add_request(request)'''
        lines = lines.split('\n')

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier._modify_path_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('    primitives.restler_fuzzable_area("fuzzstring", quoted=False),', lines[7])
        self.assertEqual('    primitives.restler_fuzzable_location("fuzzstring", quoted=False),', lines[9])
        self.assertEqual('    primitives.restler_fuzzable_region("fuzzstring", quoted=False),', lines[11])

    def test_modify_path_parameter_with_overmuch_parameter(self):
        lines = '''# Endpoint: /timezone/{area}/{location}.txt, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
    requestId="/timezone/{area}/{location}.txt"
)
req_collection.add_request(request)'''
        lines = lines.split('\n')

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier._modify_path_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('    primitives.restler_fuzzable_area("fuzzstring", quoted=False),', lines[7])

    def test_modify_path_parameter_with_multi_paragraph(self):
        lines = '''# Endpoint: /timezone/{area}/{location}/{region}, method: Get
        request = requests.Request([
            primitives.restler_static_string("GET "),
            primitives.restler_basepath("/api/"),
            primitives.restler_static_string("/"),
            primitives.restler_static_string("timezone"),
            primitives.restler_static_string("/"),
            primitives.restler_fuzzable_string("fuzzstring", quoted=False),
            primitives.restler_static_string("/"),
            primitives.restler_fuzzable_string("fuzzstring", quoted=False),
            primitives.restler_static_string("/"),
            primitives.restler_fuzzable_string("fuzzstring", quoted=False),
            primitives.restler_static_string(" HTTP/1.1\r\n"),
            primitives.restler_static_string("Accept: application/json\r\n"),
            primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
            primitives.restler_refreshable_authentication_token("authentication_token_tag"),
            primitives.restler_static_string("\r\n"),

        ],
            requestId="/timezone/{area}/{location}/{region}"
        )
        req_collection.add_request(request)

        # Endpoint: /timezone/{area}/{location}/{region}.txt, method: Get
        request = requests.Request([
            primitives.restler_static_string("GET "),
            primitives.restler_basepath("/api/"),
            primitives.restler_static_string("/"),
            primitives.restler_static_string("timezone"),
            primitives.restler_static_string("/"),
            primitives.restler_fuzzable_string("fuzzstring", quoted=False),
            primitives.restler_static_string("/"),
            primitives.restler_fuzzable_string("fuzzstring", quoted=False),
            primitives.restler_static_string(" HTTP/1.1\r\n"),
            primitives.restler_static_string("Accept: application/json\r\n"),
            primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
            primitives.restler_refreshable_authentication_token("authentication_token_tag"),
            primitives.restler_static_string("\r\n"),

        ],
            requestId="/timezone/{area}/{location}/{region}.txt"
        )
        req_collection.add_request(request)'''
        lines = lines.split('\n')

        string_modifier = StringModifier(Similarity(self._classification_table, 0.8))
        lines = string_modifier._modify_path_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('            primitives.restler_fuzzable_area("fuzzstring", quoted=False),', lines[7])
        self.assertEqual('            primitives.restler_fuzzable_location("fuzzstring", quoted=False),', lines[9])
        self.assertEqual('            primitives.restler_fuzzable_region("fuzzstring", quoted=False),', lines[11])

    def test_http_get_modify_customize_string_with_word2vec_similarity(self):
        lines = '''     primitives.restler_static_string("id="),
     primitives.restler_fuzzable_string("fuzzstring", quoted=False),'''
        lines = lines.split('\n')

        string_modifier = StringModifier(Word2vec(self._classification_table, 0.75))
        lines = string_modifier._modify_query_parameter(lines)
        self.assertTrue(lines)
        self.assertEqual('     primitives.restler_static_string("id="),', lines[0])
        self.assertEqual('     primitives.restler_fuzzable_id("fuzzstring", quoted=False),', lines[1])


if __name__ == '__main__':
    unittest.main()
