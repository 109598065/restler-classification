import string
import random

emails_correct = [
    'example@example.com'
]

emails_incorrect = [
    '@example.com',
    'example@',
    '@',
    'example'
]

email_random_generate_correct = []
extensions = ['com', 'net', 'org', 'gov']
domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier']
for _ in range(100):
    winext = extensions[random.randint(0, len(extensions) - 1)]
    windom = domains[random.randint(0, len(domains) - 1)]

    acclen = random.randint(1, 20)

    winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

    finale = winacc + "@" + windom + "." + winext
    email_random_generate_correct.append(''.join(finale))

emails = emails_correct + emails_incorrect + email_random_generate_correct
