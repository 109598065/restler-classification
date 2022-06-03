""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_repositories__username___repo_slug__put_name = dependencies.DynamicVariable("_repositories__username___repo_slug__put_name")

_repositories__username___repo_slug__branch_restrictions_post_id = dependencies.DynamicVariable("_repositories__username___repo_slug__branch_restrictions_post_id")

_repositories__username___repo_slug__commit__node__statuses_build_post_key = dependencies.DynamicVariable("_repositories__username___repo_slug__commit__node__statuses_build_post_key")

_repositories__username___repo_slug__issues_post_component_id = dependencies.DynamicVariable("_repositories__username___repo_slug__issues_post_component_id")

_repositories__username___repo_slug__pipelines_post_creator_uuid = dependencies.DynamicVariable("_repositories__username___repo_slug__pipelines_post_creator_uuid")

_repositories__username___repo_slug__pipelines_config_ssh_known_hosts_post_uuid = dependencies.DynamicVariable("_repositories__username___repo_slug__pipelines_config_ssh_known_hosts_post_uuid")

_repositories__username___repo_slug__pipelines_config_variables_post_uuid = dependencies.DynamicVariable("_repositories__username___repo_slug__pipelines_config_variables_post_uuid")

_repositories__username___repo_slug__pullrequests_post_id = dependencies.DynamicVariable("_repositories__username___repo_slug__pullrequests_post_id")

_repositories__username___repo_slug__refs_tags_post_name = dependencies.DynamicVariable("_repositories__username___repo_slug__refs_tags_post_name")

_snippets_post_creator_username = dependencies.DynamicVariable("_snippets_post_creator_username")

_snippets__username___encoded_id__put_id = dependencies.DynamicVariable("_snippets__username___encoded_id__put_id")

_snippets__username___encoded_id__comments_post_id = dependencies.DynamicVariable("_snippets__username___encoded_id__comments_post_id")

_snippets__username___encoded_id___node_id__put_id = dependencies.DynamicVariable("_snippets__username___encoded_id___node_id__put_id")

_teams__owner__projects_post_key = dependencies.DynamicVariable("_teams__owner__projects_post_key")

_teams__username__pipelines_config_variables_post_uuid = dependencies.DynamicVariable("_teams__username__pipelines_config_variables_post_uuid")

_users__username__pipelines_config_variables_post_uuid = dependencies.DynamicVariable("_users__username__pipelines_config_variables_post_uuid")

def parse_repositoriesusernamerepo_slugput(data, **kwargs):
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
        dependencies.set_variable("_repositories__username___repo_slug__put_name", temp_7262)


def parse_repositoriesusernamerepo_slugbranchrestrictionspost(data, **kwargs):
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
        dependencies.set_variable("_repositories__username___repo_slug__branch_restrictions_post_id", temp_8173)


