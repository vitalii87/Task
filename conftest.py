from Vit_test.main import Main
import pytest



@pytest.fixture()
def app():
    app = Main()
    return app
