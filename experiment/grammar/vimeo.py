""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_groups__group_id__videos__video_id__put_name = dependencies.DynamicVariable("_groups__group_id__videos__video_id__put_name")

_ondemand_pages__ondemand_id__genres__genre_id__put_name = dependencies.DynamicVariable("_ondemand_pages__ondemand_id__genres__genre_id__put_name")

_ondemand_pages__ondemand_id__videos__video_id__put_name = dependencies.DynamicVariable("_ondemand_pages__ondemand_id__videos__video_id__put_name")

_videos__video_id__privacy_users__user_id__put_name = dependencies.DynamicVariable("_videos__video_id__privacy_users__user_id__put_name")

_videos__video_id__tags__word__put_name = dependencies.DynamicVariable("_videos__video_id__tags__word__put_name")

def parse_groupsgroup_idvideosvideo_idput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_groups__group_id__videos__video_id__put_name", temp_7262)


def parse_ondemandpagesondemand_idgenresgenre_idput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8173 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8173 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_ondemand_pages__ondemand_id__genres__genre_id__put_name", temp_8173)


def parse_ondemandpagesondemand_idvideosvideo_idput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7680 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7680 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_ondemand_pages__ondemand_id__videos__video_id__put_name", temp_7680)


def parse_videosvideo_idprivacyusersuser_idput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5581 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5581 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("_videos__video_id__privacy_users__user_id__put_name", temp_5581)


def parse_videosvideo_idtagswordput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_2060 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("_videos__video_id__tags__word__put_name", temp_2060)

req_collection = requests.RequestCollection([])
# Endpoint: , method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("openapi="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId=""
)
req_collection.add_request(request)

# Endpoint: /categories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['last_video_featured_time','name']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/categories"
)
req_collection.add_request(request)

# Endpoint: /categories/{category}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /categories/{category}/channels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','followers','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/categories/{category}/channels"
)
req_collection.add_request(request)

# Endpoint: /categories/{category}/groups, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','members','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/categories/{category}/groups"
)
req_collection.add_request(request)

# Endpoint: /categories/{category}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['conditional_featured','embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','featured','likes','plays','relevant']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/categories/{category}/videos"
)
req_collection.add_request(request)

# Endpoint: /categories/{category}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["273576296"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/categories/{category}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /channels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['featured']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','followers','relevant','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels"
)
req_collection.add_request(request)

# Endpoint: /channels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/categories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/categories"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/categories, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "channels":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/categories"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/categories/{category}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/categories/{category}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("category"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/moderators, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("moderators"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/moderators"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/moderators, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("moderators"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/moderators"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/moderators, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("moderators"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "user_uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["/users/152184"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/moderators"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/moderators, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("moderators"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "user_uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["/users/152184"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/moderators"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/moderators/{user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("moderators"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/moderators/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/moderators/{user_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("moderators"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/moderators/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/moderators/{user_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("moderators"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("user_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/moderators/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/privacy/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/privacy/users"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/privacy/users, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/privacy/users"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/privacy/users/{user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/privacy/users/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/privacy/users/{user_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("user_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/privacy/users/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/tags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/tags"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/tags, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/tags"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/tags/{word}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["awesome"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/tags/{word}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/tags/{word}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["awesome"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/tags/{word}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/tags/{word}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("word"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/tags/{word}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['moderators']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/users"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "video_uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["/videos/258684937"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("containing_uri="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['added','alphabetical','comments','date','default','duration','likes','manual','modified_time','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "video_uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["/videos/258684937"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/credits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credits"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/credits"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/credits, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/credits"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/likes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/likes"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/pictures, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/pictures"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/pictures, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/pictures"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/privacy/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/privacy/users"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/privacy/users, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/privacy/users"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/texttracks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("texttracks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/texttracks"
)
req_collection.add_request(request)

# Endpoint: /channels/{channel_id}/videos/{video_id}/texttracks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("texttracks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/{channel_id}/videos/{video_id}/texttracks"
)
req_collection.add_request(request)

# Endpoint: /contentratings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contentratings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/contentratings"
)
req_collection.add_request(request)