def parse_repositoriesusernamerepo_slugcommitnodestatusesbuildpost(data, **kwargs):
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
            temp_7680 = str(data["key"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_repositories__username___repo_slug__commit__node__statuses_build_post_key", temp_7680)


def parse_repositoriesusernamerepo_slugissuespost(data, **kwargs):
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
            temp_5581 = str(data["component"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("_repositories__username___repo_slug__issues_post_component_id", temp_5581)


def parse_repositoriesusernamerepo_slugpipelinespost(data, **kwargs):
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
            temp_2060 = str(data["creator"]["uuid"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("_repositories__username___repo_slug__pipelines_post_creator_uuid", temp_2060)


def parse_repositoriesusernamerepo_slugpipelines_configsshknown_hostspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5588 = None

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
            temp_5588 = str(data["uuid"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5588):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5588:
        dependencies.set_variable("_repositories__username___repo_slug__pipelines_config_ssh_known_hosts_post_uuid", temp_5588)


def parse_repositoriesusernamerepo_slugpipelines_configvariablespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9060 = None

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
            temp_9060 = str(data["uuid"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9060:
        dependencies.set_variable("_repositories__username___repo_slug__pipelines_config_variables_post_uuid", temp_9060)


def parse_repositoriesusernamerepo_slugpullrequestspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
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
            temp_4421 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4421):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4421:
        dependencies.set_variable("_repositories__username___repo_slug__pullrequests_post_id", temp_4421)


def parse_repositoriesusernamerepo_slugrefstagspost(data, **kwargs):
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
            temp_9775 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9775):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9775:
        dependencies.set_variable("_repositories__username___repo_slug__refs_tags_post_name", temp_9775)


def parse_snippetspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2737 = None

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
            temp_2737 = str(data["creator"]["username"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2737):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2737:
        dependencies.set_variable("_snippets_post_creator_username", temp_2737)


def parse_snippetsusernameencoded_idput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2919 = None

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
            temp_2919 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2919):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2919:
        dependencies.set_variable("_snippets__username___encoded_id__put_id", temp_2919)


def parse_snippetsusernameencoded_idcommentspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4673 = None

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
            temp_4673 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4673):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4673:
        dependencies.set_variable("_snippets__username___encoded_id__comments_post_id", temp_4673)


def parse_snippetsusernameencoded_idnode_idput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6326 = None

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
            temp_6326 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6326):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6326:
        dependencies.set_variable("_snippets__username___encoded_id___node_id__put_id", temp_6326)


def parse_teamsownerprojectspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4695 = None

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
            temp_4695 = str(data["key"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4695):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4695:
        dependencies.set_variable("_teams__owner__projects_post_key", temp_4695)


def parse_teamsusernamepipelines_configvariablespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9821 = None

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
            temp_9821 = str(data["uuid"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9821):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9821:
        dependencies.set_variable("_teams__username__pipelines_config_variables_post_uuid", temp_9821)


def parse_usersusernamepipelines_configvariablespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_303 = None

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
            temp_303 = str(data["uuid"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_303):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_303:
        dependencies.set_variable("_users__username__pipelines_config_variables_post_uuid", temp_303)

req_collection = requests.RequestCollection([])
# Endpoint: /addon, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon"
)
req_collection.add_request(request)

# Endpoint: /addon, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon"
)
req_collection.add_request(request)

# Endpoint: /addon/linkers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("linkers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon/linkers"
)
req_collection.add_request(request)

# Endpoint: /addon/linkers/{linker_key}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("linkers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon/linkers/{linker_key}"
)
req_collection.add_request(request)

# Endpoint: /addon/linkers/{linker_key}/values, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("linkers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("values"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon/linkers/{linker_key}/values"
)
req_collection.add_request(request)

# Endpoint: /addon/linkers/{linker_key}/values, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("linkers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("values"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon/linkers/{linker_key}/values"
)
req_collection.add_request(request)

# Endpoint: /addon/linkers/{linker_key}/values, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("linkers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("values"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon/linkers/{linker_key}/values"
)
req_collection.add_request(request)

# Endpoint: /addon/linkers/{linker_key}/values, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("linkers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("values"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon/linkers/{linker_key}/values"
)
req_collection.add_request(request)

# Endpoint: /addon/linkers/{linker_key}/values, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("linkers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("values"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon/linkers/{linker_key}/values"
)
req_collection.add_request(request)

# Endpoint: /addon/linkers/{linker_key}/values, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("linkers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("values"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/addon/linkers/{linker_key}/values"
)
req_collection.add_request(request)

# Endpoint: /hook_events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hook_events"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/hook_events"
)
req_collection.add_request(request)

# Endpoint: /hook_events/{subject_type}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hook_events"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['user','repository','team']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/hook_events/{subject_type}"
)
req_collection.add_request(request)

