# Performance Tests

The performance testing that this suite uses is written using [Locust](https://docs.locust.io/en/latest/). These
tests use the locust tool to hit a couple of REST endpoints with valid data to see how the API
performs under stress.

## Run the tests

Locust allows you to run the tests using its Web UI to or you can run from the command line.

You can specify the `--csv` flag to create a .csv file with the data from the test run. This makes it easy to graph the results.

### With Web UI
 
If you run from the web UI, you have to manually stop the test by hitting the large stop button.

* Run `locust` 
* Navigate to `http://127.0.0.1:8089` 
* Select Number of Users to Simulate and Hatch Rate
* Click Start Swarming

### Without Web UI

If you run without the Web UI, then the load tests will continuously run, spawning the chosen users per second until the test hits the number of users to simulate. Then it will repeat.
* Run `locust -f --no-web -c {number_of_users_to_simulate} -r {hatch_rate} -n {number_of_requests}`
* If the number of requests is not specified, the tests will run continuously until process is killed. 
* **NOTE** The number of requests is not exact. If you specify 2500 requests, you can wind up doing with more. If have seen up to %10 more (2,750 requests). Keep that in mind when handling query limits.