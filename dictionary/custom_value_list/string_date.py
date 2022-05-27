import time
import random

string_dates_correct = [
    '2022-01-01',
    '1911-01-01'
]

string_dates_incorrect = [
    '2022-02-30',
    '2022-13-01'
]

string_dates_random_generate_correct = []
start_list = (1976, 1, 1, 0, 0, 0, 0, 0, 0)
end_list = (2022, 12, 31, 23, 59, 59, 0, 0, 0)
start = time.mktime(start_list)
end = time.mktime(end_list)
for _ in range(100):
    t = random.randint(start, end)
    date_tuple = time.localtime(t)
    date = time.strftime("%Y-%m-%d", date_tuple)
    string_dates_random_generate_correct.append(''.join(date))

string_dates = string_dates_correct + string_dates_incorrect + string_dates_random_generate_correct