# Endpoint: /creativecommons, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("creativecommons"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/creativecommons"
)
req_collection.add_request(request)

# Endpoint: /groups, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['featured']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','followers','relevant','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups"
)
req_collection.add_request(request)

# Endpoint: /groups, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups"
)
req_collection.add_request(request)

# Endpoint: /groups/{group_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /groups/{group_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /groups/{group_id}/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['moderators']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{group_id}/users"
)
req_collection.add_request(request)

# Endpoint: /groups/{group_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','likes','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{group_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /groups/{group_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups__group_id__videos__video_id__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{group_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /groups/{group_id}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups__group_id__videos__video_id__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{group_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /groups/{group_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_groupsgroup_idvideosvideo_idput,
            'dependencies':
            [
                _groups__group_id__videos__video_id__put_name.writer()
            ]
        }

    },

],
requestId="/groups/{group_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /languages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("languages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['texttracks']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/languages"
)
req_collection.add_request(request)

# Endpoint: /me, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me"
)
req_collection.add_request(request)

# Endpoint: /me, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me"
)
req_collection.add_request(request)

# Endpoint: /me/albums, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','duration','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums"
)
req_collection.add_request(request)

# Endpoint: /me/albums, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("containing_uri="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("password="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["hunter1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','default','duration','likes','manual','modified_time','plays']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("weak_search="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}/videos, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "videos":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["/videos/258684937,/videos/273576296"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["196367152"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["196367152"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("password="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["hunter1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/albums/{album_id}/videos/{video_id}/set_album_thumbnail, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["196367152"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("set_album_thumbnail"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "time_code":"""),
    primitives.restler_fuzzable_number("1.23", examples=["300"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/albums/{album_id}/videos/{video_id}/set_album_thumbnail"
)
req_collection.add_request(request)

# Endpoint: /me/appearances, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("appearances"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','likes','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/appearances"
)
req_collection.add_request(request)

# Endpoint: /me/categories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','name']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/categories"
)
req_collection.add_request(request)

# Endpoint: /me/categories/{category}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /me/categories/{category}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /me/categories/{category}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("category"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /me/channels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['moderated']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','followers','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/channels"
)
req_collection.add_request(request)

# Endpoint: /me/channels/{channel_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /me/channels/{channel_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /me/channels/{channel_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("channel_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /me/customlogos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("customlogos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/customlogos"
)
req_collection.add_request(request)

# Endpoint: /me/customlogos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("customlogos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/customlogos"
)
req_collection.add_request(request)

# Endpoint: /me/customlogos/{logo_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("customlogos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/customlogos/{logo_id}"
)
req_collection.add_request(request)

# Endpoint: /me/feed, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("feed"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["280"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['appears','category_featured','channel','facebook_feed','following','group','likes','ondemand_publish','share','tagged_with','twitter_timeline','uploads']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/feed"
)
req_collection.add_request(request)

# Endpoint: /me/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/followers"
)
req_collection.add_request(request)

# Endpoint: /me/following, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['online']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/following"
)
req_collection.add_request(request)

# Endpoint: /me/following, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "users":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/following"
)
req_collection.add_request(request)

# Endpoint: /me/following/{follow_user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3766357"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/following/{follow_user_id}"
)
req_collection.add_request(request)

# Endpoint: /me/following/{follow_user_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3766357"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/following/{follow_user_id}"
)
req_collection.add_request(request)

# Endpoint: /me/following/{follow_user_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("follow_user_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/following/{follow_user_id}"
)
req_collection.add_request(request)

# Endpoint: /me/groups, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['moderated']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','members','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/groups"
)
req_collection.add_request(request)

# Endpoint: /me/groups/{group_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/groups/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /me/groups/{group_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/groups/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /me/groups/{group_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("group_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/groups/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /me/likes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','likes','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/likes"
)
req_collection.add_request(request)

# Endpoint: /me/likes/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/likes/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/likes/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/likes/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/likes/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/likes/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/ondemand/pages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['film','series']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['added','alphabetical','date','modified_time','name','publish.time','rating']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/ondemand/pages"
)
req_collection.add_request(request)

