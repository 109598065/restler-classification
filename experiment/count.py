import re
import json
import csv
from pathlib import Path


class StatusCodeCSV:

    def __init__(self, directory) -> None:
        self._directory = directory

    def execute(self):
        self._create_csv()

    def _create_csv(self):
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Directory', '1xx', '2xx', '3xx', '4xx', '5xx'])
            writer.writerows(self._get_row_dictionaries(self._get_status_code_for_range))
            writer.writerow(['Directory', '200', '400', '404', '500'])
            writer.writerows(self._get_row_dictionaries(self._get_status_code_for_specific))

    def _get_row_dictionaries(self, function):
        rows = []
        fuzz_directories = Path(r"C:\users\main\downloads\300分鐘實驗")
        for main_directory in fuzz_directories.iterdir():
            if main_directory.is_dir():
                result_directory = Path(main_directory, 'RestlerResults')
                experiment_directory = Path(list(result_directory.iterdir()).pop())
                log_dir = Path(experiment_directory, 'logs')
                row = [main_directory] + function(log_dir)
                rows.append(row)
        return rows

    def _get_status_code_for_range(self, log_directory):
        numbers_of_status_code = []
        log_network_parser = LogNetworkParser(log_directory, r"network.testing.*.txt")
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 1'))
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 2'))
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 3'))
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 4'))
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 5'))
        return numbers_of_status_code

    def _get_status_code_for_specific(self, log_directory):
        numbers_of_status_code = []
        log_network_parser = LogNetworkParser(log_directory, r"network.testing.*.txt")
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 200'))
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 400'))
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 404'))
        numbers_of_status_code.append(log_network_parser.count_multiple_logs(r'HTTP/1.1 500'))
        return numbers_of_status_code


# def print_testing_summary(log_directory):
#     testing_summary = Path(log_directory, 'testing_summary.json')
#     log_testing_summary_parser = LogTestingSummaryParser(testing_summary)
#     print(log_testing_summary_parser.get_final_spec_coverage(), ' final_spec_coverage')
#     print(log_testing_summary_parser.get_number_of_success_request_sent(), ' number_of_success_request_sent')
#     print()


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
    status_code_csv = StatusCodeCSV(None)
    status_code_csv.execute()
