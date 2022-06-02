""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_v2_images_collections_post_id = dependencies.DynamicVariable("_v2_images_collections_post_id")

_v2_videos_collections_post_id = dependencies.DynamicVariable("_v2_videos_collections_post_id")

_v2_audio_collections_post_id = dependencies.DynamicVariable("_v2_audio_collections_post_id")

_v2_images_post_id = dependencies.DynamicVariable("_v2_images_post_id")

def parse_v2imagescollectionspost(data, **kwargs):
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
        dependencies.set_variable("_v2_images_collections_post_id", temp_7262)


def parse_v2videoscollectionspost(data, **kwargs):
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
        dependencies.set_variable("_v2_videos_collections_post_id", temp_8173)


def parse_v2audiocollectionspost(data, **kwargs):
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
            temp_7680 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_v2_audio_collections_post_id", temp_7680)


def parse_v2imagespost(data, **kwargs):
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
        dependencies.set_variable("_v2_images_post_id", temp_5581)

req_collection = requests.RequestCollection([])
# Endpoint: /v2/images/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("added_date="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("added_date_start="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("added_date_end="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category="),
    primitives.restler_fuzzable_category("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("color="),
    primitives.restler_fuzzable_color("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("contributor="),
    primitives.restler_fuzzable_name("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("contributor_country="),
    primitives.restler_fuzzable_location("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height_from="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height_to="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("image_type="),
    primitives.restler_fuzzable_group("", ['photo','illustration','vector']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("license="),
    primitives.restler_fuzzable_group("", ['commercial','editorial','enhanced','sensitive','NOT enhanced','NOT sensitive'] , default_enum="commercial" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("model="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orientation="),
    primitives.restler_fuzzable_group("orientation", ['horizontal','vertical']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_model_released="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_age="),
    primitives.restler_fuzzable_group("people_age", ['infants','children','teenagers','20s','30s','40s','50s','60s','older']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_ethnicity="),
    primitives.restler_fuzzable_group("people_ethnicity", ['african','african_american','black','brazilian','chinese','caucasian','east_asian','hispanic','japanese','middle_eastern','native_american','pacific_islander','south_asian','southeast_asian','other']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_gender="),
    primitives.restler_fuzzable_group("people_gender", ['male','female','both']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_query("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("safe="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','popular','relevance','random'] , default_enum="popular" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("spellcheck_query="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("width_from="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("width_to="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/search"
)
req_collection.add_request(request)

# Endpoint: /v2/images/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_images_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="full" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/images/categories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/categories"
)
req_collection.add_request(request)

# Endpoint: /v2/images/{id}/similar, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_images_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("similar"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/{id}/similar"
)
req_collection.add_request(request)

# Endpoint: /v2/images/licenses, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("subscription_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_group("format", ['eps','jpg'] , default_enum="jpg" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("size="),
    primitives.restler_fuzzable_group("size", ['small','medium','huge','vector'] , default_enum="huge" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "images":
    [
        {
            "auth_cookie":
                {
                    "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "value":"""),
    primitives.restler_fuzzable_description("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "editorial_acknowledgement":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "format":"""),
    primitives.restler_fuzzable_group("format", ['jpg','eps']  ,quoted=True),
    primitives.restler_static_string(""",
            "image_id":"""),
    primitives.restler_static_string(_v2_images_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
            "metadata":
                """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["""{
  "customer_id": "12345",
  "geo_location": "US",
  "number_viewed": "15",
  "search_term": "dog"
}"""]),
    primitives.restler_static_string("""
            ,
            "price":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "search_id":"""),
    primitives.restler_static_string(_v2_images_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
            "show_modal":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "size":"""),
    primitives.restler_fuzzable_group("size", ['small','medium','huge','vector']  ,quoted=True),
    primitives.restler_static_string(""",
            "subscription_id":"""),
    primitives.restler_static_string(_v2_images_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
            "verification_code":"""),
    primitives.restler_fuzzable_token("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/licenses"
)
req_collection.add_request(request)

# Endpoint: /v2/images/licenses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("image_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("license="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','oldest'] , default_enum="newest" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/licenses"
)
req_collection.add_request(request)

# Endpoint: /v2/images/licenses/{id}/downloads, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("downloads"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth_cookie":
        {
            "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_description("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "show_modal":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "size":"""),
    primitives.restler_fuzzable_group("size", ['small','medium','huge','supersize']  ,quoted=True),
    primitives.restler_static_string(""",
    "verification_code":"""),
    primitives.restler_fuzzable_token("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/licenses/{id}/downloads"
)
req_collection.add_request(request)

# Endpoint: /v2/images/recommendations, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recommendations"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("max_items="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("safe="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/recommendations"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v2imagescollectionspost,
            'dependencies':
            [
                _v2_images_collections_post_id.writer()
            ]
        }

    },

],
requestId="/v2/images/collections"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("embed="),
    primitives.restler_fuzzable_group("", ['share_code','share_url']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_images_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("embed="),
    primitives.restler_fuzzable_group("", ['share_code','share_url']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("share_code="),
    primitives.restler_fuzzable_token("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/{id}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_images_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_images_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/{id}/items, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_images_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "items":
    [
        {
            "added_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "media_type":"""),
    primitives.restler_fuzzable_media_type("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/{id}/items, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_images_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("share_code="),
    primitives.restler_fuzzable_token("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/{id}/items, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_images_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("item_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/featured, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("featured"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("embed="),
    primitives.restler_fuzzable_group("embed", ['share_url']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("", ['photo','editorial','vector']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("asset_hint="),
    primitives.restler_fuzzable_group("asset_hint", ['1x','2x'] , default_enum="1x" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/featured"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/featured/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("featured"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("embed="),
    primitives.restler_fuzzable_group("embed", ['share_url']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("asset_hint="),
    primitives.restler_fuzzable_group("asset_hint", ['1x','2x'] , default_enum="1x" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/featured/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/images/collections/featured/{id}/items, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("featured"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/collections/featured/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/images/updated, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("updated"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_category("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start_date="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end_date="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','oldest'] , default_enum="newest" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images/updated"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("added_date="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("added_date_start="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("added_date_end="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("aspect_ratio="),
    primitives.restler_fuzzable_group("aspect_ratio", ['4_3','16_9','nonstandard']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category="),
    primitives.restler_fuzzable_category("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("contributor="),
    primitives.restler_fuzzable_name("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("contributor_country="),
    primitives.restler_fuzzable_location("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("duration="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("duration_from="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("duration_to="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fps="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fps_from="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fps_to="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("license="),
    primitives.restler_fuzzable_group("", ['commercial','editorial'] , default_enum="commercial" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("model="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_age="),
    primitives.restler_fuzzable_group("people_age", ['infants','children','teenagers','20s','30s','40s','50s','60s','older']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_ethnicity="),
    primitives.restler_fuzzable_group("people_ethnicity", ['african','african_american','black','brazilian','chinese','caucasian','east_asian','hispanic','japanese','middle_eastern','native_american','pacific_islander','south_asian','southeast_asian','other']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_gender="),
    primitives.restler_fuzzable_group("people_gender", ['male','female','both']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("people_model_released="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_query("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("resolution="),
    primitives.restler_fuzzable_group("resolution", ['4k','standard_definition','high_definition']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("safe="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','popular','relevance','random'] , default_enum="popular" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/search"
)
req_collection.add_request(request)

# Endpoint: /v2/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="full" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/licenses, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("subscription_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("size="),
    primitives.restler_fuzzable_group("size", ['web','sd','hd','4k'] , default_enum="web" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "videos":
    [
        {
            "auth_cookie":
                {
                    "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "value":"""),
    primitives.restler_fuzzable_description("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "editorial_acknowledgement":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "metadata":
                """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["""{
  "customer_id": "12345",
  "geo_location": "US",
  "number_viewed": "15",
  "search_term": "dog"
}"""]),
    primitives.restler_static_string("""
            ,
            "price":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "search_id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "show_modal":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "size":"""),
    primitives.restler_fuzzable_group("size", ['web','sd','hd','4k']  ,quoted=True),
    primitives.restler_static_string(""",
            "subscription_id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "video_id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/licenses"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/licenses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("video_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("license="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','oldest'] , default_enum="newest" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/licenses"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/licenses/{id}/downloads, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("downloads"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth_cookie":
        {
            "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_description("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "show_modal":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "verification_code":"""),
    primitives.restler_fuzzable_token("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/licenses/{id}/downloads"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/collections, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v2videoscollectionspost,
            'dependencies':
            [
                _v2_videos_collections_post_id.writer()
            ]
        }

    },

],
requestId="/v2/videos/collections"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/collections, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/collections"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/collections/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_videos_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/collections/{id}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_videos_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/collections/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_videos_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/categories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/categories"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/collections/{id}/items, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_videos_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "items":
    [
        {
            "added_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "media_type":"""),
    primitives.restler_fuzzable_media_type("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/collections/{id}/items, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_videos_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','oldest'] , default_enum="oldest" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/collections/{id}/items, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_videos_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("item_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/{id}/similar, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("similar"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/{id}/similar"
)
req_collection.add_request(request)

# Endpoint: /v2/videos/updated, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("updated"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("start_date="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end_date="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','oldest'] , default_enum="newest" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/videos/updated"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("artists="),
    primitives.restler_fuzzable_name("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("bpm="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("bpm_from="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("bpm_to="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("duration="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("duration_from="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("duration_to="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("genre="),
    primitives.restler_fuzzable_category("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("is_instrumental="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("instruments="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("moods="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_query("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['score','ranking_all','artist','title','bpm','freshness','duration']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort_order="),
    primitives.restler_fuzzable_group("sort_order", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("vocal_description="),
    primitives.restler_fuzzable_description("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("library="),
    primitives.restler_fuzzable_group("library", ['shutterstock','premier'] , default_enum="premier" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_language("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/search"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/genres, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("genres"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/genres"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/instruments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("instruments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/instruments"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/moods, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("moods"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/moods"
)
req_collection.add_request(request)

# Endpoint: /v2/audio, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="full" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/licenses, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("license="),
    primitives.restler_fuzzable_group("license", ['audio_standard','audio_enhanced','audio_platform'] , default_enum="audio_standard" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "audio":
    [
        {
            "audio_id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "license":"""),
    primitives.restler_fuzzable_group("license", ['audio_standard','audio_enhanced','audio_platform','premier_music_basic','premier_music_extended','premier_music_pro','premier_music_comp']  ,quoted=True),
    primitives.restler_static_string(""",
            "search_id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/licenses"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/licenses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("audio_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/licenses"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/licenses/{id}/downloads, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("downloads"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/licenses/{id}/downloads"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/collections, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v2audiocollectionspost,
            'dependencies':
            [
                _v2_audio_collections_post_id.writer()
            ]
        }

    },

],
requestId="/v2/audio/collections"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/collections, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/collections"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/collections/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_audio_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/collections/{id}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_audio_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/collections/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_audio_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/collections/{id}/items, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_audio_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "items":
    [
        {
            "added_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "media_type":"""),
    primitives.restler_fuzzable_media_type("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/collections/{id}/items, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_audio_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','oldest'] , default_enum="oldest" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/audio/collections/{id}/items, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("audio"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v2_audio_collections_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("item_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/audio/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/editorial/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("editorial"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_query("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['relevant','newest','oldest'] , default_enum="relevant" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category="),
    primitives.restler_fuzzable_category("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("country="),
    primitives.restler_fuzzable_location("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supplier_code="),
    primitives.restler_fuzzable_token("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("date_start="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("date_end="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cursor="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/editorial/search"
)
req_collection.add_request(request)

# Endpoint: /v2/editorial/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("editorial"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("country="),
    primitives.restler_fuzzable_location("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/editorial/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/editorial/licenses, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("editorial"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "country":"""),
    primitives.restler_fuzzable_location("fuzzstring", quoted=True, examples=["USA"]),
    primitives.restler_static_string(""",
    "editorial":
    [
        {
            "editorial_id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "license":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "metadata":
                """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["""{
  "customer_id": "12345",
  "geo_location": "US",
  "number_viewed": "15",
  "search_term": "dog"
}"""]),
    primitives.restler_static_string("""
            ,
            "size":"""),
    primitives.restler_fuzzable_group("size", ['small','medium','original'] , default_enum="original" ,quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/editorial/licenses"
)
req_collection.add_request(request)

# Endpoint: /v2/editorial/livefeeds, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("editorial"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("livefeeds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("country="),
    primitives.restler_fuzzable_location("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/editorial/livefeeds"
)
req_collection.add_request(request)

# Endpoint: /v2/editorial/livefeeds/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("editorial"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("livefeeds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("country="),
    primitives.restler_fuzzable_location("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/editorial/livefeeds/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/editorial/livefeeds/{id}/items, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("editorial"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("livefeeds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("country="),
    primitives.restler_fuzzable_location("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/editorial/livefeeds/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/cv/images, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cv"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "base64_image":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/cv/images"
)
req_collection.add_request(request)

# Endpoint: /v2/cv/similar/images, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cv"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("similar"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("asset_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/cv/similar/images"
)
req_collection.add_request(request)

# Endpoint: /v2/cv/similar/videos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cv"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("similar"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("asset_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['cs','da','de','en','es','fi','fr','hu','it','ja','ko','nb','nl','pl','pt','ru','sv','th','tr','zh','zh-Hant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/cv/similar/videos"
)
req_collection.add_request(request)

# Endpoint: /v2/images, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("view="),
    primitives.restler_fuzzable_group("view", ['minimal','full'] , default_enum="minimal" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/images"
)
req_collection.add_request(request)

# Endpoint: /v2/images, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "base64_image":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v2imagespost,
            'dependencies':
            [
                _v2_images_post_id.writer()
            ]
        }

    },

],
requestId="/v2/images"
)
req_collection.add_request(request)

# Endpoint: /v2/contributors, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contributors"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/contributors"
)
req_collection.add_request(request)

# Endpoint: /v2/contributors/{contributor_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contributors"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/contributors/{contributor_id}"
)
req_collection.add_request(request)

# Endpoint: /v2/contributors/{contributor_id}/collections, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contributors"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','last_updated','item_count']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/contributors/{contributor_id}/collections"
)
req_collection.add_request(request)

# Endpoint: /v2/contributors/{contributor_id}/collections/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contributors"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/contributors/{contributor_id}/collections/{id}"
)
req_collection.add_request(request)

# Endpoint: /v2/contributors/{contributor_id}/collections/{id}/items, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contributors"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("items"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','oldest']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/contributors/{contributor_id}/collections/{id}/items"
)
req_collection.add_request(request)

# Endpoint: /v2/user, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_email("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_name("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/user"
)
req_collection.add_request(request)

# Endpoint: /v2/user, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/user"
)
req_collection.add_request(request)

# Endpoint: /v2/user/access_token, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/user/access_token"
)
req_collection.add_request(request)

# Endpoint: /v2/user/subscriptions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/user/subscriptions"
)
req_collection.add_request(request)

# Endpoint: /v2/test, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("test"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("text="),
    primitives.restler_fuzzable_description("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/test"
)
req_collection.add_request(request)

# Endpoint: /v2/test/validate, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("test"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("validate"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tag="),
    primitives.restler_fuzzable_category("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("user-agent: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/test/validate"
)
req_collection.add_request(request)

# Endpoint: /v2/oauth/authorize, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authorize"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("client_id="),
    primitives.restler_fuzzable_id("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("realm="),
    primitives.restler_fuzzable_group("realm", ['customer','contributor'] , default_enum="customer" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("redirect_uri="),
    primitives.restler_fuzzable_url("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("response_type="),
    primitives.restler_fuzzable_group("response_type", ['code']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("scope="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/oauth/authorize"
)
req_collection.add_request(request)

# Endpoint: /v2/oauth/access_token, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.shutterstock.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "client_id":"""),
    primitives.restler_fuzzable_id("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "client_secret":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "code":"""),
    primitives.restler_fuzzable_token("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "grant_type":"""),
    primitives.restler_fuzzable_group("grant_type", ['authorization_code','client_credentials']  ,quoted=True),
    primitives.restler_static_string(""",
    "realm":"""),
    primitives.restler_fuzzable_group("realm", ['customer','contributor'] , default_enum="customer" ,quoted=True),
    primitives.restler_static_string(""",
    "expires":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/oauth/access_token"
)
req_collection.add_request(request)
