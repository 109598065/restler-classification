import random
import secrets
import uuid

ids_correct = [
    'fuzzstring',
    '0',
    '1',
    '2',
    '3',
    '6e7f585e-e0b4-11ec-9d64-0242ac120002',
    '7927da06-e0b4-11ec-9d64-0242ac120002',
    '613ac2a5-e314-4e9b-876b-06046aca2391',
    '1bcc598d-731c-4255-82e7-fa6c6ba3a3a4'
]

ids_incorrect = [
    '_________',
    '#########',
    '$$$$$$$$$'
]


class IdGenerator:

    def get_bytes(self):
        return str(secrets.token_bytes())

    def get_int(self):
        return str(random.randint(-5, 5))

    def get_hex(self):
        return secrets.token_hex()

    def get_uuid1(self):
        return str(uuid.uuid1())

    def get_uuid4(self):
        return str(uuid.uuid4())

    def get_token(self):
        return secrets.token_urlsafe()


def get_random_ids(number=20):
    id_generator = IdGenerator()
    ids = []
    for _ in range(number):
        if _ % 6 == 0:
            ids.append(id_generator.get_bytes())
        elif _ % 6 == 1:
            ids.append(id_generator.get_int())
        elif _ % 6 == 2:
            ids.append(id_generator.get_hex())
        elif _ % 6 == 3:
            ids.append(id_generator.get_uuid1())
        elif _ % 6 == 4:
            ids.append(id_generator.get_uuid4())
        elif _ % 6 == 5:
            ids.append(id_generator.get_token())
    return ids


random_ids = get_random_ids(20)
ids = ids_correct + ids_incorrect + random_ids
