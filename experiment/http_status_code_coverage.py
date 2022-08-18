import re

path = r"D:\restler-test\300分鐘實驗\Fuzz_handwrytten_300_classification_1\RestlerResults\experiment17516\logs\network.testing.12708.1.txt"


class HttpStatusCodeCoverage:

    def __init__(self, file) -> None:
        self._file = file

    def get_numbers_of_api_cover(self, regex):
        count = 0
        request_hashes = self._get_request_hashes_set()
        for request_hash in request_hashes:
            if self._is_status_code_exist(request_hash, regex):
                count += 1
        return count

    def get_numbers_of_api(self):
        return len(self._get_request_hashes_set())

    def _get_request_hashes_set(self):
        request_hashes = set()
        with open(self._file, "r", encoding="utf-8") as input_file:
            for line in input_file:
                match_obj_for_search = re.search(r'Request hash: (.*)', line)
                if match_obj_for_search:
                    request_hash = match_obj_for_search.group(1)
                    request_hashes.add(request_hash)
        return request_hashes

    # todo: bug
    def _is_status_code_exist(self, hash_str, regex):
        state = 0
        r_hash = r'Request hash: ' + hash_str
        with open(self._file, "r", encoding="utf-8") as input_file:
            for line in input_file:
                match_obj_for_hash = re.search(r_hash, line)
                if match_obj_for_hash:
                    state = 1
                if state == 1:
                    match_obj_for_search = re.search(regex, line)
                    if match_obj_for_search:
                        return True
                if state == 1:
                    match_obj_for_terminal = re.search(r'Checker', line)
                    if match_obj_for_terminal:
                        state = 0
        return False


if __name__ == '__main__':
    http_status_code_coverage = HttpStatusCodeCoverage(path)
    print(http_status_code_coverage.get_numbers_of_api())
    print(http_status_code_coverage.get_numbers_of_api_cover(r'200 OK'))
    print(http_status_code_coverage.get_numbers_of_api_cover(r'400 Bad Request'))
    print(http_status_code_coverage.get_numbers_of_api_cover(r'404 Not Found'))
    print(http_status_code_coverage.get_numbers_of_api_cover(r'500 Internal Server Error'))
