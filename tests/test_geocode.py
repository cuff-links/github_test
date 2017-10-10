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
        "?address=Mala,+Sweden"
    ])
    def test_return_geocode_for_valid_address(self, api_key, address):

        schema = open('support/schemas/geocode_schema.json').read()

        url = "https://maps.googleapis.com/maps/api/geocode/json" + address + api_key

        data = urllib2.urlopen(url).read()
        jsonschema.Draft4Validator(json.loads(schema)).validate(json.loads(data))
