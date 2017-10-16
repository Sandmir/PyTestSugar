import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_valid_credentials(app):
    app.session.login('testmobile.marina@gmail.com', 'c980159c4c')



