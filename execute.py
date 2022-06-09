from pathlib import Path
from dictionary.main.classification_setter import ClassificationSetter
from grammar.main.grammar_modifier import GrammarModifier

path = r"D:\restler-test2\Compile"
similarity_threshold = 0.6
word2vec_threshold = 0.75

grammar_source = Path(path, 'grammar.py')
grammar_target = Path(path, 'grammar_classification.py')
engine_settings_target = 'engine_settings_classification.json'
custom_value_gen_target = 'custom_value_gen_classification.py'


if __name__ == '__main__':
    grammar_modifier = GrammarModifier(grammar_source, grammar_target)
    grammar_modifier.execute_default_similarity(similarity_threshold)
    # grammar_modifier.execute_word2vec_similarity(word2vec_threshold)

    setter = ClassificationSetter(path, engine_settings_target, custom_value_gen_target)
    setter.execute()
