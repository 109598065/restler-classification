""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /auth/authorization, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authorization"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "login":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["john@jjf.com"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["8yfqwiuy@!$"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/auth/authorization"
)
req_collection.add_request(request)

# Endpoint: /auth/changePassword, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("changePassword"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "new_password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["myn3wp455w0rd!"]),
    primitives.restler_static_string(""",
    "old_password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["myoldpassword1234!"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/auth/changePassword"
)
req_collection.add_request(request)

# Endpoint: /auth/logout, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logout"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/auth/logout"
)
req_collection.add_request(request)

# Endpoint: /auth/register, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("register"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "discount_code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "fname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["John"]),
    primitives.restler_static_string(""",
    "lname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Smith"]),
    primitives.restler_static_string(""",
    "login":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["john@jjf.com"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["8yfqwiuy@!$"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/auth/register"
)
req_collection.add_request(request)

# Endpoint: /auth/resetPasswordRequest, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resetPasswordRequest"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "login":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["joe@bloggs.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/auth/resetPasswordRequest"
)
req_collection.add_request(request)

# Endpoint: /cards/createCustomCard, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cards"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("createCustomCard"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "card_id":"""),
    primitives.restler_fuzzable_int("1", examples=["243"]),
    primitives.restler_static_string(""",
    "cover_id":"""),
    primitives.restler_fuzzable_int("1", examples=["42"]),
    primitives.restler_static_string(""",
    "cover_size_percent":"""),
    primitives.restler_fuzzable_int("1", examples=["100"]),
    primitives.restler_static_string(""",
    "footer_align":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["center"]),
    primitives.restler_static_string(""",
    "footer_font_id":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "footer_font_size":"""),
    primitives.restler_fuzzable_int("1", examples=["16"]),
    primitives.restler_static_string(""",
    "footer_text":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Sample text for the footer"]),
    primitives.restler_static_string(""",
    "header_align":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["center"]),
    primitives.restler_static_string(""",
    "header_auto_size":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "header_font_id":"""),
    primitives.restler_fuzzable_int("1", examples=["8"]),
    primitives.restler_static_string(""",
    "header_font_size":"""),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string(""",
    "header_text":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Sample text for the header"]),
    primitives.restler_static_string(""",
    "logo_id":"""),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string(""",
    "logo_size_percent":"""),
    primitives.restler_fuzzable_int("1", examples=["100"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["my custom card design"]),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["logo"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/cards/createCustomCard"
)
req_collection.add_request(request)

# Endpoint: /cards/list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cards"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/cards/list"
)
req_collection.add_request(request)

# Endpoint: /cards/list, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cards"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "category_id":"""),
    primitives.restler_fuzzable_int("1", examples=["14"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/cards/list"
)
req_collection.add_request(request)

# Endpoint: /cards/uploadCustomLogo, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cards"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("uploadCustomLogo"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/cards/uploadCustomLogo"
)
req_collection.add_request(request)

# Endpoint: /cards/view, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cards"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("view"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "card_id":"""),
    primitives.restler_fuzzable_int("1", examples=["14"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/cards/view"
)
req_collection.add_request(request)

# Endpoint: /countries/list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("countries"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/countries/list"
)
req_collection.add_request(request)

# Endpoint: /fonts/list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("fonts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/fonts/list"
)
req_collection.add_request(request)

# Endpoint: /fonts/listForCustomizer, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("fonts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("listForCustomizer"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/fonts/listForCustomizer"
)
req_collection.add_request(request)

# Endpoint: /giftCards/view, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("giftCards"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("view"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/giftCards/view"
)
req_collection.add_request(request)

# Endpoint: /giftCards/view, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("giftCards"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("view"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/giftCards/view"
)
req_collection.add_request(request)

# Endpoint: /orders/singleStepOrder, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("singleStepOrder"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "card_id":"""),
    primitives.restler_fuzzable_int("1", examples=["3404"]),
    primitives.restler_static_string(""",
    "credit_card_id":"""),
    primitives.restler_fuzzable_int("1", examples=["34124"]),
    primitives.restler_static_string(""",
    "denomination_id":"""),
    primitives.restler_fuzzable_int("1", examples=["12"]),
    primitives.restler_static_string(""",
    "font_label":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Chill Charity"]),
    primitives.restler_static_string(""",
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["""Dear Frank,
Thank you so much for your interest in our services.
Yours,
Joe"""]),
    primitives.restler_static_string(""",
    "recipient_address1":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["123 E Main Street"]),
    primitives.restler_static_string(""",
    "recipient_address2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Second Floor"]),
    primitives.restler_static_string(""",
    "recipient_business_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Spacely Space Sprockets"]),
    primitives.restler_static_string(""",
    "recipient_city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Burlington"]),
    primitives.restler_static_string(""",
    "recipient_country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Canada"]),
    primitives.restler_static_string(""",
    "recipient_country_id":"""),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string(""",
    "recipient_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Cosmo Spacely"]),
    primitives.restler_static_string(""",
    "recipient_state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["ON"]),
    primitives.restler_static_string(""",
    "recipient_zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["L7L 0E9"]),
    primitives.restler_static_string(""",
    "sender_address1":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["1430 E Indian School Road"]),
    primitives.restler_static_string(""",
    "sender_address2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Suite 100"]),
    primitives.restler_static_string(""",
    "sender_business_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Handwrytten"]),
    primitives.restler_static_string(""",
    "sender_city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Phoenix"]),
    primitives.restler_static_string(""",
    "sender_country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["United States"]),
    primitives.restler_static_string(""",
    "sender_country_id":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "sender_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Joe Sender"]),
    primitives.restler_static_string(""",
    "sender_state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["AZ"]),
    primitives.restler_static_string(""",
    "sender_zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["12345"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orders/singleStepOrder"
)
req_collection.add_request(request)

