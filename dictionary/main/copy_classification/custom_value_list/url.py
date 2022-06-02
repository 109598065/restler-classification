import random
import string

urls_correct = [
    'https://www.google.com',
    'https://www.youtube.com/',
    'https://open.spotify.com/'
]

urls_incorrect = [
    'www.google.com',
    'www.youtube.com',
    'open.spotify.com'
]

url_random_generate_correct = []
i = 5
for _ in range(100):
    size = random.randint(i, i + 10)
    url_random_generate_correct.append('http://' + ''.join(random.choices(string.ascii_letters + string.digits, k=size)))
    url_random_generate_correct.append('https://' + ''.join(random.choices(string.ascii_letters + string.digits, k=size)))


urls = urls_correct + urls_incorrect + url_random_generate_correct
