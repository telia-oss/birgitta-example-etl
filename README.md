# Birgitta Example ETL

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://en.wikipedia.org/wiki/MIT_License)
[![Build Status](https://travis-ci.com/telia-oss/birgitta-example-etl.svg?branch=master)](https://travis-ci.org/telia-oss/birgitta-example-etl)
[![PyPI](https://img.shields.io/pypi/v/birgitta-example-etl.svg)](https://pypi.python.org/pypi/birgitta-example-etl)
[![Coverage Status](https://coveralls.io/repos/github/telia-oss/birgitta-example-etl/badge.svg?branch=master)](https://coveralls.io/github/telia-oss/birgitta-example-etl?branch=master)

`birgitta-example-etl` is an example project to
demonstrate how Birgitta can be used.

Birgitta is a Python ETL test and schema framework,
providing automated tests for pyspark notebooks/recipes.

Birgitta allows doing solid ETL and ML, while still liberally
allowing imperfect notebook code, enabling a
`DataOps <https://www.dataopsmanifesto.org>` way of
working which is both solid and agile, not killing
Data Scientist flexibility by excessive coding standards in notebooks.

In addition to running recipetests on your local dev machine or on
a CI/CD server, there is support for running recipetests
as [Dataiku](https://www.dataiku.com] DSS Scenarios.