# Tests

## Understanding The Tests

### Parametrizing Tests

The majority of the tests in the `tests/` folder are [parametrized pytest](https://docs.pytest.org/en/latest/parametrize.html) cases. This allows flexibility in the test
cases and uses less code since you can just add new parameters to run multiple test cases. If you have one function that you would like to test with multiple data sets, this 
is very helpful and you can pass the values into your test function as arguments.

*Example of tests without parameters*

```python

class TestWithoutParameters(object):

    def add_one_plus_one(self):
        assert 1 + 1 == 2
        
    def add_two_plus_two(self):
        assert 2 + 2 == 4

```

These two tests would pass just fine. However, imagine if you had to write the same type of tests from 1 to 50. Parameters can help with that.

*Example of tests with parameters*


```python
import pytest
class TestWithParameters(object):

    @pytest.mark.parametrize("arithmetic,expected", [
    ("1+1", 2),
    ("2+2", 4)
    ])
    def test_arithmetic_expression(self, arithmetic, expected):
        assert eval(arithmetic) == expected
```

Writing the tests in this fashion definitely achieves what the tests without parameters did
but it's only one test case. It's also built to scale. Since the `eval()` function in python
will evaluate the expression given, the test is not limited to 
addition. You can put any math expression there with the proper output and it will pass.

### Fixtures

The test cases also made use of pytest's [fixtures](https://docs.pytest.org/en/latest/fixture.html), which allowed us to have helpers inject data or functionality in the tests.
This enabled us to:

* Keep our code simple
* Make changes to fixture data in one place 
* Easily extend multiple test methods with the same functionality
* Modify tests from the command line by using arguments

Fixtures are passed into the test case via argument and they are in `conftest.py`.

## Test Types

There are several types of tests that were written and each test method takes its own set of parameters and makes its own assertions.

**NOTE REGARDING PARAMETERS**

Do not enclose spaces within your parameters  or you will get back a Bad Response Error (400). Make sure to use either a plus sign `+` or the special character for space `%20` to 
achieve the desired result.

### Geocode Tests

#### Test Methods

* `test_return_geocode_for_valid_address`

* `test_return_address_for_valid_geocode`


##### Negative Tests


### Authentication Tests

## Hacking On Tests

## Conventions