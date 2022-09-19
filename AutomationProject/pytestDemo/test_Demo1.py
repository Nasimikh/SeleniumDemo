# Command to execute pytest's - ./pytest
# Command to execute a single pytest test - ./pytest <filename>
# Regular expression based on a partial text - ./pytest -k RegularExpression
# - s to print the log in the output
# - v to print more info about executed test
# - The test can be skipped by using @pytest.mark.skip (@ is a tag)
# - The test can be run as part of smoke or regression by using @pytest.mark.smoke before the method
# - @pytest.mark.xfail will still run the test, but won't generate a report with a description of why it failed

import pytest


@pytest.mark.xfail
def test_firstprogram():
    message = "Let's Go Brandon"
    assert message == "Hi", "Two strings do not match"


def test_greetcreditcard():
    print("Good Morning")


def test_crossbrowser(crossbrowser):
    print(crossbrowser)
