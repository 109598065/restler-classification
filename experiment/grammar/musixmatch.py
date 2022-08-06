""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /album.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("album.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("album_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/album.get"
)
req_collection.add_request(request)

# Endpoint: /album.tracks.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("album.tracks.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("album_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_has_lyrics="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/album.tracks.get"
)
req_collection.add_request(request)

# Endpoint: /artist.albums.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("artist.albums.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("artist_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("s_release_date="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("g_album_name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/artist.albums.get"
)
req_collection.add_request(request)

# Endpoint: /artist.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("artist.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("artist_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/artist.get"
)
req_collection.add_request(request)

# Endpoint: /artist.related.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("artist.related.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("artist_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/artist.related.get"
)
req_collection.add_request(request)

# Endpoint: /artist.search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("artist.search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_artist="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_artist_id="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/artist.search"
)
req_collection.add_request(request)

# Endpoint: /chart.artists.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chart.artists.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("country="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chart.artists.get"
)
req_collection.add_request(request)

# Endpoint: /chart.tracks.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chart.tracks.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("country="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_has_lyrics="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chart.tracks.get"
)
req_collection.add_request(request)

# Endpoint: /matcher.lyrics.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matcher.lyrics.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_track="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_artist="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/matcher.lyrics.get"
)
req_collection.add_request(request)

# Endpoint: /matcher.subtitle.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matcher.subtitle.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_track="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_artist="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_subtitle_length="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_subtitle_length_max_deviation="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/matcher.subtitle.get"
)
req_collection.add_request(request)

# Endpoint: /matcher.track.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("matcher.track.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_artist="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_track="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_has_lyrics="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_has_subtitle="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/matcher.track.get"
)
req_collection.add_request(request)

# Endpoint: /track.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("track.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("track_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/track.get"
)
req_collection.add_request(request)

# Endpoint: /track.lyrics.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("track.lyrics.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("track_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/track.lyrics.get"
)
req_collection.add_request(request)

# Endpoint: /track.search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("track.search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_track="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_artist="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q_lyrics="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_artist_id="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_music_genre_id="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_lyrics_language="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("f_has_lyrics="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("s_artist_rating="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("s_track_rating="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quorum_factor="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/track.search"
)
req_collection.add_request(request)

# Endpoint: /track.snippet.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("track.snippet.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("track_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/track.snippet.get"
)
req_collection.add_request(request)

# Endpoint: /track.subtitle.get, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/ws/1.1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("track.subtitle.get"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("callback="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("track_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.musixmatch.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/track.subtitle.get"
)
req_collection.add_request(request)
