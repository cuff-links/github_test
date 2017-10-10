import json
import jsonschema
import pytest
import urllib2


class TestAuthentication(object):
    # No assertions made on error property because as docs say they are not to be expected.

    @pytest.mark.parametrize("latlng, params", [
        ("?latlng=40.714224,-73.961452", "&location_type=ROOFTOP&result_type=street_address")])
    def test_return_request_denied_when_key_not_provided_for_filtering(
            self, http_url, latlng, params, request_denied_zero_results_invalid_request_schema):
        url = http_url + latlng + params

        data = json.loads(urllib2.urlopen(url).read())
        jsonschema.Draft4Validator(json.loads(request_denied_zero_results_invalid_request_schema)
                                   ).validate(data)
        assert data['status'] == "REQUEST_DENIED"

    @pytest.mark.parametrize("address", [
        "?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA"])
    def test_return_request_denied_when_key_not_needed(
            self, http_url, address, request_denied_zero_results_invalid_request_schema, api_key):
        url = http_url + address + api_key

        data = json.loads(urllib2.urlopen(url).read())
        jsonschema.Draft4Validator(json.loads(request_denied_zero_results_invalid_request_schema)
                                   ).validate(data)
        assert data['status'] == "REQUEST_DENIED"

    @pytest.mark.parametrize("address", [
        "?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA"])
    def test_return_request_denied_when_key_not_valid(
            self, fake_api_key, https_url, address, request_denied_zero_results_invalid_request_schema):
        url = https_url + address + fake_api_key

        data = json.loads(urllib2.urlopen(url).read())
        jsonschema.Draft4Validator(json.loads(request_denied_zero_results_invalid_request_schema)
                                   ).validate(data)
        assert data['status'] == "REQUEST_DENIED"

