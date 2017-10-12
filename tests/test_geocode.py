import json
import jsonschema
import pytest
import urllib2


class TestGeocode(object):

    @pytest.mark.parametrize("address", [
        "?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA",
        "?address=232000",
        "?address=4110",
        "?address=1+Frost+Street,+Gilbert,+AR",
        "?address=Narsarsuaq,+Greenland",
        "?address=chekalin,+russia%20301414",
        "?address=51+Kalakaua+St,+Hilo,+HI%2096720",
        "?address=Mala,+Sweden",
        "?address=!KS!"
    ])
    def test_return_geocode_for_valid_address(self, api_key, address, geocode_schema, https_url):

        url = https_url + address + api_key

        data = urllib2.urlopen(url).read()
        jsonschema.Draft4Validator(json.loads(geocode_schema)).validate(json.loads(data))

    @pytest.mark.parametrize(("address", "params"), [
        ("?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA",
         "&components=administrative_area:TX|country:US"),
        ("?address=38297+San+Cristobal+de+La+Laguna",
         "&components=locality:santa+cruz|country:ES"),
        ("?address=272+Gonghang-ro,+Jung-gu,+Incheon",
         "&language=ko")
    ])
    def test_return_geocode_for_valid_address_with_valid_parameters(
            self, api_key, address, params, geocode_schema, https_url):

        url = https_url + address + params + api_key

        data = urllib2.urlopen(url).read()
        jsonschema.Draft4Validator(json.loads(geocode_schema)).validate(json.loads(data))

    @pytest.mark.parametrize("latlng", [
        "?latlng=46.406876,124.423651",
        "?latlng=72.945138,-122.944512",
        "?latlng=40.714224,-73.96145",
        "?latlng=37.78226710000001,-122.3912479",
        "?latlng=51.755881,-177.260921"
    ])
    def test_return_address_for_valid_geocode(self, api_key, latlng, reverse_geocode_schema, https_url):

        url = https_url + latlng + api_key

        data = urllib2.urlopen(url).read()
        jsonschema.Draft4Validator(json.loads(reverse_geocode_schema)).validate(json.loads(data))

    @pytest.mark.parametrize(("latlng", "params"), [
        ("?latlng=46.406876,124.423651",
         "&language=zh-TW"),
        ("?latlng=72.945138,-122.944512",
         "&language=gu"),
        ("?latlng=40.714224,-73.96145",
         "&language=te"),
        ("?latlng=37.78226710000001,-122.3912479",
         "&language=ml"),
        ("?latlng=51.755881,-177.260921",
         "&language=gl")
    ])
    def test_return_address_for_valid_geocode_with_valid_parameters(
            self, api_key, latlng, params, reverse_geocode_schema, https_url):

        url = https_url + latlng + params + api_key

        data = urllib2.urlopen(url).read()
        jsonschema.Draft4Validator(json.loads(reverse_geocode_schema)).validate(json.loads(data))
