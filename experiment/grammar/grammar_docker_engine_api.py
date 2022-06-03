""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_volumes_create_post_Driver = dependencies.DynamicVariable("_volumes_create_post_Driver")

_volumes_create_post_Labels = dependencies.DynamicVariable("_volumes_create_post_Labels")

_volumes_create_post_Name = dependencies.DynamicVariable("_volumes_create_post_Name")

_volumes_create_post_Options = dependencies.DynamicVariable("_volumes_create_post_Options")

def parse_volumescreatepost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None
    temp_8173 = None
    temp_7680 = None
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
            temp_7262 = str(data["Driver"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8173 = str(data["Labels"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7680 = str(data["Name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5581 = str(data["Options"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262 or temp_8173 or temp_7680 or temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_volumes_create_post_Driver", temp_7262)
    if temp_8173:
        dependencies.set_variable("_volumes_create_post_Labels", temp_8173)
    if temp_7680:
        dependencies.set_variable("_volumes_create_post_Name", temp_7680)
    if temp_5581:
        dependencies.set_variable("_volumes_create_post_Options", temp_5581)

req_collection = requests.RequestCollection([])
# Endpoint: /_ping, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_ping"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_ping"
)
req_collection.add_request(request)

# Endpoint: /auth, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["xxxx"]),
    primitives.restler_static_string(""",
    "serveraddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["https://index.docker.io/v1/"]),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["hannibal"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/auth"
)
req_collection.add_request(request)

# Endpoint: /build, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("build"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("dockerfile="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("t="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("extrahosts="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("remote="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("nocache="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cachefrom="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pull="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rm="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("forcerm="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("memory="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("memswap="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cpushares="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cpusetcpus="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cpuperiod="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cpuquota="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("buildargs="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("shmsize="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("squash="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("networkmode="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-type: "),
    primitives.restler_fuzzable_group("Content-type", ['application/x-tar'] , default_enum="application/x-tar" ,quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("X-Registry-Config: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/build"
)
req_collection.add_request(request)

# Endpoint: /build/prune, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("build"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prune"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/build/prune"
)
req_collection.add_request(request)

# Endpoint: /commit, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commit"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("container="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("repo="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tag="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("comment="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("author="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pause="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("changes="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "ArgsEscaped":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "AttachStderr":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "AttachStdin":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "AttachStdout":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "Cmd":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    ,
    "Domainname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Entrypoint":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    ,
    "Env":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "ExposedPorts":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "Healthcheck":
        {
            "Interval":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "Retries":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "StartPeriod":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "Test":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "Timeout":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "Hostname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Image":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "MacAddress":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "NetworkDisabled":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "OnBuild":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "OpenStdin":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "Shell":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "StdinOnce":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "StopSignal":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "StopTimeout":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "Tty":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "User":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Volumes":
        {
            "additionalProperties":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
        }
    ,
    "WorkingDir":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/commit"
)
req_collection.add_request(request)

# Endpoint: /configs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("configs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/configs"
)
req_collection.add_request(request)

# Endpoint: /configs/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("configs"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Data":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Labels":"""),
    primitives.restler_static_string(_volumes_create_post_Labels.reader(), quoted=False),
    primitives.restler_static_string(""",
    "Name":"""),
    primitives.restler_static_string(_volumes_create_post_Name.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/configs/create"
)
req_collection.add_request(request)

# Endpoint: /configs/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("configs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/configs/{id}"
)
req_collection.add_request(request)

# Endpoint: /configs/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("configs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/configs/{id}"
)
req_collection.add_request(request)

# Endpoint: /configs/{id}/update, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("configs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Data":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/configs/{id}/update"
)
req_collection.add_request(request)

# Endpoint: /containers/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "AttachStderr":"true",
    "AttachStdin":"false",
    "AttachStdout":"true",
    "Cmd":
        ["date"]
    ,
    "Domainname":"",
    "Entrypoint":
        ""
    ,
    "Env":
    [
        "FOO=bar",
        "BAZ=quux"
    ],
    "ExposedPorts":{"22/tcp":{}},
    "Hostname":"",
    "Image":"ubuntu",
    "Labels":"""),
    primitives.restler_static_string(_volumes_create_post_Labels.reader(), quoted=False),
    primitives.restler_static_string(""",
    "MacAddress":"12:34:56:78:9a:bc",
    "NetworkDisabled":"false",
    "OpenStdin":"false",
    "StdinOnce":"false",
    "StopSignal":"SIGTERM",
    "StopTimeout":"10",
    "Tty":"false",
    "User":"",
    "Volumes":
        {
        }
    ,
    "WorkingDir":"",
    "HostConfig":
        {
            "BlkioDeviceReadBps":
            [
                {
                }
            ],
            "BlkioDeviceReadIOps":
            [
                {
                }
            ],
            "BlkioDeviceWriteBps":
            [
                {
                }
            ],
            "BlkioDeviceWriteIOps":
            [
                {
                }
            ],
            "BlkioWeight":"300",
            "BlkioWeightDevice":
            [
                {
                }
            ],
            "CgroupParent":"",
            "CpuPercent":"80",
            "CpuPeriod":"100000",
            "CpuQuota":"50000",
            "CpuRealtimePeriod":"1000000",
            "CpuRealtimeRuntime":"10000",
            "CpuShares":"512",
            "CpusetCpus":"0,1",
            "CpusetMems":"0,1",
            "Devices":
            [
            ],
            "KernelMemory":"0",
            "Memory":"0",
            "MemoryReservation":"0",
            "MemorySwap":"0",
            "MemorySwappiness":"60",
            "NanoCPUs":"500000",
            "OomKillDisable":"false",
            "PidsLimit":"-1",
            "Ulimits":
            [
                {
                }
            ],
            "AutoRemove":"true",
            "Binds":
            [
                "/tmp:/tmp"
            ],
            "CapAdd":
            [
                "NET_ADMIN"
            ],
            "CapDrop":
            [
                "MKNOD"
            ],
            "Dns":
            [
                "8.8.8.8"
            ],
            "DnsOptions":
            [
                ""
            ],
            "DnsSearch":
            [
                ""
            ],
            "GroupAdd":
            [
                "newgroup"
            ],
            "Links":
            [
                "redis3:redis"
            ],
            "LogConfig":
                {
                    "Config":{},
                    "Type":"json-file"
                }
            ,
            "NetworkMode":"bridge",
            "OomScoreAdj":"500",
            "PidMode":"",
            "PortBindings":{"22/tcp":[{"HostPort":"11022"}]},
            "Privileged":"false",
            "PublishAllPorts":"false",
            "ReadonlyRootfs":"false",
            "RestartPolicy":
                {
                    "MaximumRetryCount":"0",
                    "Name":""
                }
            ,
            "SecurityOpt":
            [
            ],
            "ShmSize":"67108864",
            "StorageOpt":{},
            "VolumeDriver":"",
            "VolumesFrom":
            [
                "parent",
                "other:ro"
            ]
        }
    ,
    "NetworkingConfig":
        {
            "EndpointsConfig":{"isolated_nw":{"Aliases":["server_x","server_y"],"IPAMConfig":{"IPv4Address":"172.20.30.33","IPv6Address":"2001:db8:abcd::3033","LinkLocalIPs":["169.254.34.68","fe80::3468"]},"Links":["container_1","container_2"]}}
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/create"
)
req_collection.add_request(request)

# Endpoint: /containers/json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("json"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("all="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("size="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/json"
)
req_collection.add_request(request)

