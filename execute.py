from pathlib import Path
from grammar.main.grammar_modifier import GrammarModifier

grammar_path = 'D:\\restler-test\\Compile\\grammar.py'
grammar_backup_path = grammar_path.replace('.py', '_backup.py')
similarity_threshold = 0.6
word2vec_threshold = 0.75


if __name__ == '__main__':
    file_name = Path(grammar_path)
    backup_file_name = Path(grammar_backup_path)

    grammar_modifier = GrammarModifier(file_name, backup_file_name)
    grammar_modifier.execute_similarity(similarity_threshold)
    # grammar_modifier.execute_word2vec_similarity(word2vec_threshold)
