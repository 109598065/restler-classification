import random

correct_ips = [
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

incorrect_ips = [
    '0.0.0.0',
    '256.256.256.256',
    '-1.-1.-1.-1'
]


class PublicIp:

    def get_ip(self):
        while True:
            p = random.randint(0, 255)
            q = random.randint(0, 255)
            r = random.randint(0, 255)
            s = random.randint(0, 255)
            ip = str(p) + "." + str(q) + "." + str(r) + "." + str(s)

            if p == 10 or p == 127:
                # Private IP and Loopback IP
                ip = None
            elif p == 100 and q >= 64 and q <= 127:
                # Shared Address Space
                ip = None
            elif p == 169 and q == 254:
                # APIPA
                ip = None
            elif p == 172 and q >= 16 and q <= 31:
                # Private IP  172.16.0.0 - 172.31.255.255
                ip = None
            elif p == 192 and q == 0 and r == 0:
                # 192.0.0.0/24        # RFC6890: IETF Protocol Assignments
                ip = None
            elif p == 192 and q == 0 and r == 2:
                # 192.0.2.0/24        # RFC5737: Documentation (TEST-NET-1)
                ip = None
            elif p == 192 and q == 88 and r == 99:
                # 192.88.99.0/24      # RFC3068: 6to4 Relay Anycast
                ip = None
            elif p == 192 and q == 168:
                # RFC1918: Private-Use
                ip = None
            elif p == 192 and q == 18:
                # RFC2544: Benchmarking
                ip = None
            elif p == 192 and q == 19:
                # RFC2544: Benchmarking
                ip = None
            elif p == 192 and q == 51 and r == 100:
                # RFC5737: Documentation (TEST-NET-2)
                ip = None
            elif p == 203 and r == 113:
                # RFC5737: Documentation (TEST-NET-2)
                ip = None
            elif p >= 224:
                # RFC5737: Reserved D & E
                ip = None
            if ip is not None:
                return ip
        return '1.0.0.0'


class PrivateIp:

    def get_ip(self):
        q = random.randint(0, 255)
        r = random.randint(0, 255)
        s = random.randint(0, 255)
        ips = []

        ip = "10." + str(q) + "." + str(r) + "." + str(s)
        ips.append(ip)
        ip = "172." + str(q) + "." + str(r) + "." + str(s)
        ips.append(ip)
        ip = "192.168." + str(r) + "." + str(s)
        ips.append(ip)
        ip = "127." + str(q) + "." + str(r) + "." + str(s)
        ips.append(ip)
        ip = "169.254." + str(r) + "." + str(s)
        ips.append(ip)

        return random.choice(ips)


def get_random_ips(private_ip_number=5, public_ip_number=5):
    private_ip = PrivateIp()
    private_ips = []
    for _ in range(6):
        private_ips.append(private_ip.get_ip())

    public_ip = PublicIp()
    public_ips = []
    for _ in range(24):
        public_ips.append(public_ip.get_ip())

    return private_ips + public_ips


random_ips = get_random_ips(15, 15)

ips = correct_ips + incorrect_ips + random_ips
