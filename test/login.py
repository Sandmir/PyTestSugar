import pytest
import allure
from fixture.application import Application
from time import sleep


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_valid_credentials(app):
    app.session.login('testmobile.marina@gmail.com', 'c980159c4c')
    sleep(2)
    with allure.step('Verification - valid credentials'):
        greeting = app.driver.find_element_by_xpath(app.session.greeting_xp).text
        assert greeting.split(",")[0] == "Welcome back"


def test_login_invalid_psw(app):
    app.session.login('testmobile.marina@gmail.com', '12345')
    sleep(2)
    with allure.step('Get error message.'):
        greeting = app.driver.find_element_by_xpath(app.session.invalid_cred_xp).text
    with allure.step('Verify error message: Warning: No match for E-Mail Address and/or Password.'):
        assert greeting.split(",")[0] == "Warning: No match for E-Mail Address and/or Password."


