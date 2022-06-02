import random

ips_correct = [
    '8.8.8.8',
    '8.8.4.4',
    '1.1.1.1',
    '1.0.0.1',
    '208.67.222.222',
    '208.67.220.220',
    '8.26.56.26',
    '8.20.247.20',
    '9.9.9.9',
    '149.112.112.112',
    '168.95.1.1',
    '168.95.192.1',
    '139.175.1.1',
    '61.64.127.1',
    '61.64.127.2',
    '211.78.215.137',
    '211.78.215.200',
    '101.101.101.101',
    '101.102.103.104'
]

ips_incorrect = [
    '256.256.256.256',
    '-1.-1.-1.-1'
]

ip_random_generate_correct = []
for _ in range(100):
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    d = random.randint(0, 255)
    ip_random_generate_correct.append(''.join('%s.%s.%s.%s' % (a, b, c, d)))

ips = ips_correct + ips_incorrect + ip_random_generate_correct
