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

    @pytest.mark.parametrize("latlng", [
        "?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA"
    ])
    def test_return_address_for_valid_geocode(self, api_key, latlng, reverse_geocode_schema, https_url):

        url = https_url + latlng + api_key

        data = urllib2.urlopen(url).read()
        jsonschema.Draft4Validator(json.loads(reverse_geocode_schema)).validate(json.loads(data))
