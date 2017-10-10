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
