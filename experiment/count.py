import re
import json
from pathlib import Path


def print_testing_summary(log_directory):
    testing_summary = Path(log_directory, 'testing_summary.json')
    log_testing_summary_parser = LogTestingSummaryParser(testing_summary)
    print(log_testing_summary_parser.get_final_spec_coverage(), ' final_spec_coverage')
    print(log_testing_summary_parser.get_number_of_success_request_sent(), ' number_of_success_request_sent')
    print()


def print_count_http_status_code(log_directory):
    log_network_file_extension = r"network.testing.*.txt"
    log_network_parser = LogNetworkParser(log_directory, log_network_file_extension)

    print(log_network_parser.count_multiple_logs(r'200 OK'), ' 200 OK')
    print(log_network_parser.count_multiple_logs(r'400 Bad Request'), ' 400 Bad Request')
    print(log_network_parser.count_multiple_logs(r'404 Not Found'), ' 404 Not Found')
    print(log_network_parser.count_multiple_logs(r'500 Internal Server Error'), ' 500 Internal Server Error')
    print()
    ###
    print(log_network_parser.count_multiple_logs(r'Sending: '), ' Total sent Request')
    print(log_network_parser.count_multiple_logs(r'Empty response received'), ' Empty response received')
    ###


class LogNetworkParser:

    def __init__(self, file_directory, file_extension) -> None:
        self._file_directory = file_directory
        self._file_extension = file_extension

    def count_multiple_logs(self, regex):
        count = 0
        for _ in Path(self._file_directory).glob(self._file_extension):
            count += self.count_string(_, regex)
        return count

    def count_string(self, file, regex):
        count = 0
        with open(file, "r", encoding="utf-8") as input_file:
            for line in input_file:
                match_obj_for_search = re.search(regex, line)
                if match_obj_for_search:
                    count += 1
        return count


class LogTestingSummaryParser:

    def __init__(self, file) -> None:
        self._file = file

    def get_final_spec_coverage(self):
        file = open(Path(self._file), "r")
        data = json.load(file)
        return data['final_spec_coverage']

    def get_number_of_success_request_sent(self):
        file = open(Path(self._file), "r")
        data = json.load(file)
        return data['total_requests_sent']['main_driver']


if __name__ == '__main__':
    main_directory = Path(r"D:\restler-test\300分鐘實驗\Fuzz_miataru_300_classification_1")
    result_directory = Path(main_directory, 'RestlerResults')
    experiment_directory = Path(list(result_directory.iterdir()).pop())
    log_dir = Path(experiment_directory, 'logs')

    print_testing_summary(log_dir)
    print_count_http_status_code(log_dir)
