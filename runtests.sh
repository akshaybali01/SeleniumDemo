#!/bin/bash
# stop execution on error
set -e
# run tests and generate allure results
pytest
#generate and open allure report
allure serve allure-results