# Endpoint: /repositories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("after="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("role="),
    primitives.restler_fuzzable_group("role", ['admin','contributor','member','owner']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "avatar":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "clone":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "commits":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "downloads":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "forks":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "hooks":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "html":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "pullrequests":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "watchers":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "owner":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "parent":
        """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
    ,
    "project":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "owner":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
    "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("repo_slug"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "avatar":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "clone":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "commits":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "downloads":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "forks":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "hooks":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "html":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "pullrequests":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "watchers":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "owner":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "parent":
        """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
    ,
    "project":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "owner":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
    "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugput,
            'dependencies':
            [
                _repositories__username___repo_slug__put_name.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/branch-restrictions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch-restrictions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/branch-restrictions"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/branch-restrictions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch-restrictions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "groups":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "full_slug":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "members":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "owner":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "slug":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_group("kind", ['require_tasks_to_be_completed','require_passing_builds_to_merge','force','require_all_dependencies_merged','push','require_approvals_to_merge','enforce_merge_checks','restrict_merges','reset_pullrequest_approvals_on_change','delete']  ,quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "users":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "value":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugbranchrestrictionspost,
            'dependencies':
            [
                _repositories__username___repo_slug__branch_restrictions_post_id.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}/branch-restrictions"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/branch-restrictions/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch-restrictions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__branch_restrictions_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/branch-restrictions/{id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/branch-restrictions/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch-restrictions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__branch_restrictions_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/branch-restrictions/{id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/branch-restrictions/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch-restrictions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__branch_restrictions_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "groups":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "full_slug":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "members":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "owner":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "slug":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_group("kind", ['require_tasks_to_be_completed','require_passing_builds_to_merge','force','require_all_dependencies_merged','push','require_approvals_to_merge','enforce_merge_checks','restrict_merges','reset_pullrequest_approvals_on_change','delete']  ,quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "users":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "value":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/branch-restrictions/{id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{node}/approve, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("approve"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commit/{node}/approve"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{node}/approve, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("approve"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commit/{node}/approve"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{node}/statuses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commit/{node}/statuses"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{node}/statuses/build, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("build"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugcommitnodestatusesbuildpost,
            'dependencies':
            [
                _repositories__username___repo_slug__commit__node__statuses_build_post_key.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}/commit/{node}/statuses/build"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{node}/statuses/build/{key}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("build"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__commit__node__statuses_build_post_key.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commit/{node}/statuses/build/{key}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{node}/statuses/build/{key}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("build"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__commit__node__statuses_build_post_key.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "commit":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "refname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_group("state", ['SUCCESSFUL','FAILED','INPROGRESS','STOPPED']  ,quoted=True),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commit/{node}/statuses/build/{key}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{revision}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commit/{revision}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{sha}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commit/{sha}/comments"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commit/{sha}/comments/{comment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commit/{sha}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commits"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commits, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commits"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commits/{revision}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commits/{revision}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/commits/{revision}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/commits/{revision}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/components, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("components"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/components"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/components/{component_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("components"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/components/{component_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/default-reviewers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("default-reviewers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/default-reviewers"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/default-reviewers/{target_username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("default-reviewers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/default-reviewers/{target_username}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/default-reviewers/{target_username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("default-reviewers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/default-reviewers/{target_username}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/default-reviewers/{target_username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("default-reviewers"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("target_username"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/default-reviewers/{target_username}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/diff/{spec}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("diff"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("context="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/diff/{spec}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/downloads, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("downloads"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/downloads"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/downloads, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("downloads"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/downloads"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/downloads/{filename}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("downloads"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/downloads/{filename}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/downloads/{filename}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("downloads"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/downloads/{filename}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/forks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/forks"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/hooks"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/hooks"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/hooks/{uid}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/hooks/{uid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/hooks/{uid}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("uid"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "assignee":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "account_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "is_staff":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "component":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "links":
                {
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "content":
        {
            "html":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "markup":"""),
    primitives.restler_fuzzable_group("markup", ['markdown','creole']  ,quoted=True),
    primitives.restler_static_string(""",
            "raw":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "edited_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "kind":"""),
    primitives.restler_fuzzable_group("kind", ['bug','enhancement','proposal','task']  ,quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "attachments":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "comments":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "html":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "vote":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "watch":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "milestone":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "links":
                {
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "priority":"""),
    primitives.restler_fuzzable_group("priority", ['trivial','minor','major','critical','blocker']  ,quoted=True),
    primitives.restler_static_string(""",
    "reporter":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "account_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "is_staff":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "repository":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
            "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "clone":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "commits":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "downloads":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "forks":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "hooks":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "pullrequests":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "watchers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "owner":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "parent":
                """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
            ,
            "project":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "owner":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
            "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "state":"""),
    primitives.restler_fuzzable_group("state", ['new','open','resolved','on hold','invalid','duplicate','wontfix','closed']  ,quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "version":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "links":
                {
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "votes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugissuespost,
            'dependencies':
            [
                _repositories__username___repo_slug__issues_post_component_id.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}/issues"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/attachments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("attachments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/attachments"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/attachments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("attachments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/attachments"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/attachments/{path}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("attachments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/attachments/{path}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/attachments/{path}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("attachments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/attachments/{path}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/comments/{comment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/vote, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vote"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/vote"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/vote, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vote"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/vote"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/vote, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vote"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/vote"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/watch, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/watch"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/watch, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/watch"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/issues/{issue_id}/watch, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__issues_post_component_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/issues/{issue_id}/watch"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/milestones, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/milestones"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/milestones/{milestone_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/milestones/{milestone_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/patch/{spec}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("patch"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/patch/{spec}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "build_seconds_used":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "completed_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "creator":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "repository":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
            "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "clone":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "commits":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "downloads":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "forks":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "hooks":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "pullrequests":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "watchers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "owner":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "parent":
                """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
            ,
            "project":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "owner":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
            "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "state":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "target":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "trigger":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugpipelinespost,
            'dependencies':
            [
                _repositories__username___repo_slug__pipelines_post_creator_uuid.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}/pipelines"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_post_creator_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}/steps, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_post_creator_uuid.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("steps"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}/steps"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_post_creator_uuid.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("steps"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_post_creator_uuid.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("steps"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("log"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_post_creator_uuid.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stopPipeline"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "enabled":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "repository":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
            "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "clone":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "commits":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "downloads":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "forks":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "hooks":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "pullrequests":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "watchers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "owner":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "parent":
                """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
            ,
            "project":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "owner":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
            "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/ssh/key_pair, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ssh"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("key_pair"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/ssh/key_pair"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/ssh/key_pair, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ssh"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("key_pair"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/ssh/key_pair"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/ssh/key_pair, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ssh"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("key_pair"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "private_key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "public_key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/ssh/key_pair"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ssh"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("known_hosts"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ssh"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("known_hosts"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "hostname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "public_key":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "key_type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "md5_fingerprint":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "sha256_fingerprint":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugpipelines_configsshknown_hostspost,
            'dependencies':
            [
                _repositories__username___repo_slug__pipelines_config_ssh_known_hosts_post_uuid.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ssh"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("known_hosts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_config_ssh_known_hosts_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ssh"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("known_hosts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_config_ssh_known_hosts_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ssh"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("known_hosts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_config_ssh_known_hosts_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "hostname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "public_key":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "key_type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "md5_fingerprint":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "sha256_fingerprint":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/variables, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/variables"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/variables, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "secured":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugpipelines_configvariablespost,
            'dependencies':
            [
                _repositories__username___repo_slug__pipelines_config_variables_post_uuid.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/variables"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/variables/{variable_uuid}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/variables/{variable_uuid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pipelines_config/variables/{variable_uuid}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "secured":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['MERGED','SUPERSEDED','OPEN','DECLINED']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "author":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "close_source_branch":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "closed_by":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "comment_count":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "destination":
        {
            "branch":
                {
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "commit":
                {
                    "hash":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "repository":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
                    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "clone":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "commits":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "downloads":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "forks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "hooks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "pullrequests":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "watchers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "owner":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "parent":
                        """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
                    ,
                    "project":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "owner":
                                {
                                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "links":
                                        {
                                            "avatar":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "followers":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "following":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "html":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "repositories":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "self":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                        }
                                    ,
                                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
                    "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "links":
        {
            "activity":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "approve":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "comments":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "commits":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "decline":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "diff":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "html":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "merge":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "merge_commit":
        {
            "hash":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "participants":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "approved":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "role":"""),
    primitives.restler_fuzzable_group("role", ['PARTICIPANT','REVIEWER']  ,quoted=True),
    primitives.restler_static_string(""",
            "user":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "account_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "is_staff":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                }
        }
    ],
    "reason":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "reviewers":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "source":
        {
            "branch":
                {
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "commit":
                {
                    "hash":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "repository":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
                    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "clone":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "commits":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "downloads":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "forks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "hooks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "pullrequests":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "watchers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "owner":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "parent":
                        """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
                    ,
                    "project":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "owner":
                                {
                                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "links":
                                        {
                                            "avatar":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "followers":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "following":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "html":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "repositories":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "self":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                        }
                                    ,
                                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
                    "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "state":"""),
    primitives.restler_fuzzable_group("state", ['MERGED','SUPERSEDED','OPEN','DECLINED']  ,quoted=True),
    primitives.restler_static_string(""",
    "task_count":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugpullrequestspost,
            'dependencies':
            [
                _repositories__username___repo_slug__pullrequests_post_id.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}/pullrequests"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/activity, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("activity"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/activity"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "author":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "close_source_branch":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "closed_by":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "comment_count":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "destination":
        {
            "branch":
                {
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "commit":
                {
                    "hash":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "repository":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
                    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "clone":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "commits":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "downloads":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "forks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "hooks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "pullrequests":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "watchers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "owner":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "parent":
                        """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
                    ,
                    "project":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "owner":
                                {
                                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "links":
                                        {
                                            "avatar":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "followers":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "following":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "html":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "repositories":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "self":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                        }
                                    ,
                                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
                    "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "links":
        {
            "activity":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "approve":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "comments":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "commits":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "decline":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "diff":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "html":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "merge":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "merge_commit":
        {
            "hash":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "participants":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "approved":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "role":"""),
    primitives.restler_fuzzable_group("role", ['PARTICIPANT','REVIEWER']  ,quoted=True),
    primitives.restler_static_string(""",
            "user":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "account_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "is_staff":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                }
        }
    ],
    "reason":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "reviewers":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "source":
        {
            "branch":
                {
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "commit":
                {
                    "hash":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "repository":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
                    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "clone":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "commits":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "downloads":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "forks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "hooks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "pullrequests":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "watchers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "owner":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "parent":
                        """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
                    ,
                    "project":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "owner":
                                {
                                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "links":
                                        {
                                            "avatar":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "followers":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "following":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "html":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "repositories":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "self":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                        }
                                    ,
                                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
                    "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "state":"""),
    primitives.restler_fuzzable_group("state", ['MERGED','SUPERSEDED','OPEN','DECLINED']  ,quoted=True),
    primitives.restler_static_string(""",
    "task_count":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/activity, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("activity"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/activity"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/approve, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("approve"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/approve"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/approve, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("approve"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/approve"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/commits"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/decline, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("decline"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/decline"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/diff, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("diff"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/diff"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/merge, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "close_source_branch":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "merge_strategy":"""),
    primitives.restler_fuzzable_group("merge_strategy", ['merge_commit','squash'] , default_enum="merge_commit" ,quoted=True),
    primitives.restler_static_string(""",
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/merge"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/patch, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("patch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/patch"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/statuses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pullrequests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__pullrequests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/pullrequests/{pull_request_id}/statuses"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/refs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/refs"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/refs/branches, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/refs/branches"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/refs/branches/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/refs/branches/{name}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/refs/tags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/refs/tags"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/refs/tags, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "date":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "commits":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "html":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "self":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "tagger":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "raw":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "user":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "followers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "following":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "repositories":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "target":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "author":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "raw":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "user":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "date":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "hash":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "parents":
            [
                """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
            ],
            "links":
                {
                    "approve":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "comments":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "diff":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "patch":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "statuses":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "participants":
            [
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "approved":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "role":"""),
    primitives.restler_fuzzable_group("role", ['PARTICIPANT','REVIEWER']  ,quoted=True),
    primitives.restler_static_string(""",
                    "user":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "account_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "is_staff":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                        }
                }
            ],
            "repository":
                {
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "fork_policy":"""),
    primitives.restler_fuzzable_group("fork_policy", ['allow_forks','no_public_forks','no_forks']  ,quoted=True),
    primitives.restler_static_string(""",
                    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "links":
                        {
                            "avatar":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "clone":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "commits":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "downloads":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "forks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "hooks":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "html":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "pullrequests":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "self":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "watchers":
                                {
                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "owner":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "followers":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "following":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "repositories":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "self":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "parent":
                        """),
    primitives.restler_fuzzable_object("{ }"),
    primitives.restler_static_string("""
                    ,
                    "project":
                        {
                            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "links":
                                {
                                    "avatar":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "html":
                                        {
                                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                        }
                                }
                            ,
                            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "owner":
                                {
                                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                                    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "links":
                                        {
                                            "avatar":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "followers":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "following":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "html":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "repositories":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                            ,
                                            "self":
                                                {
                                                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                                }
                                        }
                                    ,
                                    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
                    "size":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
                    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_repositoriesusernamerepo_slugrefstagspost,
            'dependencies':
            [
                _repositories__username___repo_slug__refs_tags_post_name.writer()
            ]
        }

    },

],
requestId="/repositories/{username}/{repo_slug}/refs/tags"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/refs/tags/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__refs_tags_post_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/refs/tags/{name}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/src/{node}/{path}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("src"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_group("format", ['meta']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/src/{node}/{path}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/versions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("versions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/versions"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/versions/{version_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("versions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/versions/{version_id}"
)
req_collection.add_request(request)

# Endpoint: /repositories/{username}/{repo_slug}/watchers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repositories__username___repo_slug__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{username}/{repo_slug}/watchers"
)
req_collection.add_request(request)

# Endpoint: /snippets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("role="),
    primitives.restler_fuzzable_group("role", ['owner','contributor','member']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets"
)
req_collection.add_request(request)

# Endpoint: /snippets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "creator":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "owner":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_snippetspost,
            'dependencies':
            [
                _snippets_post_creator_username.writer()
            ]
        }

    },

],
requestId="/snippets"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("role="),
    primitives.restler_fuzzable_group("role", ['owner','contributor','member']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "creator":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "owner":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("encoded_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_snippetsusernameencoded_idput,
            'dependencies':
            [
                _snippets__username___encoded_id__put_id.writer()
            ]
        }

    },

],
requestId="/snippets/{username}/{encoded_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "creator":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "owner":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "scm":"""),
    primitives.restler_fuzzable_group("scm", ['hg','git']  ,quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_snippetsusernameencoded_idcommentspost,
            'dependencies':
            [
                _snippets__username___encoded_id__comments_post_id.writer()
            ]
        }

    },

],
requestId="/snippets/{username}/{encoded_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/comments/{comment_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/comments/{comment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/comments/{comment_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/comments/{comment_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/commits"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/commits/{revision}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/commits/{revision}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/watch, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/watch"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/watch, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/watch"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/watch, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/watch"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/watchers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("watchers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/watchers"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/{node_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id___node_id__put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/{node_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/{node_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id___node_id__put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/{node_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/{node_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("node_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_snippetsusernameencoded_idnode_idput,
            'dependencies':
            [
                _snippets__username___encoded_id___node_id__put_id.writer()
            ]
        }

    },

],
requestId="/snippets/{username}/{encoded_id}/{node_id}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/{node_id}/files/{path}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id___node_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/{node_id}/files/{path}"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/{revision}/diff, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("diff"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/{revision}/diff"
)
req_collection.add_request(request)

# Endpoint: /snippets/{username}/{encoded_id}/{revision}/patch, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets_post_creator_username.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_snippets__username___encoded_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("patch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/snippets/{username}/{encoded_id}/{revision}/patch"
)
req_collection.add_request(request)

# Endpoint: /teams, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("role="),
    primitives.restler_fuzzable_group("role", ['admin','contributor','member']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams"
)
req_collection.add_request(request)

# Endpoint: /teams/{owner}/projects, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{owner}/projects"
)
req_collection.add_request(request)

# Endpoint: /teams/{owner}/projects, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "avatar":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "html":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "owner":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_teamsownerprojectspost,
            'dependencies':
            [
                _teams__owner__projects_post_key.writer()
            ]
        }

    },

],
requestId="/teams/{owner}/projects"
)
req_collection.add_request(request)

# Endpoint: /teams/{owner}/projects/{project_key}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__owner__projects_post_key.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{owner}/projects/{project_key}"
)
req_collection.add_request(request)

# Endpoint: /teams/{owner}/projects/{project_key}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__owner__projects_post_key.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{owner}/projects/{project_key}"
)
req_collection.add_request(request)

# Endpoint: /teams/{owner}/projects/{project_key}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__owner__projects_post_key.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "is_private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "links":
        {
            "avatar":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "html":
                {
                    "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
        }
    ,
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "owner":
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "created_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "links":
                {
                    "avatar":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "followers":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "following":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "html":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "repositories":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ,
                    "self":
                        {
                            "href":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "updated_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{owner}/projects/{project_key}"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/followers"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/following, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/following"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/hooks"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/hooks"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/hooks/{uid}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/hooks/{uid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/hooks/{uid}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("uid"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/members"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/pipelines_config/variables, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/pipelines_config/variables"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/pipelines_config/variables, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "secured":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_teamsusernamepipelines_configvariablespost,
            'dependencies':
            [
                _teams__username__pipelines_config_variables_post_uuid.writer()
            ]
        }

    },

],
requestId="/teams/{username}/pipelines_config/variables"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/pipelines_config/variables/{variable_uuid}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__username__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/pipelines_config/variables/{variable_uuid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__username__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/pipelines_config/variables/{variable_uuid}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__username__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "secured":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /teams/{username}/repositories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{username}/repositories"
)
req_collection.add_request(request)

# Endpoint: /user, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user"
)
req_collection.add_request(request)

# Endpoint: /user/emails, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/emails"
)
req_collection.add_request(request)

# Endpoint: /user/emails/{email}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/emails/{email}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/followers"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/following, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/following"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/hooks"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/hooks"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/hooks/{uid}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/hooks/{uid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/hooks/{uid}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("uid"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/hooks/{uid}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/pipelines_config/variables, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/pipelines_config/variables"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/pipelines_config/variables, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "secured":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_usersusernamepipelines_configvariablespost,
            'dependencies':
            [
                _users__username__pipelines_config_variables_post_uuid.writer()
            ]
        }

    },

],
requestId="/users/{username}/pipelines_config/variables"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/pipelines_config/variables/{variable_uuid}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users__username__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/pipelines_config/variables/{variable_uuid}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users__username__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/pipelines_config/variables/{variable_uuid}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines_config"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users__username__pipelines_config_variables_post_uuid.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "secured":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "uuid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/pipelines_config/variables/{variable_uuid}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/repositories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/2.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.bitbucket.org\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/repositories"
)
req_collection.add_request(request)