# Endpoint: /me/ondemand/pages, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "accepted_currencies":"""),
    primitives.restler_fuzzable_group("accepted_currencies", ['AUD','CAD','CHF','DKK','EUR','GBP','JPY','KRW','NOK','PLN','SEK','USD']  ,quoted=True),
    primitives.restler_static_string(""",
    "buy":
        {
            "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
            "download":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
            "price":
                {
                    "AUD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "CAD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "CHF":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "DKK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "EUR":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "GBP":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "JPY":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "KRW":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "NOK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "PLN":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "SEK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string("""
                }
        }
    ,
    "content_rating":"""),
    primitives.restler_fuzzable_group("content_rating", ['drugs','language','nudity','safe','unrated','violence']  ,quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["DARBY FOREVER follows the fantasies of Darby, a shopgirl at \"Bobbins & Notions\"."]),
    primitives.restler_static_string(""",
    "domain_link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://example.com"]),
    primitives.restler_static_string(""",
    "episodes":
        {
            "buy":
                {
                    "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
                    "download":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
                    "price":
                        {
                            "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["1.99"]),
    primitives.restler_static_string("""
                        }
                }
            ,
            "rent":
                {
                    "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
                    "period":"""),
    primitives.restler_fuzzable_group("period", ['1 week','1 year','24 hour','3 month','30 day','48 hour','6 month','72 hour']  ,quoted=True),
    primitives.restler_static_string(""",
                    "price":
                        {
                            "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string("""
                        }
                }
        }
    ,
    "link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["darbyforever"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Darby Forever"]),
    primitives.restler_static_string(""",
    "rent":
        {
            "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
            "period":"""),
    primitives.restler_fuzzable_group("period", ['1 week','1 year','24 hour','3 month','30 day','48 hour','6 month','72 hour']  ,quoted=True),
    primitives.restler_static_string(""",
            "price":
                {
                    "AUD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "CAD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "CHF":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "DKK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "EUR":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "GBP":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "JPY":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "KRW":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "NOK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "PLN":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "SEK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string("""
                }
        }
    ,
    "subscription":
        {
            "monthly":
                {
                    "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
                    "price":
                        {
                            "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["9.99"]),
    primitives.restler_static_string("""
                        }
                }
        }
    ,
    "type":"""),
    primitives.restler_fuzzable_group("type", ['film','series']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/ondemand/pages"
)
req_collection.add_request(request)

# Endpoint: /me/ondemand/purchases, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("purchases"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['all','expiring_soon','film','important','purchased','rented','series','subscription','unwatched','watched']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['added','alphabetical','date','name','purchase_time','rating','release_date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/ondemand/purchases"
)
req_collection.add_request(request)

# Endpoint: /me/ondemand/purchases/{ondemand_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("purchases"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/ondemand/purchases/{ondemand_id}"
)
req_collection.add_request(request)

# Endpoint: /me/pictures, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/pictures"
)
req_collection.add_request(request)

# Endpoint: /me/pictures, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/pictures"
)
req_collection.add_request(request)

# Endpoint: /me/pictures/{portraitset_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/pictures/{portraitset_id}"
)
req_collection.add_request(request)

# Endpoint: /me/pictures/{portraitset_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/pictures/{portraitset_id}"
)
req_collection.add_request(request)

# Endpoint: /me/pictures/{portraitset_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/pictures/{portraitset_id}"
)
req_collection.add_request(request)

# Endpoint: /me/portfolios, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/portfolios"
)
req_collection.add_request(request)

# Endpoint: /me/portfolios/{portfolio_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/portfolios/{portfolio_id}"
)
req_collection.add_request(request)

# Endpoint: /me/portfolios/{portfolio_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("containing_uri="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','default','likes','manual','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/portfolios/{portfolio_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /me/portfolios/{portfolio_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/portfolios/{portfolio_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/portfolios/{portfolio_id}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/portfolios/{portfolio_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/portfolios/{portfolio_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/portfolios/{portfolio_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/presets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/presets"
)
req_collection.add_request(request)

