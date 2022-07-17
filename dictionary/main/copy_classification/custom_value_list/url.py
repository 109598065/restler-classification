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
for _ in range(45):
    size = random.randint(i, i + 10)
    url_random_generate_correct.append('http://' + ''.join(random.choices(string.ascii_letters + string.digits, k=size)))
    url_random_generate_correct.append('https://' + ''.join(random.choices(string.ascii_letters + string.digits, k=size)))

urls = urls_correct + urls_incorrect + url_random_generate_correct

# class UrlGenerator:
#
#     def get_status_code_200_url(self):
#         domain_generator = DomainGenerator()
#         while True:
#             try:
#                 url = 'http://' + domain_generator.get_random_unavailable_domain()
#                 request = requests.head(url, timeout=3)
#                 if request.status_code == 200:
#                     return url
#             except:
#                 pass
#
#     def get_status_code_not_200_url(self): # todo: too slow
#         domain_generator = DomainGenerator()
#         while True:
#             try:
#                 url = 'http://' + domain_generator.get_random_available_domain()
#                 requests.head(url, timeout=3)
#             except:
#                 return url
#
#
# def get_random_urls(status_code_200_number=15, status_code_not_200_number=15):
#     url_generator = UrlGenerator()
#     urls = []
#     for _ in range(status_code_200_number):
#         urls.append(url_generator.get_status_code_200_url())
#     for _ in range(status_code_not_200_number):
#         urls.append(url_generator.get_status_code_not_200_url())
#     return urls
#
#
# random_urls = get_random_urls(15, 15)
