import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_printsecondcreditcard():
    msg = "My First Program"
    assert msg == "My First Program", "Two strings do not match"
