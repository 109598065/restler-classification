""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /ip, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ip"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ip"
)
req_collection.add_request(request)

# Endpoint: /ip.txt, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ip.txt"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ip.txt"
)
req_collection.add_request(request)

# Endpoint: /ip/{ipv4}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ip"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ip/{ipv4}"
)
req_collection.add_request(request)

# Endpoint: /ip/{ipv4}.txt, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ip"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ip/{ipv4}.txt"
)
req_collection.add_request(request)

# Endpoint: /timezone, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/timezone"
)
req_collection.add_request(request)

# Endpoint: /timezone.txt, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone.txt"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/timezone.txt"
)
req_collection.add_request(request)

# Endpoint: /timezone/{area}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/timezone/{area}"
)
req_collection.add_request(request)

# Endpoint: /timezone/{area}.txt, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/timezone/{area}.txt"
)
req_collection.add_request(request)

# Endpoint: /timezone/{area}/{location}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/timezone/{area}/{location}"
)
req_collection.add_request(request)

# Endpoint: /timezone/{area}/{location}.txt, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/timezone/{area}/{location}.txt"
)
req_collection.add_request(request)

# Endpoint: /timezone/{area}/{location}/{region}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/timezone/{area}/{location}/{region}"
)
req_collection.add_request(request)

# Endpoint: /timezone/{area}/{location}/{region}.txt, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timezone"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: worldtimeapi.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/timezone/{area}/{location}/{region}.txt"
)
req_collection.add_request(request)
