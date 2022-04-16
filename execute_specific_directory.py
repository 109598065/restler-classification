from pathlib import Path
from main.grammar.grammar_modifier import GrammarModifier

path = 'D:\\restler-test\\Compile\\grammar.py'
backup_path = path.replace('.py', '_backup.py')
threshold = 0.6

if __name__ == '__main__':
    file_name = Path(path)
    backup_file_name = Path(backup_path)

    grammar_modifier = GrammarModifier(file_name, backup_file_name)
    # grammar_modifier.execute_similarity(threshold)
    grammar_modifier.execute_word2vec_similarity(0.75)
