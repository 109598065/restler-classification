""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_drives_post_backgroundImageFile_id = dependencies.DynamicVariable("_drives_post_backgroundImageFile_id")

_drives_post_backgroundImageLink = dependencies.DynamicVariable("_drives_post_backgroundImageLink")

_drives_post_colorRgb = dependencies.DynamicVariable("_drives_post_colorRgb")

_drives_post_createdTime = dependencies.DynamicVariable("_drives_post_createdTime")

_drives_post_hidden = dependencies.DynamicVariable("_drives_post_hidden")

_drives_post_id = dependencies.DynamicVariable("_drives_post_id")

_drives_post_kind = dependencies.DynamicVariable("_drives_post_kind")

_drives_post_name = dependencies.DynamicVariable("_drives_post_name")

_files_post_id = dependencies.DynamicVariable("_files_post_id")

_files__fileId__comments_post_anchor = dependencies.DynamicVariable("_files__fileId__comments_post_anchor")

_files__fileId__comments_post_content = dependencies.DynamicVariable("_files__fileId__comments_post_content")

_files__fileId__comments_post_createdTime = dependencies.DynamicVariable("_files__fileId__comments_post_createdTime")

_files__fileId__comments_post_deleted = dependencies.DynamicVariable("_files__fileId__comments_post_deleted")

_files__fileId__comments_post_id = dependencies.DynamicVariable("_files__fileId__comments_post_id")

_files__fileId__comments_post_kind = dependencies.DynamicVariable("_files__fileId__comments_post_kind")

_files__fileId__comments_post_modifiedTime = dependencies.DynamicVariable("_files__fileId__comments_post_modifiedTime")

_files__fileId__comments_post_resolved = dependencies.DynamicVariable("_files__fileId__comments_post_resolved")

_files__fileId__comments__commentId__replies_post_action = dependencies.DynamicVariable("_files__fileId__comments__commentId__replies_post_action")

_files__fileId__comments__commentId__replies_post_content = dependencies.DynamicVariable("_files__fileId__comments__commentId__replies_post_content")

_files__fileId__comments__commentId__replies_post_createdTime = dependencies.DynamicVariable("_files__fileId__comments__commentId__replies_post_createdTime")

_files__fileId__comments__commentId__replies_post_deleted = dependencies.DynamicVariable("_files__fileId__comments__commentId__replies_post_deleted")

_files__fileId__comments__commentId__replies_post_id = dependencies.DynamicVariable("_files__fileId__comments__commentId__replies_post_id")

_files__fileId__comments__commentId__replies_post_kind = dependencies.DynamicVariable("_files__fileId__comments__commentId__replies_post_kind")

_files__fileId__comments__commentId__replies_post_modifiedTime = dependencies.DynamicVariable("_files__fileId__comments__commentId__replies_post_modifiedTime")

_files__fileId__permissions_post_allowFileDiscovery = dependencies.DynamicVariable("_files__fileId__permissions_post_allowFileDiscovery")

_files__fileId__permissions_post_deleted = dependencies.DynamicVariable("_files__fileId__permissions_post_deleted")

_files__fileId__permissions_post_displayName = dependencies.DynamicVariable("_files__fileId__permissions_post_displayName")

_files__fileId__permissions_post_domain = dependencies.DynamicVariable("_files__fileId__permissions_post_domain")

_files__fileId__permissions_post_emailAddress = dependencies.DynamicVariable("_files__fileId__permissions_post_emailAddress")

_files__fileId__permissions_post_expirationTime = dependencies.DynamicVariable("_files__fileId__permissions_post_expirationTime")

_files__fileId__permissions_post_id = dependencies.DynamicVariable("_files__fileId__permissions_post_id")

_files__fileId__permissions_post_kind = dependencies.DynamicVariable("_files__fileId__permissions_post_kind")

_files__fileId__permissions_post_photoLink = dependencies.DynamicVariable("_files__fileId__permissions_post_photoLink")

_files__fileId__permissions_post_role = dependencies.DynamicVariable("_files__fileId__permissions_post_role")

_files__fileId__permissions_post_type = dependencies.DynamicVariable("_files__fileId__permissions_post_type")