# Endpoint: /containers/prune, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prune"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/prune"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("v="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("force="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("link="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/archive, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("archive"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/archive"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/archive, method: Head
request = requests.Request([
    primitives.restler_static_string("HEAD "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("archive"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/archive"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/archive, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("archive"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("noOverwriteDirNonDir="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/archive"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/attach, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("attach"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("detachKeys="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("logs="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stream="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stdin="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stdout="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stderr="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/attach"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/attach/ws, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("attach"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ws"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("detachKeys="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("logs="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stream="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stdin="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stdout="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stderr="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/attach/ws"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/changes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("changes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/changes"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/exec, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("exec"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "AttachStderr":"""),
    primitives.restler_fuzzable_bool("true", examples=['"true"']),
    primitives.restler_static_string(""",
    "AttachStdin":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string(""",
    "AttachStdout":"""),
    primitives.restler_fuzzable_bool("true", examples=['"true"']),
    primitives.restler_static_string(""",
    "Cmd":
    [
        "date"
    ],
    "DetachKeys":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["ctrl-p,ctrl-q"]),
    primitives.restler_static_string(""",
    "Env":
    [
        "FOO=bar",
        "BAZ=quux"
    ],
    "Tty":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/exec"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/export, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("export"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/export"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("json"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("size="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/json"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/kill, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("kill"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("signal="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/kill"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("follow="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stdout="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stderr="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timestamps="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tail="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/logs"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/pause, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pause"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/pause"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/rename, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rename"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/rename"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/resize, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resize"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("h="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("w="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/resize"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/restart, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("restart"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("t="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/restart"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/start, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("start"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("detachKeys="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/start"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/stats, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stats"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("stream="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/stats"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/stop, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stop"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("t="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/stop"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/top, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("top"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ps_args="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/top"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/unpause, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unpause"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/unpause"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/update, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "BlkioWeight":"300",
    "CpuPeriod":"100000",
    "CpuQuota":"50000",
    "CpuRealtimePeriod":"1000000",
    "CpuRealtimeRuntime":"10000",
    "CpuShares":"512",
    "CpusetCpus":"0,1",
    "CpusetMems":"0",
    "KernelMemory":"52428800",
    "Memory":"314572800",
    "MemoryReservation":"209715200",
    "MemorySwap":"514288000",
    "RestartPolicy":
        {
            "MaximumRetryCount":"4",
            "Name":"on-failure"
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/update"
)
req_collection.add_request(request)

# Endpoint: /containers/{id}/wait, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("containers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("wait"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("condition="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/containers/{id}/wait"
)
req_collection.add_request(request)

# Endpoint: /distribution/{name}/json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("distribution"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("json"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/distribution/{name}/json"
)
req_collection.add_request(request)

# Endpoint: /events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("until="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/events"
)
req_collection.add_request(request)

# Endpoint: /exec/{id}/json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("exec"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("json"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/exec/{id}/json"
)
req_collection.add_request(request)

# Endpoint: /exec/{id}/resize, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("exec"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resize"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("h="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("w="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/exec/{id}/resize"
)
req_collection.add_request(request)

# Endpoint: /exec/{id}/start, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("exec"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("start"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Detach":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string(""",
    "Tty":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/exec/{id}/start"
)
req_collection.add_request(request)

# Endpoint: /images/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("fromImage="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fromSrc="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("repo="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tag="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("X-Registry-Auth: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/create"
)
req_collection.add_request(request)

# Endpoint: /images/get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("names="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/get"
)
req_collection.add_request(request)

# Endpoint: /images/json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("json"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("all="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("digests="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/json"
)
req_collection.add_request(request)

# Endpoint: /images/load, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("load"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("quiet="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/load"
)
req_collection.add_request(request)

# Endpoint: /images/prune, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prune"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/prune"
)
req_collection.add_request(request)

# Endpoint: /images/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("term="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/search"
)
req_collection.add_request(request)

# Endpoint: /images/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("force="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("noprune="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{name}"
)
req_collection.add_request(request)

# Endpoint: /images/{name}/get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("get"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{name}/get"
)
req_collection.add_request(request)

