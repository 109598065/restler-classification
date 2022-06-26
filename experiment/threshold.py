import os
import re
from pathlib import Path
from grammar.main.grammar_modifier import GrammarModifier

sources = '''grammar/grammar_bitbucket.py
grammar/grammar_calendar.py
grammar/grammar_docker_engine_api.py
grammar/grammar_drive.py
grammar/grammar_giphy.py
grammar/grammar_instagram.py
grammar/grammar_shutterstock.py
grammar/grammar_trello.py
grammar/grammar_twitter.py
grammar/grammar_vimeo.py
grammar/grammar_zoom.py'''
sources = sources.split('\n')


def count_fuzzable_string(file):
    count = 0
    with open(file, "r") as input_file:
        for line in input_file:
            match_obj_for_search = re.search(r'restler_fuzzable_string', line)
            if match_obj_for_search:
                count += 1
    return count


if __name__ == '__main__':

    for path in sources:
        print('path: ' + str(path))
        target_name = path.replace('.py', '_classification.py')

        source = Path(path)
        target = Path(target_name)

        before_modify_count = count_fuzzable_string(source)
        print(str(before_modify_count) + ' before modify fuzzable string count')

        grammar_modifier = GrammarModifier(source, target)

        for i in range(75, 95, 5):
            threshold = i / 100

            grammar_modifier.execute_default_similarity(threshold)
            # grammar_modifier.execute_word2vec_similarity(threshold)

            after_modify_count = count_fuzzable_string(target)
            success_number = before_modify_count - after_modify_count

            print(str(threshold) + ' threshold')
            print(str(success_number) + ' Success number')
            # print(str(success_number/before_modify_count) + ' Success rate')

            os.remove(target)

        print('')
