# GitHub Senior Test Engineer Exercise

<iframe src="https://githubbadge.appspot.com/silne30?s=1" style="border: 0;height: 142px;width: 200px;overflow: hidden;" frameBorder="0"></iframe>

Thanks for taking a look at my GitHub **Senior** Test Engineer exercise. This submission is actually
a mixture of REST API tests, Performance tests, and CI Configuration.

 [![Build Status](https://ci.powercoder.tech/buildStatus/icon?job=github_test)](https://ci.powercoder.tech/job/github_test/)
 [![SSL Rating](https://sslbadge.org/?domain=ci.powercoder.tech)](https://www.ssllabs.com/ssltest/analyze.html?d=ci.powercoder.tech)
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Running The Tests Locally

To run this test suite, one will already assume that you have [python 2.7](https://www.python.org/download/releases/2.7/) installed along with 
[Virtualenv](https://virtualenv.pypa.io/en/stable/) (or perhaps [VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)).

### Using Tox

The easiest way to run the test suite is through [Tox](https://tox.readthedocs.io/en/latest/).

* [Tox](https://tox.readthedocs.io/en/latest/)
* Navigate to root of repository
* Run `tox`

### Using Py.Test Directly
* Install [Py.Test](https://docs.pytest.org/en/latest/)
* `cd tests` from the root of repository.
* Run ` pytest --capture=sys --spec`

    
