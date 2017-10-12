import json
import jsonschema
import pytest
import urllib2


class TestNegativeGeocode(object):

    @pytest.mark.parametrize("address", [
        "?address=9999+Fakery+Road+Falsehood,+ZZ",
        "?address=JonJon,+HT",
        "?address=Zuklamat,+NY",
        '?address=$#%%$##',
        "?address=<iframe%20src='www.google.com'></iframe>",
        "?address=%20%20%20%20%20%20%20%20%20%20%20"
    ])
    def test_return_zero_results_for_fake_addresses(
            self, api_key, address, request_denied_zero_results_invalid_request_schema, https_url):

        url = https_url + address + api_key

        data = json.loads(urllib2.urlopen(url).read())
        jsonschema.Draft4Validator(json.loads(request_denied_zero_results_invalid_request_schema)
                                   ).validate(data)

        assert data['status'] == "ZERO_RESULTS"

    @pytest.mark.parametrize("latlng", [
        "?latlng=abcd,wxyz",
        "?latlng=9999,-9999",
        "?latlng=40.714224a,-73.961452",
        "?latlng=40.714224,-73.961452a",
        "?latlng=40.714%20224,-73.961452",
        "?latlng=40.714224,-73.96%201452",
        "?latlng=40.714224!,-73.961452",
        "?latlng=40.714224,-73.961452!"
    ])
    def test_http_error_thrown_for_invalid_latlng(
            self, api_key, latlng, https_url):
        url = https_url + latlng + api_key
        with pytest.raises(urllib2.HTTPError) as error:
            json.loads(urllib2.urlopen(url).read())
        assert str(error.value) == "HTTP Error 400: Bad Request"
