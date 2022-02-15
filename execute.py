from pathlib import Path
from main.grammar_modifying import GrammarModifying


if __name__ == '__main__':
    path = 'grammar.py'
    back_path = path.replace('.py', '_backup.py')

    file_name = Path(path)
    backup_file_name = Path(back_path)

    grammar_modifying = GrammarModifying(file_name, backup_file_name)
    grammar_modifying.execute()
