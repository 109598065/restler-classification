import random
import re
import socket
from dictionary.main.copy_classification.custom_value_list.resource import word

correct_domains = [
    'wikipedia.org',
    'google.com',
    'youtube.com'
    'facebook.com',
    'github.com',
    'gitlab.com',
    'spotify.com'
]

incorrect_domains = [
    'https://www.google.com.tw',
    'https://www.youtube.com',
    'https://tw.yahoo.com'
]


class DomainGenerator:

    def get_random_available_domain(self):
        while True:
            domain_name = ''.join([random.choice(word.words) for _ in range(2)]) + '.com'
            if self._is_domain_available(domain_name):
                return domain_name
        return 'not.domain.com'

    def get_random_unavailable_domain(self):
        while True:
            domain_name = random.choice(word.words) + '.com'
            if not self._is_domain_available(domain_name):
                return domain_name
        return 'example.com'

    def _is_domain_available(self, domain_name):
        whois_response = self._whois_request(domain_name)

        if re.search("Domain Name: %s" % domain_name.upper(), whois_response):
            return False
        else:
            return True

    def _whois_request(self, domain, server='whois.verisign-grs.com', port=43):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server, port))
        sock.send(("%s\r\n" % domain).encode('utf-8'))
        buff = b""
        while True:
            data = sock.recv(1024)
            if len(data) == 0:
                break
            buff += data
        sock.close()
        return buff.decode('utf-8')


def get_random_domains(available_domain_count=15, unavailable_domain_count=15):
    domain_generator = DomainGenerator()
    domains = []
    for _ in range(available_domain_count):
        domains.append(domain_generator.get_random_available_domain())
    for _ in range(unavailable_domain_count):
        domains.append(domain_generator.get_random_unavailable_domain())
    return domains


random_domains = get_random_domains(20, 20)

domains = correct_domains + incorrect_domains + random_domains
