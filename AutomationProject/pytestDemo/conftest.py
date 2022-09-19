import pytest


# Confest used to declare one global fixture when you have multiple test cases

# When setting up a confest and use it globally all your test cases should be under a class and that way you can
# eliminate passing fixture method name in every single other test case. Example below

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture(scope="class")
def dataload():
    return ("Nasimi Khalimzoda", "nasimikhalimzoda@gmail.com",
            "929-441-8999")


@pytest.fixture(params=[("chrome", "Naseem"),
                        ("Firefox", "Khalimzoda"),
                        ("IE", "Dilafruz")])
def crossbrowser(request):
    return request.param
