from pathlib import Path
from main.grammar_modifying import GrammarModifying

path = 'grammar.py'
backup_path = path.replace('.py', '_backup.py')
threshold = 0.8

if __name__ == '__main__':
    file_name = Path(path)
    backup_file_name = Path(backup_path)

    grammar_modifying = GrammarModifying(file_name, backup_file_name)
    grammar_modifying.execute_similarity(threshold)
