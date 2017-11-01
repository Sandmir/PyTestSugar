from fixture.application import Application
import pytest


@pytest.fixture(scope='module')
def appLogin(request):
    fixture = Application()
    fixture.session.login(psw=fixture.session.get_new_psw())
    fixture.session.return_to_home_page()

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope='module')
def appGuest(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# @pytest.fixture(scope='session')
# def stop(request):
#     fixture = Application()
#     request.addfinalizer(fixture.destroy)
#     return fixture