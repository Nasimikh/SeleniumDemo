import pytest


@pytest.mark.usefixtures("setup")
class TestDemo:

    def test_fixturedemo(self):
        print("I will be executing fixtureDemo")

    def test_fixturedemo1(self):
        print("I will be executing fixtureDemo1")

    def test_fixturedemo2(self):
        print("I will be executing fixtureDemo2")

    def test_fixturedemo3(self):
        print("I will be executing fixtureDemo3")

