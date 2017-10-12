from locust import HttpLocust, TaskSet, task


class GeocodeResponse(TaskSet):

    _GITHUB_STREET_ADDRESS = "maps/api/geocode/json?&address=88%20Colin%20P%20Kelly%20Jr%20St.%20San%20Francisco%2C%20CA"  # noqa
    _GITHUB_LATLNG = "maps/api/geocode/json?latlng=37.78226710000001,-122.3912479"

    @staticmethod
    def api_key():
        return "&key=AIzaSyCEF5uFW7KYGLUpzqpgWwYrlqXpqjz8PCw"

    @task
    def geocode(self):
        self.client.get(self._GITHUB_STREET_ADDRESS + self.api_key())

    @task
    def reverse_geocode(self):
        self.client.get(self._GITHUB_LATLNG + self.api_key())


class GoogleMapsUser(HttpLocust):
    host = "https://maps.googleapis.com/"
    task_set = GeocodeResponse
