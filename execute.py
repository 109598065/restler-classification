from pathlib import Path
from dictionary.main.classification_setter import ClassificationSetter
from grammar.main.grammar_modifier import GrammarModifier

path = 'D:\\restler-test-\\Compile'
similarity_threshold = 0.6
word2vec_threshold = 0.75

engine_settings = 'engine_settings_classification.json'
custom_value_gen = 'custom_value_gen_classification.py'


if __name__ == '__main__':
    grammar_source = Path(path, 'grammar.py')
    grammar_target = Path(path, 'grammar_classification.py')

    grammar_modifier = GrammarModifier(grammar_source, grammar_target)
    grammar_modifier.execute_default_similarity(similarity_threshold)
    # grammar_modifier.execute_word2vec_similarity(word2vec_threshold)

    setter = ClassificationSetter(path, engine_settings, custom_value_gen)
    setter.execute()
