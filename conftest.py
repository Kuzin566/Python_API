import pytest


@pytest.fixture(autouse=True)
def set_up():
    print("\nStart test")
    yield
    print("Finish test")