# Endpoint: /images/{name}/history, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("history"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{name}/history"
)
req_collection.add_request(request)

# Endpoint: /images/{name}/json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("json"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{name}/json"
)
req_collection.add_request(request)

# Endpoint: /images/{name}/push, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("tag="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("X-Registry-Auth: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{name}/push"
)
req_collection.add_request(request)

# Endpoint: /images/{name}/tag, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("images"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tag"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("repo="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tag="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/images/{name}/tag"
)
req_collection.add_request(request)

# Endpoint: /info, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("info"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/info"
)
req_collection.add_request(request)

# Endpoint: /networks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("networks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/networks"
)
req_collection.add_request(request)

# Endpoint: /networks/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("networks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Attachable":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string(""",
    "CheckDuplicate":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string(""",
    "Driver":"""),
    primitives.restler_static_string(_volumes_create_post_Driver.reader(), quoted=True),
    primitives.restler_static_string(""",
    "EnableIPv6":"""),
    primitives.restler_fuzzable_bool("true", examples=['"true"']),
    primitives.restler_static_string(""",
    "IPAM":
        {
            "Config":
            [
                {"Gateway":"172.20.10.11","IPRange":"172.20.10.0/24","Subnet":"172.20.0.0/16"},
                {"Gateway":"2001:db8:abcd::1011","Subnet":"2001:db8:abcd::/64"}
            ],
            "Driver":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["default"]),
    primitives.restler_static_string(""",
            "Options":
            [
                "foo":"bar"
            ]
        }
    ,
    "Ingress":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string(""",
    "Internal":"""),
    primitives.restler_fuzzable_bool("true", examples=['"true"']),
    primitives.restler_static_string(""",
    "Labels":"""),
    primitives.restler_static_string(_volumes_create_post_Labels.reader(), quoted=False),
    primitives.restler_static_string(""",
    "Name":"""),
    primitives.restler_static_string(_volumes_create_post_Name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "Options":"""),
    primitives.restler_static_string(_volumes_create_post_Options.reader(), quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/networks/create"
)
req_collection.add_request(request)

# Endpoint: /networks/prune, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("networks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prune"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/networks/prune"
)
req_collection.add_request(request)

# Endpoint: /networks/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("networks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/networks/{id}"
)
req_collection.add_request(request)

# Endpoint: /networks/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("networks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("verbose="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("scope="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/networks/{id}"
)
req_collection.add_request(request)

# Endpoint: /networks/{id}/connect, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("networks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("connect"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/networks/{id}/connect"
)
req_collection.add_request(request)

# Endpoint: /networks/{id}/disconnect, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("networks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("disconnect"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Container":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Force":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/networks/{id}/disconnect"
)
req_collection.add_request(request)

# Endpoint: /nodes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("nodes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/nodes"
)
req_collection.add_request(request)

# Endpoint: /nodes/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("nodes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("force="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/nodes/{id}"
)
req_collection.add_request(request)

# Endpoint: /nodes/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("nodes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/nodes/{id}"
)
req_collection.add_request(request)

# Endpoint: /nodes/{id}/update, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("nodes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Availability":"""),
    primitives.restler_fuzzable_group("Availability", ['active','pause','drain']  ,quoted=True, examples=["active"]),
    primitives.restler_static_string(""",
    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"foo\":\"bar\"}"]),
    primitives.restler_static_string(""",
    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node-name"]),
    primitives.restler_static_string(""",
    "Role":"""),
    primitives.restler_fuzzable_group("Role", ['worker','manager']  ,quoted=True, examples=["manager"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/nodes/{id}/update"
)
req_collection.add_request(request)

# Endpoint: /plugins, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins"
)
req_collection.add_request(request)

# Endpoint: /plugins/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/create"
)
req_collection.add_request(request)

