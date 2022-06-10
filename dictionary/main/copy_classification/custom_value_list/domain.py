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

    def whois_request(self, domain, server='whois.verisign-grs.com', port=43):
        """
        Carries out the WHOIS request for a particular domain name, against a particular registrar.
        This is not .com specific.
        """
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

    def is_domain_available(self, domain_name):
        """
        'Builds' the domain name (just appends .com as that's all I check right now)
        then checks its WHOIS status - assuming we don't skip this in the args.
        """
        whois_response = self.whois_request(domain_name)

        if re.search("Domain Name: %s" % domain_name.upper(), whois_response):
            return False
        else:
            return True


def get_random_domains(available_domain_count=15, not_available_domain_count=15):
    domain_generator = DomainGenerator()

    available_domains = []
    while len(available_domains) < available_domain_count:
        domain_name = ''.join([random.choice(word.words) for _ in range(2)]) + '.com'
        if domain_generator.is_domain_available(domain_name):
            available_domains.append(domain_name)

    not_available_domains = []
    while len(not_available_domains) < not_available_domain_count:
        domain_name = random.choice(word.words) + '.com'
        if not domain_generator.is_domain_available(domain_name):
            not_available_domains.append(domain_name)

    domains = available_domains + not_available_domains
    return domains


random_domains = get_random_domains(20, 20)

domains = correct_domains + incorrect_domains + random_domains
