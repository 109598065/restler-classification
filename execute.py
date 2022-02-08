from pathlib import Path

from main.grammar_modifying import GrammarModifying

if __name__ == '__main__':
    file_name = Path("grammar.py")
    backup_file_name = Path("grammar_backup.py")

    grammar_modifying = GrammarModifying(file_name, backup_file_name)
    grammar_modifying.execute()