# Endpoint: /plugins/privileges, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("privileges"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("remote="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/privileges"
)
req_collection.add_request(request)

# Endpoint: /plugins/pull, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pull"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("remote="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("X-Registry-Auth: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/pull"
)
req_collection.add_request(request)

# Endpoint: /plugins/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("force="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/{name}"
)
req_collection.add_request(request)

# Endpoint: /plugins/{name}/disable, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("disable"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/{name}/disable"
)
req_collection.add_request(request)

# Endpoint: /plugins/{name}/enable, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enable"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("timeout="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/{name}/enable"
)
req_collection.add_request(request)

# Endpoint: /plugins/{name}/json, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("json"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/{name}/json"
)
req_collection.add_request(request)

# Endpoint: /plugins/{name}/push, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/{name}/push"
)
req_collection.add_request(request)

# Endpoint: /plugins/{name}/set, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("set"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("["),
    primitives.restler_static_string("""
    "DEBUG=1"]"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/{name}/set"
)
req_collection.add_request(request)

# Endpoint: /plugins/{name}/upgrade, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plugins"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("upgrade"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("remote="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("X-Registry-Auth: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/plugins/{name}/upgrade"
)
req_collection.add_request(request)

# Endpoint: /secrets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("secrets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/secrets"
)
req_collection.add_request(request)

# Endpoint: /secrets/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("secrets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Data":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=[""]),
    primitives.restler_static_string(""",
    "Driver":"""),
    primitives.restler_static_string(_volumes_create_post_Driver.reader(), quoted=False),
    primitives.restler_static_string(""",
    "Labels":"""),
    primitives.restler_static_string(_volumes_create_post_Labels.reader(), quoted=False),
    primitives.restler_static_string(""",
    "Name":"""),
    primitives.restler_static_string(_volumes_create_post_Name.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/secrets/create"
)
req_collection.add_request(request)

# Endpoint: /secrets/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("secrets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/secrets/{id}"
)
req_collection.add_request(request)

# Endpoint: /secrets/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("secrets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/secrets/{id}"
)
req_collection.add_request(request)

# Endpoint: /secrets/{id}/update, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("secrets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Data":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=[""]),
    primitives.restler_static_string(""",
    "Driver":
        {
            "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["some-driver"]),
    primitives.restler_static_string(""",
            "Options":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["""{
  "OptionA": "value for driver-specific option A",
  "OptionB": "value for driver-specific option B"
}"""]),
    primitives.restler_static_string("""
        }
    ,
    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["""{
  "com.example.some-label": "some-value",
  "com.example.some-other-label": "some-other-value"
}"""]),
    primitives.restler_static_string(""",
    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/secrets/{id}/update"
)
req_collection.add_request(request)

# Endpoint: /services, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/services"
)
req_collection.add_request(request)

# Endpoint: /services/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("X-Registry-Auth: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "EndpointSpec":
        {
            "Mode":"""),
    primitives.restler_fuzzable_group("Mode", ['vip','dnsrr'] , default_enum="vip" ,quoted=True),
    primitives.restler_static_string(""",
            "Ports":
            [
                {
                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Protocol":"""),
    primitives.restler_fuzzable_group("Protocol", ['tcp','udp']  ,quoted=True),
    primitives.restler_static_string(""",
                    "PublishedPort":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "TargetPort":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
            ]
        }
    ,
    "Labels":"""),
    primitives.restler_static_string(_volumes_create_post_Labels.reader(), quoted=False),
    primitives.restler_static_string(""",
    "Mode":
        {
            "Global":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "Replicated":
                {
                    "Replicas":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
        }
    ,
    "Name":"""),
    primitives.restler_static_string(_volumes_create_post_Name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "Networks":
    [
        {
            "Aliases":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "Target":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "RollbackConfig":
        {
            "Delay":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "FailureAction":"""),
    primitives.restler_fuzzable_group("FailureAction", ['continue','pause']  ,quoted=True),
    primitives.restler_static_string(""",
            "MaxFailureRatio":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "Monitor":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "Order":"""),
    primitives.restler_fuzzable_group("Order", ['stop-first','start-first']  ,quoted=True),
    primitives.restler_static_string(""",
            "Parallelism":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "TaskTemplate":
        {
            "ContainerSpec":
                {
                    "Args":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Command":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Configs":
                    [
                        {
                            "ConfigID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "ConfigName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "File":
                                {
                                    "GID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Mode":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "UID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ],
                    "DNSConfig":
                        {
                            "Nameservers":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ],
                            "Options":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ],
                            "Search":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ]
                        }
                    ,
                    "Dir":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Env":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Groups":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "HealthCheck":
                        {
                            "Interval":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "Retries":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "StartPeriod":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "Test":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ],
                            "Timeout":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                        }
                    ,
                    "Hostname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Hosts":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Image":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
                    "Mounts":
                    [
                        {
                            "BindOptions":
                                {
                                    "Propagation":
                                        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                                }
                            ,
                            "Consistency":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "ReadOnly":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                            "Source":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "Target":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "TmpfsOptions":
                                {
                                    "Mode":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                                    "SizeBytes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                                }
                            ,
                            "Type":"""),
    primitives.restler_fuzzable_group("Type", ['bind','volume','tmpfs']  ,quoted=True),
    primitives.restler_static_string(""",
                            "VolumeOptions":
                                {
                                    "DriverConfig":
                                        {
                                            "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                            "Options":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
                                    "NoCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                                }
                        }
                    ],
                    "OpenStdin":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "Privileges":
                        {
                            "CredentialSpec":
                                {
                                    "File":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Registry":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "SELinuxContext":
                                {
                                    "Disable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                                    "Level":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "User":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "ReadOnly":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "Secrets":
                    [
                        {
                            "File":
                                {
                                    "GID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Mode":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "UID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "SecretID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "SecretName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ],
                    "StopGracePeriod":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "StopSignal":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "TTY":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "User":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "ForceUpdate":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "LogDriver":
                {
                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Options":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                }
            ,
            "Networks":
            [
                {
                    "Aliases":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Target":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "Placement":
                {
                    "Constraints":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.hostname!=node3.corp.example.com"]),
    primitives.restler_static_string(""",
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.role!=manager"]),
    primitives.restler_static_string(""",
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.labels.type==production"]),
    primitives.restler_static_string("""
                    ],
                    "Platforms":
                    [
                        {
                            "Architecture":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["x86_64"]),
    primitives.restler_static_string(""",
                            "OS":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["linux"]),
    primitives.restler_static_string("""
                        }
                    ],
                    "Preferences":
                    [
                        {
                            "Spread":
                                {
                                    "SpreadDescriptor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.labels.datacenter"]),
    primitives.restler_static_string("""
                                }
                        },
                        {
                            "Spread":
                                {
                                    "SpreadDescriptor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.labels.rack"]),
    primitives.restler_static_string("""
                                }
                        }
                    ]
                }
            ,
            "PluginSpec":
                {
                    "Disabled":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "PluginPrivilege":
                    [
                        {
                            "Description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "Value":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ]
                        }
                    ],
                    "Remote":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "Resources":
                {
                    "Limits":
                        {
                            "GenericResources":
                                [
                                    {
                                        "DiscreteResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["SSD"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_int("1", examples=['"3"']),
    primitives.restler_static_string("""
                                            }
                                    },
                                    {
                                        "NamedResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GPU"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["UUID1"]),
    primitives.restler_static_string("""
                                            }
                                    },
                                    {
                                        "NamedResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GPU"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["UUID2"]),
    primitives.restler_static_string("""
                                            }
                                    }
                                ]
                            ,
                            "MemoryBytes":"""),
    primitives.restler_fuzzable_int("1", examples=["8272408576"]),
    primitives.restler_static_string(""",
                            "NanoCPUs":"""),
    primitives.restler_fuzzable_int("1", examples=["4000000000"]),
    primitives.restler_static_string("""
                        }
                    ,
                    "Reservation":
                        {
                            "GenericResources":
                                [
                                    {
                                        "DiscreteResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["SSD"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_int("1", examples=['"3"']),
    primitives.restler_static_string("""
                                            }
                                    },
                                    {
                                        "NamedResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GPU"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["UUID1"]),
    primitives.restler_static_string("""
                                            }
                                    },
                                    {
                                        "NamedResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GPU"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["UUID2"]),
    primitives.restler_static_string("""
                                            }
                                    }
                                ]
                            ,
                            "MemoryBytes":"""),
    primitives.restler_fuzzable_int("1", examples=["8272408576"]),
    primitives.restler_static_string(""",
                            "NanoCPUs":"""),
    primitives.restler_fuzzable_int("1", examples=["4000000000"]),
    primitives.restler_static_string("""
                        }
                }
            ,
            "RestartPolicy":
                {
                    "Condition":"""),
    primitives.restler_fuzzable_group("Condition", ['none','on-failure','any']  ,quoted=True),
    primitives.restler_static_string(""",
                    "Delay":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "MaxAttempts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "Window":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
            ,
            "Runtime":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "UpdateConfig":
        {
            "Delay":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "FailureAction":"""),
    primitives.restler_fuzzable_group("FailureAction", ['continue','pause','rollback']  ,quoted=True),
    primitives.restler_static_string(""",
            "MaxFailureRatio":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "Monitor":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "Order":"""),
    primitives.restler_fuzzable_group("Order", ['stop-first','start-first']  ,quoted=True),
    primitives.restler_static_string(""",
            "Parallelism":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/services/create"
)
req_collection.add_request(request)

# Endpoint: /services/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/services/{id}"
)
req_collection.add_request(request)

# Endpoint: /services/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("insertDefaults="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/services/{id}"
)
req_collection.add_request(request)

# Endpoint: /services/{id}/logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("details="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("follow="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stdout="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stderr="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timestamps="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tail="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/services/{id}/logs"
)
req_collection.add_request(request)

# Endpoint: /services/{id}/update, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("registryAuthFrom="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rollback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("X-Registry-Auth: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "EndpointSpec":
        {
            "Mode":"""),
    primitives.restler_fuzzable_group("Mode", ['vip','dnsrr'] , default_enum="vip" ,quoted=True),
    primitives.restler_static_string(""",
            "Ports":
            [
                {
                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Protocol":"""),
    primitives.restler_fuzzable_group("Protocol", ['tcp','udp']  ,quoted=True),
    primitives.restler_static_string(""",
                    "PublishedPort":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "TargetPort":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
            ]
        }
    ,
    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "Mode":
        {
            "Global":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
            "Replicated":
                {
                    "Replicas":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
        }
    ,
    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Networks":
    [
        {
            "Aliases":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "Target":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "RollbackConfig":
        {
            "Delay":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "FailureAction":"""),
    primitives.restler_fuzzable_group("FailureAction", ['continue','pause']  ,quoted=True),
    primitives.restler_static_string(""",
            "MaxFailureRatio":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "Monitor":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "Order":"""),
    primitives.restler_fuzzable_group("Order", ['stop-first','start-first']  ,quoted=True),
    primitives.restler_static_string(""",
            "Parallelism":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "TaskTemplate":
        {
            "ContainerSpec":
                {
                    "Args":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Command":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Configs":
                    [
                        {
                            "ConfigID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "ConfigName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "File":
                                {
                                    "GID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Mode":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "UID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ],
                    "DNSConfig":
                        {
                            "Nameservers":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ],
                            "Options":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ],
                            "Search":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ]
                        }
                    ,
                    "Dir":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Env":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Groups":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "HealthCheck":
                        {
                            "Interval":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "Retries":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "StartPeriod":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                            "Test":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ],
                            "Timeout":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                        }
                    ,
                    "Hostname":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Hosts":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Image":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
                    "Mounts":
                    [
                        {
                            "BindOptions":
                                {
                                    "Propagation":
                                        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                                }
                            ,
                            "Consistency":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "ReadOnly":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                            "Source":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "Target":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "TmpfsOptions":
                                {
                                    "Mode":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                                    "SizeBytes":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                                }
                            ,
                            "Type":"""),
    primitives.restler_fuzzable_group("Type", ['bind','volume','tmpfs']  ,quoted=True),
    primitives.restler_static_string(""",
                            "VolumeOptions":
                                {
                                    "DriverConfig":
                                        {
                                            "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                            "Options":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                                        }
                                    ,
                                    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
                                    "NoCopy":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                                }
                        }
                    ],
                    "OpenStdin":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "Privileges":
                        {
                            "CredentialSpec":
                                {
                                    "File":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Registry":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "SELinuxContext":
                                {
                                    "Disable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                                    "Level":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "User":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                        }
                    ,
                    "ReadOnly":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "Secrets":
                    [
                        {
                            "File":
                                {
                                    "GID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "Mode":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "UID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "SecretID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "SecretName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ],
                    "StopGracePeriod":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "StopSignal":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "TTY":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "User":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "ForceUpdate":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "LogDriver":
                {
                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Options":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
                }
            ,
            "Networks":
            [
                {
                    "Aliases":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "Target":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "Placement":
                {
                    "Constraints":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.hostname!=node3.corp.example.com"]),
    primitives.restler_static_string(""",
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.role!=manager"]),
    primitives.restler_static_string(""",
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.labels.type==production"]),
    primitives.restler_static_string("""
                    ],
                    "Platforms":
                    [
                        {
                            "Architecture":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["x86_64"]),
    primitives.restler_static_string(""",
                            "OS":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["linux"]),
    primitives.restler_static_string("""
                        }
                    ],
                    "Preferences":
                    [
                        {
                            "Spread":
                                {
                                    "SpreadDescriptor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.labels.datacenter"]),
    primitives.restler_static_string("""
                                }
                        },
                        {
                            "Spread":
                                {
                                    "SpreadDescriptor":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["node.labels.rack"]),
    primitives.restler_static_string("""
                                }
                        }
                    ]
                }
            ,
            "PluginSpec":
                {
                    "Disabled":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "PluginPrivilege":
                    [
                        {
                            "Description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "Value":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ]
                        }
                    ],
                    "Remote":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "Resources":
                {
                    "Limits":
                        {
                            "GenericResources":
                                [
                                    {
                                        "DiscreteResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["SSD"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_int("1", examples=['"3"']),
    primitives.restler_static_string("""
                                            }
                                    },
                                    {
                                        "NamedResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GPU"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["UUID1"]),
    primitives.restler_static_string("""
                                            }
                                    },
                                    {
                                        "NamedResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GPU"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["UUID2"]),
    primitives.restler_static_string("""
                                            }
                                    }
                                ]
                            ,
                            "MemoryBytes":"""),
    primitives.restler_fuzzable_int("1", examples=["8272408576"]),
    primitives.restler_static_string(""",
                            "NanoCPUs":"""),
    primitives.restler_fuzzable_int("1", examples=["4000000000"]),
    primitives.restler_static_string("""
                        }
                    ,
                    "Reservation":
                        {
                            "GenericResources":
                                [
                                    {
                                        "DiscreteResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["SSD"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_int("1", examples=['"3"']),
    primitives.restler_static_string("""
                                            }
                                    },
                                    {
                                        "NamedResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GPU"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["UUID1"]),
    primitives.restler_static_string("""
                                            }
                                    },
                                    {
                                        "NamedResourceSpec":
                                            {
                                                "Kind":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["GPU"]),
    primitives.restler_static_string(""",
                                                "Value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["UUID2"]),
    primitives.restler_static_string("""
                                            }
                                    }
                                ]
                            ,
                            "MemoryBytes":"""),
    primitives.restler_fuzzable_int("1", examples=["8272408576"]),
    primitives.restler_static_string(""",
                            "NanoCPUs":"""),
    primitives.restler_fuzzable_int("1", examples=["4000000000"]),
    primitives.restler_static_string("""
                        }
                }
            ,
            "RestartPolicy":
                {
                    "Condition":"""),
    primitives.restler_fuzzable_group("Condition", ['none','on-failure','any']  ,quoted=True),
    primitives.restler_static_string(""",
                    "Delay":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "MaxAttempts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "Window":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
                }
            ,
            "Runtime":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "UpdateConfig":
        {
            "Delay":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "FailureAction":"""),
    primitives.restler_fuzzable_group("FailureAction", ['continue','pause','rollback']  ,quoted=True),
    primitives.restler_static_string(""",
            "MaxFailureRatio":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
            "Monitor":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "Order":"""),
    primitives.restler_fuzzable_group("Order", ['stop-first','start-first']  ,quoted=True),
    primitives.restler_static_string(""",
            "Parallelism":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/services/{id}/update"
)
req_collection.add_request(request)

# Endpoint: /session, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("session"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/session"
)
req_collection.add_request(request)

# Endpoint: /swarm, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("swarm"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/swarm"
)
req_collection.add_request(request)

# Endpoint: /swarm/init, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("swarm"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("init"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "AdvertiseAddr":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["192.168.1.1:2377"]),
    primitives.restler_static_string(""",
    "ForceNewCluster":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string(""",
    "ListenAddr":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["0.0.0.0:2377"]),
    primitives.restler_static_string(""",
    "Spec":
        {
            "CAConfig":
                {
                }
            ,
            "Dispatcher":
                {
                }
            ,
            "EncryptionConfig":
                {
                    "AutoLockManagers":"""),
    primitives.restler_fuzzable_bool("true", examples=['"false"']),
    primitives.restler_static_string("""
                }
            ,
            "Orchestration":
                {
                }
            ,
            "Raft":
                {
                }
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/swarm/init"
)
req_collection.add_request(request)

# Endpoint: /swarm/join, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("swarm"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("join"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "AdvertiseAddr":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["192.168.1.1:2377"]),
    primitives.restler_static_string(""",
    "JoinToken":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["SWMTKN-1-3pu6hszjas19xyp7ghgosyx9k8atbfcr8p2is99znpy26u2lkl-7p73s1dx5in4tatdymyhg9hu2"]),
    primitives.restler_static_string(""",
    "ListenAddr":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["0.0.0.0:2377"]),
    primitives.restler_static_string(""",
    "RemoteAddrs":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["[\"node1:2377\"]"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/swarm/join"
)
req_collection.add_request(request)

# Endpoint: /swarm/leave, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("swarm"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("leave"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("force="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/swarm/leave"
)
req_collection.add_request(request)

# Endpoint: /swarm/unlock, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("swarm"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unlock"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "UnlockKey":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["SWMKEY-1-7c37Cc8654o6p38HnroywCi19pllOnGtbdZEgtKxZu8"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/swarm/unlock"
)
req_collection.add_request(request)

# Endpoint: /swarm/unlockkey, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("swarm"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unlockkey"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/swarm/unlockkey"
)
req_collection.add_request(request)

# Endpoint: /swarm/update, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("swarm"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rotateWorkerToken="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rotateManagerToken="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rotateManagerUnlockKey="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "CAConfig":
        {
            "ExternalCAs":
            [
                {
                    "CACert":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "Options":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
                    "Protocol":"""),
    primitives.restler_fuzzable_group("Protocol", ['cfssl'] , default_enum="cfssl" ,quoted=True),
    primitives.restler_static_string(""",
                    "URL":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "ForceRotate":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "NodeCertExpiry":"""),
    primitives.restler_fuzzable_int("1", examples=["7776000000000000"]),
    primitives.restler_static_string(""",
            "SigningCACert":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "SigningCAKey":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "Dispatcher":
        {
            "HeartbeatPeriod":"""),
    primitives.restler_fuzzable_int("1", examples=["5000000000"]),
    primitives.restler_static_string("""
        }
    ,
    "EncryptionConfig":
        {
            "AutoLockManagers":"""),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string("""
        }
    ,
    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["""{
  "com.example.corp.department": "engineering",
  "com.example.corp.type": "production"
}"""]),
    primitives.restler_static_string(""",
    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["default"]),
    primitives.restler_static_string(""",
    "Orchestration":
        {
            "TaskHistoryRetentionLimit":"""),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("""
        }
    ,
    "Raft":
        {
            "ElectionTick":"""),
    primitives.restler_fuzzable_int("1", examples=["3"]),
    primitives.restler_static_string(""",
            "HeartbeatTick":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
            "KeepOldSnapshots":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "LogEntriesForSlowFollowers":"""),
    primitives.restler_fuzzable_int("1", examples=["500"]),
    primitives.restler_static_string(""",
            "SnapshotInterval":"""),
    primitives.restler_fuzzable_int("1", examples=["10000"]),
    primitives.restler_static_string("""
        }
    ,
    "TaskDefaults":
        {
            "LogDriver":
                {
                    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["json-file"]),
    primitives.restler_static_string(""",
                    "Options":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["""{
  "max-file": "10",
  "max-size": "100m"
}"""]),
    primitives.restler_static_string("""
                }
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/swarm/update"
)
req_collection.add_request(request)

# Endpoint: /system/df, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("system"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("df"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/system/df"
)
req_collection.add_request(request)

# Endpoint: /tasks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tasks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tasks"
)
req_collection.add_request(request)

# Endpoint: /tasks/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tasks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tasks/{id}"
)
req_collection.add_request(request)

# Endpoint: /tasks/{id}/logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tasks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("details="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("follow="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stdout="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stderr="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("timestamps="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tail="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tasks/{id}/logs"
)
req_collection.add_request(request)

# Endpoint: /version, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/version"
)
req_collection.add_request(request)

# Endpoint: /volumes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("volumes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/volumes"
)
req_collection.add_request(request)

# Endpoint: /volumes/create, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("volumes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("create"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Driver":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["custom"]),
    primitives.restler_static_string(""",
    "Labels":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"com.example.some-label\":\"some-value\",\"com.example.some-other-label\":\"some-other-value\"}"]),
    primitives.restler_static_string(""",
    "Name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["tardis"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_volumescreatepost,
            'dependencies':
            [
                _volumes_create_post_Driver.writer(),
                _volumes_create_post_Labels.writer(),
                _volumes_create_post_Name.writer(),
                _volumes_create_post_Options.writer()
            ]
        }

    },

],
requestId="/volumes/create"
)
req_collection.add_request(request)

# Endpoint: /volumes/prune, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("volumes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prune"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/volumes/prune"
)
req_collection.add_request(request)

# Endpoint: /volumes/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("volumes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("force="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/volumes/{name}"
)
req_collection.add_request(request)

# Endpoint: /volumes/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1.33"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("volumes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/volumes/{name}"
)
req_collection.add_request(request)
