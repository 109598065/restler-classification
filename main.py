import os
import re
from difflib import SequenceMatcher

_file_name = "grammar.py"
_backup_file_name = "grammar_backup.py"
categories = [
    'description',
    'datetime',
    'time zone',
    'date',
    'url',
    'username',
    'language',
    'location',
    'media type',
    'color',
    'email',
    'query',
    'file path',
    'domain name'
]
threshold = 0.6


def execute():
    if os.path.exists(_backup_file_name):
        return
    os.rename(_file_name, _backup_file_name)

    state = 0

    with open(_backup_file_name, "r") as input_file:
        with open(_file_name, "w") as output_file:
            for line in input_file:
                if state == 0:
                    match_obj_for_search = re.search(r'primitives.restler_static_string\("(.*)="\),', line)
                    if match_obj_for_search:
                        attribute = match_obj_for_search.group(1)
                        state = 1
                elif state == 1:
                    match_obj_for_change = re.search(r'restler_fuzzable_string', line)
                    state = 0
                    if match_obj_for_change:
                        classification = similarity(attribute)
                        if classification is None:
                            classification = 'string'
                        line = line.replace('restler_fuzzable_string',
                                            'restler_fuzzable_' + classification)
                        # print(line)  # will change
                output_file.write(line)


def similarity(parm):
    max_similar = 0.0
    classification = ''

    for category in categories:
        similar = SequenceMatcher(None, category, parm).ratio()
        if similar > max_similar:
            max_similar = similar
            classification = category

    if max_similar > threshold:
        return classification
    return None


def get_regular():
    line = '     primitives.restler_static_string("country="),'
    match_obj = re.search(r'primitives.restler_static_string\("(.*)="\),', line)
    if match_obj:
        print("match_obj.group() : ", match_obj.group())
        print("match_obj.group(1) : ", match_obj.group(1))


def get_change_next_statement():
    line1 = '     primitives.restler_static_string("country="),'
    line2 = '           primitives.restler_fuzzable_string("fuzzstring", quoted=False),'
    input_file = [line1, line2]
    state = 0

    for line in input_file:
        if state == 0:
            match_obj_for_search = re.search(r'primitives.restler_static_string\("(.*)="\),', line)
            if match_obj_for_search:
                attribute = match_obj_for_search.group(1)
                print(attribute)  # will change
                state = 1
        elif state == 1:
            state = 0
            match_obj_for_change = re.search(r'restler_fuzzable_string', line)
            if match_obj_for_change:
                line = line.replace('restler_fuzzable_string', 'restler_fuzzable_' + match_obj_for_search.group(1))
                print(line)  # will change


def post_change_next_statement():
    line1 = 'primitives.restler_static_string("""'
    line2 = '"items":'
    line3 = '['
    line4 = '    {'
    line5 = '        "added_time":"""),'
    line6 = 'primitives.restler_fuzzable_string("fuzzstring", quoted=True),'
    input_file = [line1, line2, line3, line4, line5, line6]
    state = 0

    for line in input_file:
        if state == 0:
            match_obj_for_search = re.search(r'primitives.restler_static_string\("""', line)
            if match_obj_for_search:
                state = 1
        elif state == 1:
            match_obj_for_search = re.search(r'"(.*)":"""\),', line)
            if match_obj_for_search:
                attribute = match_obj_for_search.group(1)
                print(attribute)  # will change
                state = 0
            # state = 0
            # match_obj_for_change = re.search(r'restler_fuzzable_string', line)
            # if match_obj_for_change:
            #     line = line.replace('restler_fuzzable_string', 'restler_fuzzable_' + match_obj_for_search.group(1))
            #     print(line)  # will change


def get_read_file_and_print_change_next_statement():
    state = 0

    with open(_file_name, "r") as input_file:
        for line in input_file:
            if state == 0:
                match_obj_for_search = re.search(r'primitives.restler_static_string\("(.*)="\),', line)
                if match_obj_for_search:
                    attribute = match_obj_for_search.group(1)
                    print(attribute)  # will change
                    state = 1
            elif state == 1:
                match_obj_for_change = re.search(r'restler_fuzzable_string', line)
                state = 0
                if match_obj_for_change:
                    line = line.replace('restler_fuzzable_string', 'restler_fuzzable_' + match_obj_for_search.group(1))
                    print(line)  # will change


def similarity_experiment():
    origin_attribute = 'contributor'

    max_value = 0.0
    temp = ''
    for category in categories:
        similar = SequenceMatcher(None, category, origin_attribute).ratio()
        if similar > max_value:
            max_value = similar
            temp = category

    print(max_value)
    print(temp)


if __name__ == '__main__':
    # execute()
    # get_regular()
    # get_change_next_statement()
    # get_read_file_and_print_change_next_statement()
    # similarity_experiment()
    post_change_next_statement()
