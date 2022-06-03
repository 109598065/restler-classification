import os
import re
from pathlib import Path
from grammar.main.grammar_modifier import GrammarModifier

path1 = 'grammar/grammar_bitbucket.py'
path2 = 'grammar/grammar_calendar.py'
path3 = 'grammar/grammar_docker_engine_api.py'
path4 = 'grammar/grammar_drive.py'
path5 = 'grammar/grammar_giphy.py'
path6 = 'grammar/grammar_instagram.py'
path7 = 'grammar/grammar_shutterstock.py'
path8 = 'grammar/grammar_stack_exchange.py'
path9 = 'grammar/grammar_trello.py'
path10 = 'grammar/grammar_twitter.py'
path11 = 'grammar/grammar_vimeo.py'
path12 = 'grammar/grammar_zoom.py'


def count_fuzzable_string(file):
    count = 0
    with open(file, "r") as input_file:
        for line in input_file:
            match_obj_for_search = re.search(r'restler_fuzzable_string', line)
            if match_obj_for_search:
                count += 1
    return count


if __name__ == '__main__':

    paths = [path1, path2, path3, path4, path5, path6, path7, path8, path9, path10, path11, path12]

    for path in paths:
        print('path: ' + str(path))
        backup_path = path.replace('.py', '_backup.py')

        file_name = Path(path)
        backup_file_name = Path(backup_path)

        before_modify_count = count_fuzzable_string(file_name)
        print('before modify fuzzable string count: ' + str(before_modify_count))

        grammar_modifier = GrammarModifier(file_name, backup_file_name)

        for i in range(70, 95, 5):
            threshold = i / 100

            grammar_modifier.execute_default_similarity(threshold)

            after_modify_count = count_fuzzable_string(file_name)
            print('threshold: ' + str(threshold))
            print('failure classification count: ' + str(after_modify_count))

            if os.path.exists(path) and os.path.exists(backup_path):
                os.remove(path)
                os.rename(backup_file_name, path)

        print('')
