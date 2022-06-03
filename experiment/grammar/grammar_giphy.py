""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /gifs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gifs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/gifs"
)
req_collection.add_request(request)

# Endpoint: /gifs/random, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gifs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("random"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("tag="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rating="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/gifs/random"
)
req_collection.add_request(request)

# Endpoint: /gifs/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gifs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rating="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("lang="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/gifs/search"
)
req_collection.add_request(request)

# Endpoint: /gifs/translate, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gifs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("translate"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("s="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/gifs/translate"
)
req_collection.add_request(request)

# Endpoint: /gifs/trending, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gifs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trending"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rating="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/gifs/trending"
)
req_collection.add_request(request)

# Endpoint: /gifs/{gifId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gifs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/gifs/{gifId}"
)
req_collection.add_request(request)

# Endpoint: /stickers/random, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stickers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("random"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("tag="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rating="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/stickers/random"
)
req_collection.add_request(request)

# Endpoint: /stickers/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stickers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rating="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("lang="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/stickers/search"
)
req_collection.add_request(request)

# Endpoint: /stickers/translate, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stickers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("translate"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("s="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/stickers/translate"
)
req_collection.add_request(request)

# Endpoint: /stickers/trending, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stickers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trending"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rating="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.giphy.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/stickers/trending"
)
req_collection.add_request(request)