# Endpoint: /me/presets/{preset_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/presets/{preset_id}"
)
req_collection.add_request(request)

# Endpoint: /me/presets/{preset_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/presets/{preset_id}"
)
req_collection.add_request(request)

# Endpoint: /me/presets/{preset_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/presets/{preset_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /me/projects, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['date','default','modified_time','name']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects"
)
req_collection.add_request(request)

# Endpoint: /me/projects, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Rough cuts"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects"
)
req_collection.add_request(request)

# Endpoint: /me/projects/{project_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("should_delete_clips="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects/{project_id}"
)
req_collection.add_request(request)

# Endpoint: /me/projects/{project_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects/{project_id}"
)
req_collection.add_request(request)

# Endpoint: /me/projects/{project_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Rough cuts"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects/{project_id}"
)
req_collection.add_request(request)

# Endpoint: /me/projects/{project_id}/videos, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("should_delete_clips="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("uris="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937,/videos/273576296"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects/{project_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /me/projects/{project_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','default','duration','last_user_action_event_date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects/{project_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /me/projects/{project_id}/videos, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("uris="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937,/videos/273576296"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects/{project_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /me/projects/{project_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects/{project_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/projects/{project_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/projects/{project_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("containing_uri="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['app_only','embeddable','featured','playable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_playable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','default','duration','last_user_action_event_date','likes','modified_time','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/videos"
)
req_collection.add_request(request)

# Endpoint: /me/videos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/videos"
)
req_collection.add_request(request)

# Endpoint: /me/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/watched/videos, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watched"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/watched/videos"
)
req_collection.add_request(request)

# Endpoint: /me/watched/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watched"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/watched/videos"
)
req_collection.add_request(request)

# Endpoint: /me/watched/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watched"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/watched/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/watchlater, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchlater"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','likes','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/watchlater"
)
req_collection.add_request(request)

# Endpoint: /me/watchlater/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchlater"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/watchlater/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/watchlater/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchlater"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/watchlater/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /me/watchlater/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchlater"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/me/watchlater/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /oauth/access_token, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/oauth/access_token"
)
req_collection.add_request(request)

# Endpoint: /oauth/authorize/client, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authorize"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/oauth/authorize/client"
)
req_collection.add_request(request)

# Endpoint: /oauth/authorize/vimeo_oauth1, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authorize"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vimeo_oauth1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/oauth/authorize/vimeo_oauth1"
)
req_collection.add_request(request)

# Endpoint: /oauth/verify, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("verify"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/oauth/verify"
)
req_collection.add_request(request)

# Endpoint: /ondemand/genres, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/genres"
)
req_collection.add_request(request)

# Endpoint: /ondemand/genres/{genre_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/genres/{genre_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/genres/{genre_id}/pages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['country','my_region']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','name','publish.time','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/genres/{genre_id}/pages"
)
req_collection.add_request(request)

