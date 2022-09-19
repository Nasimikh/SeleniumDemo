import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2:

    def test_editconfigs(self, dataload):
        log = BaseClass.getlogger()
        log.info(dataload[1])
        log.info(dataload[2])