_teamdrives_post_backgroundImageFile_id = dependencies.DynamicVariable("_teamdrives_post_backgroundImageFile_id")

_teamdrives_post_backgroundImageLink = dependencies.DynamicVariable("_teamdrives_post_backgroundImageLink")

_teamdrives_post_colorRgb = dependencies.DynamicVariable("_teamdrives_post_colorRgb")

_teamdrives_post_createdTime = dependencies.DynamicVariable("_teamdrives_post_createdTime")

_teamdrives_post_id = dependencies.DynamicVariable("_teamdrives_post_id")

_teamdrives_post_kind = dependencies.DynamicVariable("_teamdrives_post_kind")

_teamdrives_post_name = dependencies.DynamicVariable("_teamdrives_post_name")

def parse_drivespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None
    temp_8173 = None
    temp_7680 = None
    temp_5581 = None
    temp_2060 = None
    temp_5588 = None
    temp_9060 = None
    temp_4421 = None

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
            temp_7262 = str(data["backgroundImageFile"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8173 = str(data["backgroundImageLink"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7680 = str(data["colorRgb"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5581 = str(data["createdTime"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2060 = str(data["hidden"])
            temp_2060 = temp_2060.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5588 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9060 = str(data["kind"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4421 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262 or temp_8173 or temp_7680 or temp_5581 or temp_2060 or temp_5588 or temp_9060 or temp_4421):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_drives_post_backgroundImageFile_id", temp_7262)
    if temp_8173:
        dependencies.set_variable("_drives_post_backgroundImageLink", temp_8173)
    if temp_7680:
        dependencies.set_variable("_drives_post_colorRgb", temp_7680)
    if temp_5581:
        dependencies.set_variable("_drives_post_createdTime", temp_5581)
    if temp_2060:
        dependencies.set_variable("_drives_post_hidden", temp_2060)
    if temp_5588:
        dependencies.set_variable("_drives_post_id", temp_5588)
    if temp_9060:
        dependencies.set_variable("_drives_post_kind", temp_9060)
    if temp_4421:
        dependencies.set_variable("_drives_post_name", temp_4421)


def parse_filespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9775 = None

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
            temp_9775 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9775):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9775:
        dependencies.set_variable("_files_post_id", temp_9775)


def parse_filesfileIdcommentspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2737 = None
    temp_2919 = None
    temp_4673 = None
    temp_6326 = None
    temp_4695 = None
    temp_9821 = None
    temp_303 = None
    temp_8623 = None

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
            temp_2737 = str(data["anchor"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2919 = str(data["content"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4673 = str(data["createdTime"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6326 = str(data["deleted"])
            temp_6326 = temp_6326.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4695 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9821 = str(data["kind"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_303 = str(data["modifiedTime"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8623 = str(data["resolved"])
            temp_8623 = temp_8623.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2737 or temp_2919 or temp_4673 or temp_6326 or temp_4695 or temp_9821 or temp_303 or temp_8623):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2737:
        dependencies.set_variable("_files__fileId__comments_post_anchor", temp_2737)
    if temp_2919:
        dependencies.set_variable("_files__fileId__comments_post_content", temp_2919)
    if temp_4673:
        dependencies.set_variable("_files__fileId__comments_post_createdTime", temp_4673)
    if temp_6326:
        dependencies.set_variable("_files__fileId__comments_post_deleted", temp_6326)
    if temp_4695:
        dependencies.set_variable("_files__fileId__comments_post_id", temp_4695)
    if temp_9821:
        dependencies.set_variable("_files__fileId__comments_post_kind", temp_9821)
    if temp_303:
        dependencies.set_variable("_files__fileId__comments_post_modifiedTime", temp_303)
    if temp_8623:
        dependencies.set_variable("_files__fileId__comments_post_resolved", temp_8623)


def parse_filesfileIdcommentscommentIdrepliespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9953 = None
    temp_6771 = None
    temp_3145 = None
    temp_8169 = None
    temp_8480 = None
    temp_9919 = None
    temp_326 = None

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
            temp_9953 = str(data["action"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6771 = str(data["content"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3145 = str(data["createdTime"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8169 = str(data["deleted"])
            temp_8169 = temp_8169.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8480 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9919 = str(data["kind"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_326 = str(data["modifiedTime"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9953 or temp_6771 or temp_3145 or temp_8169 or temp_8480 or temp_9919 or temp_326):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9953:
        dependencies.set_variable("_files__fileId__comments__commentId__replies_post_action", temp_9953)
    if temp_6771:
        dependencies.set_variable("_files__fileId__comments__commentId__replies_post_content", temp_6771)
    if temp_3145:
        dependencies.set_variable("_files__fileId__comments__commentId__replies_post_createdTime", temp_3145)
    if temp_8169:
        dependencies.set_variable("_files__fileId__comments__commentId__replies_post_deleted", temp_8169)
    if temp_8480:
        dependencies.set_variable("_files__fileId__comments__commentId__replies_post_id", temp_8480)
    if temp_9919:
        dependencies.set_variable("_files__fileId__comments__commentId__replies_post_kind", temp_9919)
    if temp_326:
        dependencies.set_variable("_files__fileId__comments__commentId__replies_post_modifiedTime", temp_326)


def parse_filesfileIdpermissionspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6999 = None
    temp_5262 = None
    temp_9340 = None
    temp_6876 = None
    temp_5468 = None
    temp_811 = None
    temp_1871 = None
    temp_4533 = None
    temp_2971 = None
    temp_9885 = None
    temp_6426 = None

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
            temp_6999 = str(data["allowFileDiscovery"])
            temp_6999 = temp_6999.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5262 = str(data["deleted"])
            temp_5262 = temp_5262.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9340 = str(data["displayName"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6876 = str(data["domain"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5468 = str(data["emailAddress"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_811 = str(data["expirationTime"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_1871 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4533 = str(data["kind"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2971 = str(data["photoLink"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9885 = str(data["role"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6426 = str(data["type"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6999 or temp_5262 or temp_9340 or temp_6876 or temp_5468 or temp_811 or temp_1871 or temp_4533 or temp_2971 or temp_9885 or temp_6426):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6999:
        dependencies.set_variable("_files__fileId__permissions_post_allowFileDiscovery", temp_6999)
    if temp_5262:
        dependencies.set_variable("_files__fileId__permissions_post_deleted", temp_5262)
    if temp_9340:
        dependencies.set_variable("_files__fileId__permissions_post_displayName", temp_9340)
    if temp_6876:
        dependencies.set_variable("_files__fileId__permissions_post_domain", temp_6876)
    if temp_5468:
        dependencies.set_variable("_files__fileId__permissions_post_emailAddress", temp_5468)
    if temp_811:
        dependencies.set_variable("_files__fileId__permissions_post_expirationTime", temp_811)
    if temp_1871:
        dependencies.set_variable("_files__fileId__permissions_post_id", temp_1871)
    if temp_4533:
        dependencies.set_variable("_files__fileId__permissions_post_kind", temp_4533)
    if temp_2971:
        dependencies.set_variable("_files__fileId__permissions_post_photoLink", temp_2971)
    if temp_9885:
        dependencies.set_variable("_files__fileId__permissions_post_role", temp_9885)
    if temp_6426:
        dependencies.set_variable("_files__fileId__permissions_post_type", temp_6426)


def parse_teamdrivespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7629 = None
    temp_303 = None
    temp_3810 = None
    temp_3431 = None
    temp_9574 = None
    temp_5051 = None
    temp_7159 = None

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
            temp_7629 = str(data["backgroundImageFile"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_303 = str(data["backgroundImageLink"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3810 = str(data["colorRgb"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3431 = str(data["createdTime"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9574 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5051 = str(data["kind"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7159 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7629 or temp_303 or temp_3810 or temp_3431 or temp_9574 or temp_5051 or temp_7159):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7629:
        dependencies.set_variable("_teamdrives_post_backgroundImageFile_id", temp_7629)
    if temp_303:
        dependencies.set_variable("_teamdrives_post_backgroundImageLink", temp_303)
    if temp_3810:
        dependencies.set_variable("_teamdrives_post_colorRgb", temp_3810)
    if temp_3431:
        dependencies.set_variable("_teamdrives_post_createdTime", temp_3431)
    if temp_9574:
        dependencies.set_variable("_teamdrives_post_id", temp_9574)
    if temp_5051:
        dependencies.set_variable("_teamdrives_post_kind", temp_5051)
    if temp_7159:
        dependencies.set_variable("_teamdrives_post_name", temp_7159)

req_collection = requests.RequestCollection([])
# Endpoint: /about, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("about"),
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
requestId="/about"
)
req_collection.add_request(request)

# Endpoint: /changes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("changes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("driveId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeCorpusRemovals="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeItemsFromAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeRemoved="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeTeamDriveItems="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("restrictToMyDrive="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("spaces="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("teamDriveId="),
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
requestId="/changes"
)
req_collection.add_request(request)

# Endpoint: /changes/startPageToken, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("changes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("startPageToken"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("driveId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("teamDriveId="),
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
requestId="/changes/startPageToken"
)
req_collection.add_request(request)

# Endpoint: /changes/watch, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("changes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("driveId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeCorpusRemovals="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeItemsFromAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeRemoved="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeTeamDriveItems="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("restrictToMyDrive="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("spaces="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("teamDriveId="),
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
requestId="/changes/watch"
)
req_collection.add_request(request)

# Endpoint: /channels/stop, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
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

# Endpoint: /drives, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("drives"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useDomainAdminAccess="),
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

],
requestId="/drives"
)
req_collection.add_request(request)

# Endpoint: /drives, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("drives"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("requestId="),
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
    
    {

        'post_send':
        {
            'parser': parse_drivespost,
            'dependencies':
            [
                _drives_post_backgroundImageFile_id.writer(),
                _drives_post_backgroundImageLink.writer(),
                _drives_post_colorRgb.writer(),
                _drives_post_createdTime.writer(),
                _drives_post_hidden.writer(),
                _drives_post_id.writer(),
                _drives_post_kind.writer(),
                _drives_post_name.writer()
            ]
        }

    },

],
requestId="/drives"
)
req_collection.add_request(request)

# Endpoint: /drives/{driveId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("drives"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_drives_post_backgroundImageFile_id.reader(), quoted=False),
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
requestId="/drives/{driveId}"
)
req_collection.add_request(request)

# Endpoint: /drives/{driveId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("drives"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_drives_post_backgroundImageFile_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("useDomainAdminAccess="),
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

],
requestId="/drives/{driveId}"
)
req_collection.add_request(request)

# Endpoint: /drives/{driveId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("drives"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_drives_post_backgroundImageFile_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("useDomainAdminAccess="),
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
    "backgroundImageFile":
        {
            "id":"""),
    primitives.restler_static_string(_files_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
            "width":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "xCoordinate":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "yCoordinate":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("""
        }
    ,
    "backgroundImageLink":"""),
    primitives.restler_static_string(_drives_post_backgroundImageLink.reader(), quoted=True),
    primitives.restler_static_string(""",
    "capabilities":
        {
            "canAddChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeCopyRequiresWriterPermissionRestriction":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeDomainUsersOnlyRestriction":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeDriveBackground":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeDriveMembersOnlyRestriction":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canComment":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDeleteChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDeleteDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDownload":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canEdit":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canListChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canManageMembers":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canReadRevisions":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canRename":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canRenameDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canShare":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canTrashChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "colorRgb":"""),
    primitives.restler_static_string(_drives_post_colorRgb.reader(), quoted=True),
    primitives.restler_static_string(""",
    "createdTime":"""),
    primitives.restler_static_string(_drives_post_createdTime.reader(), quoted=True),
    primitives.restler_static_string(""",
    "hidden":"""),
    primitives.restler_static_string(_drives_post_hidden.reader(), quoted=False),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_static_string(_drives_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_static_string(_drives_post_kind.reader(), quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_drives_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "restrictions":
        {
            "adminManagedRestrictions":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "copyRequiresWriterPermission":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "domainUsersOnly":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "driveMembersOnly":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "themeId":"""),
    primitives.restler_static_string(_drives_post_id.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/drives/{driveId}"
)
req_collection.add_request(request)

# Endpoint: /drives/{driveId}/hide, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("drives"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_drives_post_backgroundImageFile_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hide"),
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
requestId="/drives/{driveId}/hide"
)
req_collection.add_request(request)

# Endpoint: /drives/{driveId}/unhide, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("drives"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_drives_post_backgroundImageFile_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unhide"),
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
requestId="/drives/{driveId}/unhide"
)
req_collection.add_request(request)

# Endpoint: /files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("corpora="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("corpus="),
    primitives.restler_fuzzable_group("corpus", ['domain','user']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("driveId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeItemsFromAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeTeamDriveItems="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderBy="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("spaces="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("teamDriveId="),
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
requestId="/files"
)
req_collection.add_request(request)

# Endpoint: /files, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ignoreDefaultVisibility="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("keepRevisionForever="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ocrLanguage="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useContentAsIndexableText="),
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
            'parser': parse_filespost,
            'dependencies':
            [
                _files_post_id.writer()
            ]
        }

    },

],
requestId="/files"
)
req_collection.add_request(request)

# Endpoint: /files/generateIds, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("generateIds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("count="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("space="),
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
requestId="/files/generateIds"
)
req_collection.add_request(request)

# Endpoint: /files/trash, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trash"),
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
requestId="/files/trash"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
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

],
requestId="/files/{fileId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("acknowledgeAbuse="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
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

],
requestId="/files/{fileId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("addParents="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("keepRevisionForever="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ocrLanguage="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("removeParents="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useContentAsIndexableText="),
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

],
requestId="/files/{fileId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("includeDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("startModifiedTime="),
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
requestId="/files/{fileId}/comments"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
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
    "anchor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "author":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "content":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "createdTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "deleted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "htmlContent":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "modifiedTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "quotedFileContent":
        {
            "mimeType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "replies":
    [
        {
            "action":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "author":
                {
                    "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "content":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "createdTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "deleted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "htmlContent":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "modifiedTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "resolved":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_filesfileIdcommentspost,
            'dependencies':
            [
                _files__fileId__comments_post_anchor.writer(),
                _files__fileId__comments_post_content.writer(),
                _files__fileId__comments_post_createdTime.writer(),
                _files__fileId__comments_post_deleted.writer(),
                _files__fileId__comments_post_id.writer(),
                _files__fileId__comments_post_kind.writer(),
                _files__fileId__comments_post_modifiedTime.writer(),
                _files__fileId__comments_post_resolved.writer()
            ]
        }

    },

],
requestId="/files/{fileId}/comments"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments/{commentId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=False),
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
requestId="/files/{fileId}/comments/{commentId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments/{commentId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("includeDeleted="),
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

],
requestId="/files/{fileId}/comments/{commentId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments/{commentId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=False),
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
    "anchor":"""),
    primitives.restler_static_string(_files__fileId__comments_post_anchor.reader(), quoted=True),
    primitives.restler_static_string(""",
    "author":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "content":"""),
    primitives.restler_static_string(_files__fileId__comments_post_content.reader(), quoted=True),
    primitives.restler_static_string(""",
    "createdTime":"""),
    primitives.restler_static_string(_files__fileId__comments_post_createdTime.reader(), quoted=True),
    primitives.restler_static_string(""",
    "deleted":"""),
    primitives.restler_static_string(_files__fileId__comments_post_deleted.reader(), quoted=False),
    primitives.restler_static_string(""",
    "htmlContent":"""),
    primitives.restler_static_string(_files__fileId__comments_post_content.reader(), quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_static_string(_files__fileId__comments_post_kind.reader(), quoted=True),
    primitives.restler_static_string(""",
    "modifiedTime":"""),
    primitives.restler_static_string(_files__fileId__comments_post_modifiedTime.reader(), quoted=True),
    primitives.restler_static_string(""",
    "quotedFileContent":"""),
    primitives.restler_static_string(_files__fileId__comments_post_content.reader(), quoted=False),
    primitives.restler_static_string(""",
    "replies":
    [
        {
            "action":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "author":
                {
                    "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "content":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "createdTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "deleted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "htmlContent":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "modifiedTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "resolved":"""),
    primitives.restler_static_string(_files__fileId__comments_post_resolved.reader(), quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/files/{fileId}/comments/{commentId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments/{commentId}/replies, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("replies"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("includeDeleted="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
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
requestId="/files/{fileId}/comments/{commentId}/replies"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments/{commentId}/replies, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("replies"),
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
    "action":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "author":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "content":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "createdTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "deleted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "htmlContent":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "modifiedTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_filesfileIdcommentscommentIdrepliespost,
            'dependencies':
            [
                _files__fileId__comments__commentId__replies_post_action.writer(),
                _files__fileId__comments__commentId__replies_post_content.writer(),
                _files__fileId__comments__commentId__replies_post_createdTime.writer(),
                _files__fileId__comments__commentId__replies_post_deleted.writer(),
                _files__fileId__comments__commentId__replies_post_id.writer(),
                _files__fileId__comments__commentId__replies_post_kind.writer(),
                _files__fileId__comments__commentId__replies_post_modifiedTime.writer()
            ]
        }

    },

],
requestId="/files/{fileId}/comments/{commentId}/replies"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments/{commentId}/replies/{replyId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("replies"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_id.reader(), quoted=False),
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
requestId="/files/{fileId}/comments/{commentId}/replies/{replyId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments/{commentId}/replies/{replyId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("replies"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("includeDeleted="),
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

],
requestId="/files/{fileId}/comments/{commentId}/replies/{replyId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/comments/{commentId}/replies/{replyId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("replies"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_id.reader(), quoted=False),
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
    "action":"""),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_action.reader(), quoted=True),
    primitives.restler_static_string(""",
    "author":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "content":"""),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_content.reader(), quoted=True),
    primitives.restler_static_string(""",
    "createdTime":"""),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_createdTime.reader(), quoted=True),
    primitives.restler_static_string(""",
    "deleted":"""),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_deleted.reader(), quoted=False),
    primitives.restler_static_string(""",
    "htmlContent":"""),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_content.reader(), quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_kind.reader(), quoted=True),
    primitives.restler_static_string(""",
    "modifiedTime":"""),
    primitives.restler_static_string(_files__fileId__comments__commentId__replies_post_modifiedTime.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/files/{fileId}/comments/{commentId}/replies/{replyId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/copy, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("copy"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ignoreDefaultVisibility="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("keepRevisionForever="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ocrLanguage="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
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
    "appProperties":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "capabilities":
        {
            "canAddChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeCopyRequiresWriterPermission":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeViewersCanCopyContent":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canComment":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDelete":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDeleteChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDownload":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canEdit":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canListChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canModifyContent":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveChildrenOutOfDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveChildrenOutOfTeamDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveChildrenWithinDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveChildrenWithinTeamDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveItemIntoTeamDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveItemOutOfDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveItemOutOfTeamDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveItemWithinDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveItemWithinTeamDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canMoveTeamDriveItem":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canReadDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canReadRevisions":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canReadTeamDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canRemoveChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canRename":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canShare":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canTrash":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canTrashChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canUntrash":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "contentHints":
        {
            "indexableText":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "thumbnail":
                {
                    "image":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "mimeType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "copyRequiresWriterPermission":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "createdTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "driveId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "explicitlyTrashed":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "exportLinks":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "fileExtension":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "folderColorRgb":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "fullFileExtension":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "hasAugmentedPermissions":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "hasThumbnail":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "headRevisionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "iconLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "imageMediaMetadata":
        {
            "aperture":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "cameraMake":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "cameraModel":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "colorSpace":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "exposureBias":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "exposureMode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "exposureTime":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "flashUsed":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "focalLength":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "height":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "isoSpeed":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "lens":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "location":
                {
                    "altitude":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
                    "latitude":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
                    "longitude":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("""
                }
            ,
            "maxApertureValue":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "meteringMode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "rotation":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "sensor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "subjectDistance":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "time":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "whiteBalance":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "width":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "isAppAuthorized":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "lastModifyingUser":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "md5Checksum":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "mimeType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "modifiedByMe":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "modifiedByMeTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "modifiedTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "originalFilename":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "ownedByMe":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "owners":
    [
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "parents":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "permissionIds":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "permissions":
    [
        {
            "allowFileDiscovery":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_allowFileDiscovery.reader(), quoted=False),
    primitives.restler_static_string(""",
            "deleted":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_deleted.reader(), quoted=False),
    primitives.restler_static_string(""",
            "displayName":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_displayName.reader(), quoted=True),
    primitives.restler_static_string(""",
            "domain":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_domain.reader(), quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_emailAddress.reader(), quoted=True),
    primitives.restler_static_string(""",
            "expirationTime":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_expirationTime.reader(), quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_kind.reader(), quoted=True),
    primitives.restler_static_string(""",
            "permissionDetails":
            [
                {
                    "inherited":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "inheritedFrom":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "permissionType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "photoLink":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_photoLink.reader(), quoted=True),
    primitives.restler_static_string(""",
            "role":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_role.reader(), quoted=True),
    primitives.restler_static_string(""",
            "teamDrivePermissionDetails":
            [
                {
                    "inherited":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "inheritedFrom":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "teamDrivePermissionType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "type":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_type.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "properties":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "quotaBytesUsed":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "shared":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "sharedWithMeTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "sharingUser":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "size":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "spaces":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "starred":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "teamDriveId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "thumbnailLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "thumbnailVersion":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "trashed":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "trashedTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "trashingUser":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "version":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "videoMediaMetadata":
        {
            "durationMillis":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "height":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "width":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "viewedByMe":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "viewedByMeTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "viewersCanCopyContent":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "webContentLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "webViewLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "writersCanShare":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/files/{fileId}/copy"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/export, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("export"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("mimeType="),
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
requestId="/files/{fileId}/export"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/permissions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permissions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useDomainAdminAccess="),
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

],
requestId="/files/{fileId}/permissions"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/permissions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permissions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("emailMessage="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sendNotificationEmail="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("transferOwnership="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useDomainAdminAccess="),
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
    "allowFileDiscovery":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "deleted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "domain":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "expirationTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "permissionDetails":
    [
        {
            "inherited":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "inheritedFrom":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "permissionType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "teamDrivePermissionDetails":
    [
        {
            "inherited":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "inheritedFrom":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "teamDrivePermissionType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_filesfileIdpermissionspost,
            'dependencies':
            [
                _files__fileId__permissions_post_allowFileDiscovery.writer(),
                _files__fileId__permissions_post_deleted.writer(),
                _files__fileId__permissions_post_displayName.writer(),
                _files__fileId__permissions_post_domain.writer(),
                _files__fileId__permissions_post_emailAddress.writer(),
                _files__fileId__permissions_post_expirationTime.writer(),
                _files__fileId__permissions_post_id.writer(),
                _files__fileId__permissions_post_kind.writer(),
                _files__fileId__permissions_post_photoLink.writer(),
                _files__fileId__permissions_post_role.writer(),
                _files__fileId__permissions_post_type.writer()
            ]
        }

    },

],
requestId="/files/{fileId}/permissions"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/permissions/{permissionId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permissions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__permissions_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useDomainAdminAccess="),
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

],
requestId="/files/{fileId}/permissions/{permissionId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/permissions/{permissionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permissions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__permissions_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useDomainAdminAccess="),
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

],
requestId="/files/{fileId}/permissions/{permissionId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/permissions/{permissionId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permissions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files__fileId__permissions_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("removeExpiration="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("transferOwnership="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useDomainAdminAccess="),
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
    "allowFileDiscovery":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_allowFileDiscovery.reader(), quoted=False),
    primitives.restler_static_string(""",
    "deleted":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_deleted.reader(), quoted=False),
    primitives.restler_static_string(""",
    "displayName":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_displayName.reader(), quoted=True),
    primitives.restler_static_string(""",
    "domain":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_domain.reader(), quoted=True),
    primitives.restler_static_string(""",
    "emailAddress":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_emailAddress.reader(), quoted=True),
    primitives.restler_static_string(""",
    "expirationTime":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_expirationTime.reader(), quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_kind.reader(), quoted=True),
    primitives.restler_static_string(""",
    "permissionDetails":
    [
        {
            "inherited":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "inheritedFrom":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "permissionType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "photoLink":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_photoLink.reader(), quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_role.reader(), quoted=True),
    primitives.restler_static_string(""",
    "teamDrivePermissionDetails":
    [
        {
            "inherited":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "inheritedFrom":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "teamDrivePermissionType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "type":"""),
    primitives.restler_static_string(_files__fileId__permissions_post_type.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/files/{fileId}/permissions/{permissionId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/revisions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("revisions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
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
requestId="/files/{fileId}/revisions"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/revisions/{revisionId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("revisions"),
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
requestId="/files/{fileId}/revisions/{revisionId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/revisions/{revisionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("revisions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("acknowledgeAbuse="),
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

],
requestId="/files/{fileId}/revisions/{revisionId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/revisions/{revisionId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("revisions"),
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
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "exportLinks":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "keepForever":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "lastModifyingUser":
        {
            "displayName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "emailAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "me":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "permissionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "photoLink":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "md5Checksum":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "mimeType":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "modifiedTime":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "originalFilename":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "publishAuto":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "published":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "publishedOutsideDomain":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "size":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/files/{fileId}/revisions/{revisionId}"
)
req_collection.add_request(request)

# Endpoint: /files/{fileId}/watch, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_files_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("acknowledgeAbuse="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsAllDrives="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("supportsTeamDrives="),
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
requestId="/files/{fileId}/watch"
)
req_collection.add_request(request)

# Endpoint: /teamdrives, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teamdrives"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageToken="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("useDomainAdminAccess="),
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

],
requestId="/teamdrives"
)
req_collection.add_request(request)

# Endpoint: /teamdrives, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teamdrives"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("requestId="),
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
    
    {

        'post_send':
        {
            'parser': parse_teamdrivespost,
            'dependencies':
            [
                _teamdrives_post_backgroundImageFile_id.writer(),
                _teamdrives_post_backgroundImageLink.writer(),
                _teamdrives_post_colorRgb.writer(),
                _teamdrives_post_createdTime.writer(),
                _teamdrives_post_id.writer(),
                _teamdrives_post_kind.writer(),
                _teamdrives_post_name.writer()
            ]
        }

    },

],
requestId="/teamdrives"
)
req_collection.add_request(request)

# Endpoint: /teamdrives/{teamDriveId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teamdrives"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teamdrives_post_backgroundImageFile_id.reader(), quoted=False),
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
requestId="/teamdrives/{teamDriveId}"
)
req_collection.add_request(request)

# Endpoint: /teamdrives/{teamDriveId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teamdrives"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teamdrives_post_backgroundImageFile_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("useDomainAdminAccess="),
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

],
requestId="/teamdrives/{teamDriveId}"
)
req_collection.add_request(request)

# Endpoint: /teamdrives/{teamDriveId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/drive/v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teamdrives"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teamdrives_post_backgroundImageFile_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("useDomainAdminAccess="),
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
    "backgroundImageFile":
        {
            "id":"""),
    primitives.restler_static_string(_files_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
            "width":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "xCoordinate":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "yCoordinate":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("""
        }
    ,
    "backgroundImageLink":"""),
    primitives.restler_static_string(_teamdrives_post_backgroundImageLink.reader(), quoted=True),
    primitives.restler_static_string(""",
    "capabilities":
        {
            "canAddChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeCopyRequiresWriterPermissionRestriction":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeDomainUsersOnlyRestriction":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeTeamDriveBackground":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canChangeTeamMembersOnlyRestriction":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canComment":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDeleteChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDeleteTeamDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canDownload":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canEdit":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canListChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canManageMembers":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canReadRevisions":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canRemoveChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canRename":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canRenameTeamDrive":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canShare":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "canTrashChildren":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "colorRgb":"""),
    primitives.restler_static_string(_teamdrives_post_colorRgb.reader(), quoted=True),
    primitives.restler_static_string(""",
    "createdTime":"""),
    primitives.restler_static_string(_teamdrives_post_createdTime.reader(), quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_static_string(_teamdrives_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_static_string(_teamdrives_post_kind.reader(), quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_teamdrives_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "restrictions":
        {
            "adminManagedRestrictions":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "copyRequiresWriterPermission":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "domainUsersOnly":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "teamMembersOnly":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "themeId":"""),
    primitives.restler_static_string(_teamdrives_post_id.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teamdrives/{teamDriveId}"
)
req_collection.add_request(request)