# Endpoint: /ondemand/genres/{genre_id}/pages/{ondemand_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/genres/{genre_id}/pages/{ondemand_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/backgrounds, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("backgrounds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/backgrounds"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/backgrounds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("backgrounds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/backgrounds"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/backgrounds/{background_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("backgrounds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/backgrounds/{background_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("backgrounds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/backgrounds/{background_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("backgrounds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/genres, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/genres"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/genres/{genre_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_ondemand_pages__ondemand_id__genres__genre_id__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/genres/{genre_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/genres/{genre_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_ondemand_pages__ondemand_id__genres__genre_id__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/genres/{genre_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/genres/{genre_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("genre_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_ondemandpagesondemand_idgenresgenre_idput,
            'dependencies':
            [
                _ondemand_pages__ondemand_id__genres__genre_id__put_name.writer()
            ]
        }

    },

],
requestId="/ondemand/pages/{ondemand_id}/genres/{genre_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/likes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['extra','main','trailer']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/likes"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/pictures, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/pictures"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/pictures, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/pictures"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/pictures/{poster_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/pictures/{poster_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/pictures/{poster_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/pictures/{poster_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/promotions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("promotions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['batch','default','single','vip']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/promotions"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/promotions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("promotions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/promotions"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/promotions/{promotion_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("promotions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/promotions/{promotion_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/promotions/{promotion_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("promotions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/promotions/{promotion_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("promotions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("codes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/regions, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("regions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/regions"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/regions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("regions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/regions"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/regions, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("regions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/regions"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/regions/{country}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("regions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["US"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/regions/{country}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/regions/{country}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("regions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["US"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/regions/{country}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/regions/{country}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("regions"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("country"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/regions/{country}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/seasons, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("seasons"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['viewable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['date','manual']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/seasons"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/seasons/{season_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("seasons"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/seasons/{season_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/seasons/{season_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("seasons"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['viewable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['date','default','manual','name','purchase_time','release_date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/seasons/{season_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['all','buy','expiring_soon','extra','main','main.viewable','rent','trailer','unwatched','viewable','watched']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['date','default','episode','manual','name','purchase_time','release_date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_ondemand_pages__ondemand_id__videos__video_id__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_ondemand_pages__ondemand_id__videos__video_id__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/pages/{ondemand_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/pages/{ondemand_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["61326"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_ondemandpagesondemand_idvideosvideo_idput,
            'dependencies':
            [
                _ondemand_pages__ondemand_id__videos__video_id__put_name.writer()
            ]
        }

    },

],
requestId="/ondemand/pages/{ondemand_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /ondemand/regions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("regions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/regions"
)
req_collection.add_request(request)

# Endpoint: /ondemand/regions/{country}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("regions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["US"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/ondemand/regions/{country}"
)
req_collection.add_request(request)

# Endpoint: /tags/{word}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["awesome"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tags/{word}"
)
req_collection.add_request(request)

# Endpoint: /tags/{word}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["awesome"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created_time','duration','name']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tags/{word}/videos"
)
req_collection.add_request(request)

# Endpoint: /tokens, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tokens"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tokens"
)
req_collection.add_request(request)

# Endpoint: /users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','followers','relevant','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','duration','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/custom_thumbnails, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("custom_thumbnails"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/custom_thumbnails"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/custom_thumbnails, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("custom_thumbnails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/custom_thumbnails"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("custom_thumbnails"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("custom_thumbnails"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("custom_thumbnails"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/logos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/logos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/logos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/logos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/logos/{logo_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/logos/{logo_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/logos/{logo_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/logos/{logo_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/logos/{logo_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/logos/{logo_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("containing_uri="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("password="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["hunter1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','default','duration','likes','manual','modified_time','plays']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("weak_search="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/videos, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "videos":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["/videos/258684937,/videos/273576296"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["196367152"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3706071"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["196367152"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("password="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["hunter1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("albums"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["196367152"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("set_album_thumbnail"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "time_code":"""),
    primitives.restler_fuzzable_number("1.23", examples=["300"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/appearances, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("appearances"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','likes','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/appearances"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/categories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','name']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/categories"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/categories/{category}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/categories/{category}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["animation"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/categories/{category}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("category"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/categories/{category}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/channels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['moderated']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','followers','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/channels"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/channels/{channel_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/channels/{channel_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["927"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/channels/{channel_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("channel_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/channels/{channel_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/customlogos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("customlogos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/customlogos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/customlogos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("customlogos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/customlogos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/customlogos/{logo_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("customlogos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/customlogos/{logo_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/feed, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("feed"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["280"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['appears','category_featured','channel','facebook_feed','following','group','likes','ondemand_publish','share','tagged_with','twitter_timeline','uploads']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/feed"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/followers"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/following, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['online']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/following"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/following, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "users":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/following"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/following/{follow_user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3766357"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/following/{follow_user_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/following/{follow_user_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["3766357"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/following/{follow_user_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/following/{follow_user_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("follow_user_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/following/{follow_user_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/groups, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['moderated']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','members','videos']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/groups"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/groups/{group_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/groups/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/groups/{group_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["1108"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/groups/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/groups/{group_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("group_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/groups/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/likes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','likes','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/likes"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/likes/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/likes/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/likes/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/likes/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/likes/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/likes/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/ondemand/pages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['film','series']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['added','alphabetical','date','modified_time','name','publish.time','rating']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/ondemand/pages"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/ondemand/pages, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "accepted_currencies":"""),
    primitives.restler_fuzzable_group("accepted_currencies", ['AUD','CAD','CHF','DKK','EUR','GBP','JPY','KRW','NOK','PLN','SEK','USD']  ,quoted=True),
    primitives.restler_static_string(""",
    "buy":
        {
            "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
            "download":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
            "price":
                {
                    "AUD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "CAD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "CHF":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "DKK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "EUR":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "GBP":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "JPY":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "KRW":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "NOK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "PLN":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "SEK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string(""",
                    "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["2.99"]),
    primitives.restler_static_string("""
                }
        }
    ,
    "content_rating":"""),
    primitives.restler_fuzzable_group("content_rating", ['drugs','language','nudity','safe','unrated','violence']  ,quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["DARBY FOREVER follows the fantasies of Darby, a shopgirl at \"Bobbins & Notions\"."]),
    primitives.restler_static_string(""",
    "domain_link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://example.com"]),
    primitives.restler_static_string(""",
    "episodes":
        {
            "buy":
                {
                    "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
                    "download":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
                    "price":
                        {
                            "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["1.99"]),
    primitives.restler_static_string("""
                        }
                }
            ,
            "rent":
                {
                    "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
                    "period":"""),
    primitives.restler_fuzzable_group("period", ['1 week','1 year','24 hour','3 month','30 day','48 hour','6 month','72 hour']  ,quoted=True),
    primitives.restler_static_string(""",
                    "price":
                        {
                            "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string("""
                        }
                }
        }
    ,
    "link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["darbyforever"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Darby Forever"]),
    primitives.restler_static_string(""",
    "rent":
        {
            "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
            "period":"""),
    primitives.restler_fuzzable_group("period", ['1 week','1 year','24 hour','3 month','30 day','48 hour','6 month','72 hour']  ,quoted=True),
    primitives.restler_static_string(""",
            "price":
                {
                    "AUD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "CAD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "CHF":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "DKK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "EUR":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "GBP":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "JPY":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "KRW":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "NOK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "PLN":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "SEK":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string(""",
                    "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.99"]),
    primitives.restler_static_string("""
                }
        }
    ,
    "subscription":
        {
            "monthly":
                {
                    "active":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
                    "price":
                        {
                            "USD":"""),
    primitives.restler_fuzzable_number("1.23", examples=["9.99"]),
    primitives.restler_static_string("""
                        }
                }
        }
    ,
    "type":"""),
    primitives.restler_fuzzable_group("type", ['film','series']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/ondemand/pages"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/ondemand/purchases, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ondemand"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("purchases"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/ondemand/purchases"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/pictures, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/pictures"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/pictures, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/pictures"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/pictures/{portraitset_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/pictures/{portraitset_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/pictures/{portraitset_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/pictures/{portraitset_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/pictures/{portraitset_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/pictures/{portraitset_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/portfolios, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/portfolios"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/portfolios/{portfolio_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/portfolios/{portfolio_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/portfolios/{portfolio_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("containing_uri="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','default','likes','manual','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/portfolios/{portfolio_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("portfolios"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/presets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/presets"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/presets/{preset_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/presets/{preset_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/presets/{preset_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/presets/{preset_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/presets/{preset_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/presets/{preset_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['date','default','modified_time','name']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Rough cuts"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects/{project_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("should_delete_clips="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects/{project_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects/{project_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects/{project_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects/{project_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Rough cuts"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects/{project_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects/{project_id}/videos, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("should_delete_clips="),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("uris="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937,/videos/273576296"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects/{project_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects/{project_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date','default','duration','last_user_action_event_date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects/{project_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects/{project_id}/videos, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("uris="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937,/videos/273576296"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects/{project_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects/{project_id}/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects/{project_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/projects/{project_id}/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/projects/{project_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/uploads/{upload}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("uploads"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("signature="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["cd89a20adde7a608f3331e71c37bdfa087bacbf3"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("video_file_id="),
    primitives.restler_fuzzable_number("1.23", examples=["1234"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/uploads/{upload}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/uploads/{upload}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("uploads"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/uploads/{upload}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("containing_uri="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/258684937"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['app_only','embeddable','featured','playable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_playable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','default','duration','last_user_action_event_date','likes','modified_time','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/videos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/videos"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/watchlater, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchlater"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['embeddable']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter_embeddable="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','likes','plays']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/watchlater"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/watchlater/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchlater"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/watchlater/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/watchlater/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchlater"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/watchlater/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /users/{user_id}/watchlater/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["152184"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchlater"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("video_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{user_id}/watchlater/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['CC','CC-BY','CC-BY-NC','CC-BY-NC-ND','CC-BY-NC-SA','CC-BY-ND','CC-BY-SA','CC0','categories','duration','in-progress','minimum_likes','trending','upload_date']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("links="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["https://vimeo.com/122375452,https://vimeo.com/273576296"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["staff picks"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','comments','date','duration','likes','plays','relevant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("uris="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["/videos/122375452,/videos/273576296"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/available_channels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("available_channels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/available_channels"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/categories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/categories"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/categories, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/categories"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/comments/{comment_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/comments/{comment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/comments/{comment_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/comments/{comment_id}/replies, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("replies"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/comments/{comment_id}/replies"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/comments/{comment_id}/replies, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("replies"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/comments/{comment_id}/replies"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/credits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credits"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stop motion"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/credits"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/credits, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/credits"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/credits/{credit_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/credits/{credit_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/credits/{credit_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/credits/{credit_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/credits/{credit_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/credits/{credit_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/likes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("likes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['alphabetical','date']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/likes"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/pictures, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/pictures"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/pictures, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/pictures"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/pictures/{picture_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/pictures/{picture_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/pictures/{picture_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/pictures/{picture_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/pictures/{picture_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pictures"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/pictures/{picture_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/presets/{preset_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/presets/{preset_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/presets/{preset_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/presets/{preset_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/presets/{preset_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presets"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("preset_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/presets/{preset_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/privacy/domains, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("domains"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/privacy/domains"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/privacy/domains/{domain}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("domains"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["example.com"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/privacy/domains/{domain}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/privacy/domains/{domain}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("domains"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("domain"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/privacy/domains/{domain}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/privacy/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/privacy/users"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/privacy/users, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/privacy/users"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/privacy/users/{user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_videos__video_id__privacy_users__user_id__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/privacy/users/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/privacy/users/{user_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privacy"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("user_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_videosvideo_idprivacyusersuser_idput,
            'dependencies':
            [
                _videos__video_id__privacy_users__user_id__put_name.writer()
            ]
        }

    },

],
requestId="/videos/{video_id}/privacy/users/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/tags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/tags"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/tags, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/tags"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/tags/{word}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_videos__video_id__tags__word__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/tags/{word}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/tags/{word}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_videos__video_id__tags__word__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/tags/{word}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/tags/{word}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("word"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_videosvideo_idtagswordput,
            'dependencies':
            [
                _videos__video_id__tags__word__put_name.writer()
            ]
        }

    },

],
requestId="/videos/{video_id}/tags/{word}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/texttracks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("texttracks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/texttracks"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/texttracks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("texttracks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/texttracks"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/texttracks/{texttrack_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("texttracks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/texttracks/{texttrack_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/texttracks/{texttrack_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("texttracks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/texttracks/{texttrack_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/texttracks/{texttrack_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("texttracks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/texttracks/{texttrack_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/timelinethumbnails, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timelinethumbnails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/timelinethumbnails"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/timelinethumbnails/{thumbnail_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timelinethumbnails"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/timelinethumbnails/{thumbnail_id}"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/versions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("versions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/versions"
)
req_collection.add_request(request)

# Endpoint: /videos/{video_id}/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_number("1.23", examples=["258684937"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['related']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_number("1.23", examples=["10"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.vimeo.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/videos/{video_id}/videos"
)
req_collection.add_request(request)
