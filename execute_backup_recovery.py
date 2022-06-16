import os
import shutil

path = 'D:\\restler-test\\Compile\\'

grammar_path = path + 'grammar.py'
grammar_backup_path = grammar_path.replace('.py', '_backup.py')
custom_value_gen_template_path = path + 'custom_value_gen_template'
custom_value_gen_template_backup_path = custom_value_gen_template_path.replace('.py', '_backup.py')
engine_settings_path = path + 'engine_settings.json'
engine_settings_backup_path = engine_settings_path.replace('.json', '_backup.json')
custom_value_list = path + 'custom_value_list'


def dictionary():
    if os.path.exists(custom_value_gen_template_path) and os.path.exists(custom_value_gen_template_backup_path):
        os.remove(custom_value_gen_template_path)
        os.rename(custom_value_gen_template_backup_path, custom_value_gen_template_path)

    if os.path.exists(engine_settings_path) and os.path.exists(engine_settings_backup_path):
        os.remove(engine_settings_path)
        os.rename(engine_settings_backup_path, engine_settings_path)

    if os.path.exists(custom_value_list):
        shutil.rmtree(custom_value_list)


def grammar():
    if os.path.exists(grammar_path) and os.path.exists(grammar_backup_path):
        os.remove(grammar_path)
        os.rename(grammar_backup_path, grammar_path)


if __name__ == '__main__':
    grammar()
    dictionary()
