""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /geomarks/copy, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/pub/geomark"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("geomarks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("copy"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("geomarkUrl="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("resultFormat="),
    primitives.restler_fuzzable_group("resultFormat", ['json','xml','kml','kmz','shp','shpz','geojson','gml','wkt']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("allowOverlap="),
    primitives.restler_fuzzable_group("allowOverlap", ['False','True'] , default_enum="False" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("redirectUrl="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("failureRedirectUrl="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("bufferMetres="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("bufferJoin="),
    primitives.restler_fuzzable_group("bufferJoin", ['ROUND','MITRE','BEVEL'] , default_enum="ROUND" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("bufferCap="),
    primitives.restler_fuzzable_group("bufferCap", ['ROUND','SQUARE','FLAT'] , default_enum="ROUND" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("bufferMitreLimit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("bufferSegments="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: apps.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/geomarks/copy"
)
req_collection.add_request(request)

# Endpoint: /geomarks/new, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/pub/geomark"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("geomarks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("new"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: apps.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/geomarks/new"
)
req_collection.add_request(request)

# Endpoint: /geomarks/{geomarkId}.{fileFormatExtension}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/pub/geomark"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("geomarks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("srid="),
    primitives.restler_fuzzable_group("srid", ['4326','3005','3857','26907','26908','26909','26910','26911'] , default_enum="4326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: apps.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/geomarks/{geomarkId}.{fileFormatExtension}"
)
req_collection.add_request(request)

# Endpoint: /geomarks/{geomarkId}/boundingBox.{fileFormatExtension}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/pub/geomark"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("geomarks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("boundingBox.{fileFormatExtension}"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("srid="),
    primitives.restler_fuzzable_group("srid", ['4326','3005','3857','26907','26908','26909','26910','26911'] , default_enum="4326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: apps.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/geomarks/{geomarkId}/boundingBox.{fileFormatExtension}"
)
req_collection.add_request(request)

# Endpoint: /geomarks/{geomarkId}/feature.{fileFormatExtension}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/pub/geomark"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("geomarks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("feature.{fileFormatExtension}"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("srid="),
    primitives.restler_fuzzable_group("srid", ['4326','3005','3857','26907','26908','26909','26910','26911'] , default_enum="4326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: apps.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/geomarks/{geomarkId}/feature.{fileFormatExtension}"
)
req_collection.add_request(request)

# Endpoint: /geomarks/{geomarkId}/parts.{fileFormatExtension}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/pub/geomark"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("geomarks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("parts.{fileFormatExtension}"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("srid="),
    primitives.restler_fuzzable_group("srid", ['4326','3005','3857','26907','26908','26909','26910','26911'] , default_enum="4326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: apps.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/geomarks/{geomarkId}/parts.{fileFormatExtension}"
)
req_collection.add_request(request)

# Endpoint: /geomarks/{geomarkId}/point.{fileFormatExtension}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/pub/geomark"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("geomarks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("point.{fileFormatExtension}"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("srid="),
    primitives.restler_fuzzable_group("srid", ['4326','3005','3857','26907','26908','26909','26910','26911'] , default_enum="4326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: apps.gov.bc.ca\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/geomarks/{geomarkId}/point.{fileFormatExtension}"
)
req_collection.add_request(request)
