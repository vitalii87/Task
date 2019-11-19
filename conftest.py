from Vit_test.Task.main import Main
import pytest


@pytest.fixture()
def app():
    app = Main()
    return app
