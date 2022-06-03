""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_calendars_post_id = dependencies.DynamicVariable("_calendars_post_id")

_calendars__calendarId__acl_post_id = dependencies.DynamicVariable("_calendars__calendarId__acl_post_id")

_calendars__calendarId__events_post_attendees_0_id = dependencies.DynamicVariable("_calendars__calendarId__events_post_attendees_0_id")

_users_me_calendarList_post_id = dependencies.DynamicVariable("_users_me_calendarList_post_id")

def parse_calendarspost(data, **kwargs):
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
            temp_7262 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_calendars_post_id", temp_7262)


def parse_calendarscalendarIdaclpost(data, **kwargs):
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
            temp_8173 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_calendars__calendarId__acl_post_id", temp_8173)


def parse_calendarscalendarIdeventspost(data, **kwargs):
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
            temp_7680 = str(data["attendees"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_calendars__calendarId__events_post_attendees_0_id", temp_7680)


def parse_usersmecalendarListpost(data, **kwargs):
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
            temp_5581 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("_users_me_calendarList_post_id", temp_5581)

req_collection = requests.RequestCollection([])
# Endpoint: /calendars, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_calendarspost,
            'dependencies':
            [
                _calendars_post_id.writer()
            ]
        }

    },

],
requestId="/calendars"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "conferenceProperties":
        {
            "allowedConferenceSolutionTypes":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ]
        }
    ,
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "summary":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "conferenceProperties":
        {
            "allowedConferenceSolutionTypes":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ]
        }
    ,
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "summary":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/acl, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("acl"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("syncToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/acl"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/acl, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("acl"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "scope":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_calendarscalendarIdaclpost,
            'dependencies':
            [
                _calendars__calendarId__acl_post_id.writer()
            ]
        }

    },

],
requestId="/calendars/{calendarId}/acl"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/acl/watch, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("acl"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("syncToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "expiration":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "params":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "payload":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "resourceId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "resourceUri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/acl/watch"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/acl/{ruleId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("acl"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__acl_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/acl/{ruleId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/acl/{ruleId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("acl"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__acl_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/acl/{ruleId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/acl/{ruleId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("acl"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__acl_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "scope":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/acl/{ruleId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/acl/{ruleId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("acl"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__acl_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "scope":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/acl/{ruleId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/clear, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("clear"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/clear"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alwaysIncludeEmail="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("iCalUID="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxAttendees="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderBy="),
    primitives.restler_fuzzable_group("orderBy", ['startTime','updated']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("privateExtendedProperty="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sharedExtendedProperty="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showHiddenInvitations="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("singleEvents="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("syncToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeMax="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeMin="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeZone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("updatedMin="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("conferenceDataVersion="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxAttendees="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendUpdates="),
    primitives.restler_fuzzable_group("sendUpdates", ['all','externalOnly','none']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAttachments="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "anyoneCanAddSelf":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "attachments":
    [
        {
            "fileId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "fileUrl":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "mimeType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "attendees":
    [
        {
            "additionalGuests":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "comment":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "optional":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "organizer":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "resource":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "responseStatus":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ],
    "attendeesOmitted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "colorId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "conferenceData":
        {
            "conferenceId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "conferenceSolution":
                {
                    "iconUri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "key":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "createRequest":
                {
                    "conferenceSolutionKey":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "requestId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "status":
                        {
                            "statusCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "entryPoints":
            [
                {
                    "accessCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "entryPointFeatures":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "entryPointType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "label":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "meetingCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "passcode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "pin":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "regionCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "notes":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "parameters":
                {
                    "addOnParameters":
                        {
                            "parameters":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                        }
                }
            ,
            "signature":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "created":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "creator":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "end":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "endTimeUnspecified":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extendedProperties":
        {
            "private":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "shared":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
        }
    ,
    "gadget":
        {
            "display":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "height":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "preferences":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "width":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "guestsCanInviteOthers":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "guestsCanModify":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "guestsCanSeeOtherGuests":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "hangoutLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "htmlLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "iCalUID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "locked":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "organizer":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "originalStartTime":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "privateCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "recurrence":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "recurringEventId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "reminders":
        {
            "overrides":
            [
                {
                    "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "minutes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
            ],
            "useDefault":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "sequence":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "source":
        {
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "start":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "status":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "summary":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "transparency":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "visibility":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_calendarscalendarIdeventspost,
            'dependencies':
            [
                _calendars__calendarId__events_post_attendees_0_id.writer()
            ]
        }

    },

],
requestId="/calendars/{calendarId}/events"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/import, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("import"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("conferenceDataVersion="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAttachments="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "anyoneCanAddSelf":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "attachments":
    [
        {
            "fileId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "fileUrl":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "mimeType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "attendees":
    [
        {
            "additionalGuests":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "comment":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "optional":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "organizer":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "resource":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "responseStatus":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ],
    "attendeesOmitted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "colorId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "conferenceData":
        {
            "conferenceId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "conferenceSolution":
                {
                    "iconUri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "key":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "createRequest":
                {
                    "conferenceSolutionKey":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "requestId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "status":
                        {
                            "statusCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "entryPoints":
            [
                {
                    "accessCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "entryPointFeatures":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "entryPointType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "label":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "meetingCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "passcode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "pin":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "regionCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "notes":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "parameters":
                {
                    "addOnParameters":
                        {
                            "parameters":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                        }
                }
            ,
            "signature":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "created":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "creator":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "end":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "endTimeUnspecified":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extendedProperties":
        {
            "private":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "shared":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
        }
    ,
    "gadget":
        {
            "display":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "height":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "preferences":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "width":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "guestsCanInviteOthers":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "guestsCanModify":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "guestsCanSeeOtherGuests":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "hangoutLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "htmlLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "iCalUID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "locked":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "organizer":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "originalStartTime":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "privateCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "recurrence":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "recurringEventId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "reminders":
        {
            "overrides":
            [
                {
                    "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "minutes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
            ],
            "useDefault":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "sequence":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "source":
        {
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "start":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "status":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "summary":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "transparency":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "visibility":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/import"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/quickAdd, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("quickAdd"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("text="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendUpdates="),
    primitives.restler_fuzzable_group("sendUpdates", ['all','externalOnly','none']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/quickAdd"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/watch, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alwaysIncludeEmail="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("iCalUID="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxAttendees="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderBy="),
    primitives.restler_fuzzable_group("orderBy", ['startTime','updated']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("privateExtendedProperty="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sharedExtendedProperty="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showHiddenInvitations="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("singleEvents="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("syncToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeMax="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeMin="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeZone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("updatedMin="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "expiration":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "params":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "payload":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "resourceId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "resourceUri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/watch"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/{eventId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__events_post_attendees_0_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendUpdates="),
    primitives.restler_fuzzable_group("sendUpdates", ['all','externalOnly','none']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/{eventId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__events_post_attendees_0_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alwaysIncludeEmail="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxAttendees="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeZone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/{eventId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__events_post_attendees_0_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alwaysIncludeEmail="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("conferenceDataVersion="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxAttendees="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendUpdates="),
    primitives.restler_fuzzable_group("sendUpdates", ['all','externalOnly','none']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAttachments="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "anyoneCanAddSelf":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "attachments":
    [
        {
            "fileId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "fileUrl":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "mimeType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "attendees":
    [
        {
            "additionalGuests":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "comment":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "optional":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "organizer":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "resource":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "responseStatus":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ],
    "attendeesOmitted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "colorId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "conferenceData":
        {
            "conferenceId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "conferenceSolution":
                {
                    "iconUri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "key":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "createRequest":
                {
                    "conferenceSolutionKey":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "requestId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "status":
                        {
                            "statusCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "entryPoints":
            [
                {
                    "accessCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "entryPointFeatures":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "entryPointType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "label":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "meetingCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "passcode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "pin":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "regionCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "notes":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "parameters":
                {
                    "addOnParameters":
                        {
                            "parameters":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                        }
                }
            ,
            "signature":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "created":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "creator":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "end":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "endTimeUnspecified":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extendedProperties":
        {
            "private":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "shared":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
        }
    ,
    "gadget":
        {
            "display":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "height":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "preferences":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "width":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "guestsCanInviteOthers":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "guestsCanModify":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "guestsCanSeeOtherGuests":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "hangoutLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "htmlLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "iCalUID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "locked":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "organizer":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "originalStartTime":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "privateCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "recurrence":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "recurringEventId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "reminders":
        {
            "overrides":
            [
                {
                    "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "minutes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
            ],
            "useDefault":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "sequence":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "source":
        {
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "start":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "status":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "summary":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "transparency":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "visibility":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/{eventId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__events_post_attendees_0_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alwaysIncludeEmail="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("conferenceDataVersion="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxAttendees="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendUpdates="),
    primitives.restler_fuzzable_group("sendUpdates", ['all','externalOnly','none']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAttachments="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "anyoneCanAddSelf":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "attachments":
    [
        {
            "fileId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "fileUrl":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "mimeType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "attendees":
    [
        {
            "additionalGuests":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "comment":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "optional":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "organizer":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "resource":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "responseStatus":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ],
    "attendeesOmitted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "colorId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "conferenceData":
        {
            "conferenceId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "conferenceSolution":
                {
                    "iconUri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "key":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "createRequest":
                {
                    "conferenceSolutionKey":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "requestId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "status":
                        {
                            "statusCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "entryPoints":
            [
                {
                    "accessCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "entryPointFeatures":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "entryPointType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "label":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "meetingCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "passcode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "pin":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "regionCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uri":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "notes":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "parameters":
                {
                    "addOnParameters":
                        {
                            "parameters":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                        }
                }
            ,
            "signature":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "created":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "creator":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "end":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "endTimeUnspecified":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extendedProperties":
        {
            "private":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "shared":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
        }
    ,
    "gadget":
        {
            "display":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "height":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "link":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "preferences":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "width":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "guestsCanInviteOthers":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "guestsCanModify":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "guestsCanSeeOtherGuests":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "hangoutLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "htmlLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "iCalUID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "locked":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "organizer":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "self":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "originalStartTime":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "privateCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "recurrence":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "recurringEventId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "reminders":
        {
            "overrides":
            [
                {
                    "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "minutes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
            ],
            "useDefault":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "sequence":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "source":
        {
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "start":
        {
            "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True),
    primitives.restler_static_string(""",
            "dateTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "status":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "summary":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "transparency":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "visibility":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/{eventId}/instances, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__events_post_attendees_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("instances"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alwaysIncludeEmail="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxAttendees="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("originalStart="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeMax="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeMin="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timeZone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/{eventId}/instances"
)
req_collection.add_request(request)

# Endpoint: /calendars/{calendarId}/events/{eventId}/move, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_calendars__calendarId__events_post_attendees_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("move"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("destination="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendNotifications="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendUpdates="),
    primitives.restler_fuzzable_group("sendUpdates", ['all','externalOnly','none']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/calendars/{calendarId}/events/{eventId}/move"
)
req_collection.add_request(request)

# Endpoint: /channels/stop, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stop"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/channels/stop"
)
req_collection.add_request(request)

# Endpoint: /colors, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("colors"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/colors"
)
req_collection.add_request(request)

# Endpoint: /freeBusy, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("freeBusy"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "calendarExpansionMax":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "groupExpansionMax":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "items":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "timeMax":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "timeMin":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/freeBusy"
)
req_collection.add_request(request)

# Endpoint: /users/me/calendarList, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendarList"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("minAccessRole="),
    primitives.restler_fuzzable_group("minAccessRole", ['freeBusyReader','owner','reader','writer']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showHidden="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("syncToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/calendarList"
)
req_collection.add_request(request)

# Endpoint: /users/me/calendarList, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendarList"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("colorRgbFormat="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_usersmecalendarListpost,
            'dependencies':
            [
                _users_me_calendarList_post_id.writer()
            ]
        }

    },

],
requestId="/users/me/calendarList"
)
req_collection.add_request(request)

# Endpoint: /users/me/calendarList/watch, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendarList"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("minAccessRole="),
    primitives.restler_fuzzable_group("minAccessRole", ['freeBusyReader','owner','reader','writer']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("showHidden="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("syncToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/calendarList/watch"
)
req_collection.add_request(request)

# Endpoint: /users/me/calendarList/{calendarId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendarList"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_me_calendarList_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/calendarList/{calendarId}"
)
req_collection.add_request(request)

# Endpoint: /users/me/calendarList/{calendarId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendarList"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_me_calendarList_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/calendarList/{calendarId}"
)
req_collection.add_request(request)

# Endpoint: /users/me/calendarList/{calendarId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendarList"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_me_calendarList_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("colorRgbFormat="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "accessRole":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "backgroundColor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "colorId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "conferenceProperties":
        {
            "allowedConferenceSolutionTypes":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ]
        }
    ,
    "defaultReminders":
    [
        {
            "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "minutes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ],
    "deleted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "foregroundColor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "hidden":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "notificationSettings":
        {
            "notifications":
            [
                {
                    "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ]
        }
    ,
    "primary":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "selected":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "summary":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "summaryOverride":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/calendarList/{calendarId}"
)
req_collection.add_request(request)

# Endpoint: /users/me/calendarList/{calendarId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calendarList"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_me_calendarList_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("colorRgbFormat="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "accessRole":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "backgroundColor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "colorId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "conferenceProperties":
        {
            "allowedConferenceSolutionTypes":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ]
        }
    ,
    "defaultReminders":
    [
        {
            "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "minutes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ],
    "deleted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "etag":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "foregroundColor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "hidden":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "notificationSettings":
        {
            "notifications":
            [
                {
                    "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ]
        }
    ,
    "primary":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "selected":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "summary":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "summaryOverride":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "timeZone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/calendarList/{calendarId}"
)
req_collection.add_request(request)

# Endpoint: /users/me/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("syncToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/settings"
)
req_collection.add_request(request)

# Endpoint: /users/me/settings/watch, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("maxResults="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("syncToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/settings/watch"
)
req_collection.add_request(request)

# Endpoint: /users/me/settings/{setting}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/calendar/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("alt="),
    primitives.restler_fuzzable_group("alt", ['json'] , default_enum="json" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("oauth_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prettyPrint="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quotaUser="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("userIp="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.googleapis.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/settings/{setting}"
)
req_collection.add_request(request)
