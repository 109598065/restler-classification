import typing
import random
import time
import string
import itertools

from custom_value_list.special_character import special_character
from custom_value_list.id import id
from custom_value_list.description import description
from custom_value_list.name import name
from custom_value_list.time_zone import time_zone
from custom_value_list.area import area
from custom_value_list.location import location
from custom_value_list.region import region
from custom_value_list.url import url
from custom_value_list.language import language
from custom_value_list.media_type import media_type
from custom_value_list.color import color
from custom_value_list.email import email
from custom_value_list.query import query
from custom_value_list.path import path
from custom_value_list.domain import domain
from custom_value_list.token import token
from custom_value_list.category import category
from custom_value_list.ip import ip
from custom_value_list.string_datetime import string_datetime
from custom_value_list.string_date import string_date

random_seed=0
# random_seed=time.time()
print(f"Value generator random seed: {random_seed}")
random.seed(random_seed)

EXAMPLE_ARG = "examples"

def gen_restler_fuzzable_string(**kwargs):   
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    
    while True:
        for i in special_character:
            yield ''.join(i)


def placeholder_value_generator():
    while True:
        yield str(random.randint(-10, 10))
        yield ''.join(random.choices(string.ascii_letters + string.digits, k=1))
    

def gen_restler_fuzzable_string_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_id(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in id:
            yield ''.join(i)
    


def gen_restler_fuzzable_id_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_name(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in name:
            yield ''.join(i)
    


def gen_restler_fuzzable_name_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_description(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in description:
            yield ''.join(i)
    


def gen_restler_fuzzable_description_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_time_zone(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in time_zone:
            yield ''.join(i)
    


def gen_restler_fuzzable_time_zone_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_area(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in area:
            yield ''.join(i)
    


def gen_restler_fuzzable_area_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_location(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in location:
            yield ''.join(i)
    


def gen_restler_fuzzable_location_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_region(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in region:
            yield ''.join(i)
    


def gen_restler_fuzzable_region_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_url(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in url:
            yield ''.join(i)
        i = 5
        for _ in range(100):
            size = random.randint(i, i + 10)
            yield 'http://' + ''.join(random.choices(string.ascii_letters + string.digits, k=size))
            yield 'https://' + ''.join(random.choices(string.ascii_letters + string.digits, k=size))
    


def gen_restler_fuzzable_url_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_language(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in language:
            yield ''.join(i)
    


def gen_restler_fuzzable_language_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_media_type(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in media_type:
            yield ''.join(i)
    


def gen_restler_fuzzable_media_type_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_color(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in color:
            yield ''.join(i)
        for _ in range(100):
            color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
            yield ''.join(color)
    


def gen_restler_fuzzable_color_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_email(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    extensions = ['com', 'net', 'org', 'gov']
    domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier']

    while True:
        for i in special_character:
            yield ''.join(i)
        for i in email:
            yield ''.join(i)
        for _ in range(100):
            winext = extensions[random.randint(0, len(extensions) - 1)]
            windom = domains[random.randint(0, len(domains) - 1)]

            acclen = random.randint(1, 20)

            winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

            finale = winacc + "@" + windom + "." + winext
            yield ''.join(finale)
    


def gen_restler_fuzzable_email_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_query(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in query:
            yield ''.join(i)
    


def gen_restler_fuzzable_query_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_path(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in path:
            yield ''.join(i)
    


def gen_restler_fuzzable_path_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_domain(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in domain:
            yield ''.join(i)
    


def gen_restler_fuzzable_domain_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_token(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in token:
            yield ''.join(i)
    


def gen_restler_fuzzable_token_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_category(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in category:
            yield ''.join(i)
    


def gen_restler_fuzzable_category_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_ip(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    while True:
        for i in special_character:
            yield ''.join(i)
        for i in ip:
            yield ''.join(i)
        for _ in range(100):
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            d = random.randint(0, 255)
            yield ''.join('%s.%s.%s.%s' % (a, b, c, d))


def gen_restler_fuzzable_ip_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_string_datetime(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    start_list = (1976, 1, 1, 0, 0, 0, 0, 0, 0)
    end_list = (2022, 12, 31, 23, 59, 59, 0, 0, 0)
    start = time.mktime(start_list)
    end = time.mktime(end_list)

    while True:
        for i in special_character:
            yield ''.join(i)
        for i in string_datetime:
            yield ''.join(i)
        for _ in range(100):
            t = random.randint(start, end)
            date_tuple = time.localtime(t)
            date = time.strftime('%Y-%m-%d %H:%M:%S', date_tuple)
            yield''.join(date)
    


def gen_restler_fuzzable_string_datetime_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_string_date(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]
    

    # Add logic here to generate values
    start_list = (1976, 1, 1, 0, 0, 0, 0, 0, 0)
    end_list = (2022, 12, 31, 23, 59, 59, 0, 0, 0)
    start = time.mktime(start_list)
    end = time.mktime(end_list)

    while True:
        for i in special_character:
            yield ''.join(i)
        for i in string_date:
            yield ''.join(i)
        for _ in range(100):
            t = random.randint(start, end)
            date_tuple = time.localtime(t)
            date = time.strftime("%Y-%m-%d", date_tuple)
            yield ''.join(date)
    


def gen_restler_fuzzable_string_date_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_datetime(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()

    


def gen_restler_fuzzable_datetime_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_date(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_date_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_uuid4(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_uuid4_unquoted(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_int(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_number(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_bool(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    


def gen_restler_fuzzable_object(**kwargs):
    example_value=None
    if EXAMPLE_ARG in kwargs:
        example_value = kwargs[EXAMPLE_ARG]

    # Add logic here to generate values
    return placeholder_value_generator()
    
value_generators = {
	"restler_fuzzable_string": gen_restler_fuzzable_string,
	"restler_fuzzable_string_unquoted": None,
	"restler_fuzzable_id": gen_restler_fuzzable_id,
	"restler_fuzzable_id_unquoted": None,
	"restler_fuzzable_name": gen_restler_fuzzable_name,
	"restler_fuzzable_name_unquoted": None,
	"restler_fuzzable_description": gen_restler_fuzzable_description,
	"restler_fuzzable_description_unquoted": None,
	"restler_fuzzable_time_zone": gen_restler_fuzzable_time_zone,
	"restler_fuzzable_time_zone_unquoted": None,
	"restler_fuzzable_area": gen_restler_fuzzable_area,
	"restler_fuzzable_area_unquoted": None,
	"restler_fuzzable_location": gen_restler_fuzzable_location,
	"restler_fuzzable_location_unquoted": None,
	"restler_fuzzable_region": gen_restler_fuzzable_region,
	"restler_fuzzable_region_unquoted": None,
	"restler_fuzzable_url": gen_restler_fuzzable_url,
	"restler_fuzzable_url_unquoted": None,
	"restler_fuzzable_language": gen_restler_fuzzable_language,
	"restler_fuzzable_language_unquoted": None,
	"restler_fuzzable_media_type": gen_restler_fuzzable_media_type,
	"restler_fuzzable_media_type_unquoted": None,
	"restler_fuzzable_color": gen_restler_fuzzable_color,
	"restler_fuzzable_color_unquoted": None,
	"restler_fuzzable_email": gen_restler_fuzzable_email,
	"restler_fuzzable_email_unquoted": None,
	"restler_fuzzable_query": gen_restler_fuzzable_query,
	"restler_fuzzable_query_unquoted": None,
	"restler_fuzzable_path": gen_restler_fuzzable_path,
	"restler_fuzzable_path_unquoted": None,
	"restler_fuzzable_domain": gen_restler_fuzzable_domain,
	"restler_fuzzable_domain_unquoted": None,
	"restler_fuzzable_token": gen_restler_fuzzable_token,
	"restler_fuzzable_token_unquoted": None,
	"restler_fuzzable_category": gen_restler_fuzzable_category,
	"restler_fuzzable_category_unquoted": None,
	"restler_fuzzable_ip": gen_restler_fuzzable_ip,
	"restler_fuzzable_ip_unquoted": None,
	"restler_fuzzable_string_datetime": gen_restler_fuzzable_datetime,
	"restler_fuzzable_string_datetime_unquoted": None,
	"restler_fuzzable_string_date": gen_restler_fuzzable_date,
	"restler_fuzzable_string_date_unquoted": None,
	"restler_fuzzable_datetime": None,
	"restler_fuzzable_datetime_unquoted": None,
	"restler_fuzzable_date": None,
	"restler_fuzzable_date_unquoted": None,
	"restler_fuzzable_uuid4": None,
	"restler_fuzzable_uuid4_unquoted": None,
	"restler_fuzzable_int": None,
	"restler_fuzzable_number": None,
	"restler_fuzzable_bool": None,
	"restler_fuzzable_object": None,
	"restler_custom_payload": {
	},
	"restler_custom_payload_unquoted": {
	},
}