# Endpoint: /profile/address, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("address"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/profile/address"
)
req_collection.add_request(request)

# Endpoint: /profile/deleteRecipient, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deleteRecipient"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address_id":"""),
    primitives.restler_fuzzable_int("1", examples=["549494"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["33ce76fede1a31d5ee823179f78d9882"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/profile/deleteRecipient"
)
req_collection.add_request(request)

# Endpoint: /profile/profileAddRecipient, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profileAddRecipient"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address1":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["1430 E Indian School Rd"]),
    primitives.restler_static_string(""",
    "address2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Suite 100"]),
    primitives.restler_static_string(""",
    "business_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Handwrytten LLC"]),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Phoenix"]),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["United States"]),
    primitives.restler_static_string(""",
    "country_id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Joe Smith"]),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["AZ"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["33ce76fede1a31d5ee823179f78d9882"]),
    primitives.restler_static_string(""",
    "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["85014"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/profile/profileAddRecipient"
)
req_collection.add_request(request)

# Endpoint: /profile/recipientsList, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recipientsList"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["33ce76fede1a31d5ee823179f78d9882"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/profile/recipientsList"
)
req_collection.add_request(request)

# Endpoint: /profile/updateAddress, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("updateAddress"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address1":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["1430 E Indian School Rd"]),
    primitives.restler_static_string(""",
    "address2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Suite 100"]),
    primitives.restler_static_string(""",
    "address_id":"""),
    primitives.restler_fuzzable_int("1", examples=["42"]),
    primitives.restler_static_string(""",
    "business_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Handwrytten LLC"]),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Phoenix"]),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["United States"]),
    primitives.restler_static_string(""",
    "country_id":"""),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Joe Smith"]),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["AZ"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["33ce76fede1a31d5ee823179f78d9882"]),
    primitives.restler_static_string(""",
    "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["85014"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/profile/updateAddress"
)
req_collection.add_request(request)

# Endpoint: /profile/updateRecipient, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("profile"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("updateRecipient"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address1":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["1430 E Indian School Rd"]),
    primitives.restler_static_string(""",
    "address2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Suite 100"]),
    primitives.restler_static_string(""",
    "business_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Handwrytten LLC"]),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Phoenix"]),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["United States"]),
    primitives.restler_static_string(""",
    "country_id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_int("1", examples=["549494"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Joe Smith"]),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["AZ"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["33ce76fede1a31d5ee823179f78d9882"]),
    primitives.restler_static_string(""",
    "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["85014"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/profile/updateRecipient"
)
req_collection.add_request(request)

# Endpoint: /templateCategories/list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templateCategories"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/templateCategories/list"
)
req_collection.add_request(request)

# Endpoint: /templateCategories/list, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templateCategories"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/templateCategories/list"
)
req_collection.add_request(request)

# Endpoint: /templates/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["How do I love thee?  Let me count the ways"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["My custom template"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/templates/create"
)
req_collection.add_request(request)

# Endpoint: /templates/delete, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "template_id":"""),
    primitives.restler_fuzzable_int("1", examples=["12"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/templates/delete"
)
req_collection.add_request(request)

# Endpoint: /templates/list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/templates/list"
)
req_collection.add_request(request)

# Endpoint: /templates/list, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "category_id":"""),
    primitives.restler_fuzzable_int("1", examples=["12"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/templates/list"
)
req_collection.add_request(request)

# Endpoint: /templates/update, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["How do I love thee?  Let me count the ways"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["My custom template"]),
    primitives.restler_static_string(""",
    "template_id":"""),
    primitives.restler_fuzzable_int("1", examples=["12"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/templates/update"
)
req_collection.add_request(request)

# Endpoint: /templates/view, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("view"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.handwrytten.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "template_id":"""),
    primitives.restler_fuzzable_int("1", examples=["12"]),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["fhqwfuihuifqwhiuwqfhiqwfh124"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/templates/view"
)
req_collection.add_request(request)
