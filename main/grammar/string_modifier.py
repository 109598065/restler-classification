import re


class StringModifier:
    def __init__(self, classification):
        self._classification = classification

    def modify_query_parameter(self, lines):
        state = 0

        for index, line in enumerate(lines):
            if state == 0:
                match_obj_for_search = re.search(r'primitives.restler_static_string\("(.*)="\),', line)
                if match_obj_for_search:
                    attribute = match_obj_for_search.group(1)
                    state = 1
            elif state == 1:
                state = 0
                match_obj_for_change = re.search(r'restler_fuzzable_string', line)
                if match_obj_for_change:
                    classify = self._classification.classify(attribute)
                    classification = classify if classify else 'string'
                    line = line.replace('restler_fuzzable_string', 'restler_fuzzable_' + classification)
                    lines[index] = line

        return lines

    def modify_body_parameter(self, lines):
        state = 0

        for index, line in enumerate(lines):
            if state == 0:
                match_obj_for_search = re.search(r'primitives.restler_static_string\("""', line)
                if match_obj_for_search:
                    state = 1
            elif state == 1:
                match_obj_for_search = re.search(r'"(.*)":"""\),', line)
                if match_obj_for_search:
                    attribute = match_obj_for_search.group(1)
                    state = 2
            elif state == 2:
                state = 0
                match_obj_for_change = re.search(r'restler_fuzzable_string', line)
                if match_obj_for_change:
                    classify = self._classification.classify(attribute)
                    classification = classify if classify else 'string'
                    line = line.replace('restler_fuzzable_string', 'restler_fuzzable_' + classification)
                    lines[index] = line

        return lines

    def modify_path_parameter(self, lines):
        state = 0

        for index, line in enumerate(lines):
            if state == 0:
                match_obj_for_search = re.search(r'primitives.restler_static_string\("/"\),', line)
                if match_obj_for_search:
                    state = 1
            elif state == 1:
                state = 0
                match_obj_for_change = re.search(r'restler_fuzzable_string', line)
                if match_obj_for_change:
                    line = line.replace('restler_fuzzable_string', 'restler_fuzzable_id')
                    lines[index] = line

        return lines
