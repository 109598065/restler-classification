import time
import random

string_datetimes_correct = [
    '2019-06-26T20:20:39+00:00',
    '2019-03-15T08:00:00Z',
]

string_datetimes_incorrect = [
    '2019-06-26',
    '2019-02-30T20:20:39+00:00'
]

string_datetimes_random_generate_correct = []
start_list = (1976, 1, 1, 0, 0, 0, 0, 0, 0)
end_list = (2022, 12, 31, 23, 59, 59, 0, 0, 0)
start = time.mktime(start_list)
end = time.mktime(end_list)
for _ in range(100):
    t = random.randint(start, end)
    date_tuple = time.localtime(t)
    date = time.strftime('%Y-%m-%d %H:%M:%S', date_tuple)
    string_datetimes_random_generate_correct.append(''.join(date))

string_datetimes = string_datetimes_correct + string_datetimes_incorrect + string_datetimes_random_generate_correct
