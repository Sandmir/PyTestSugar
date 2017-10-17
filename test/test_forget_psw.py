import allure
import pytest

from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_forget_psw_negative(app):
    app.session.forget_psw("uuu")
    with allure.step('Get error message'):
        error_new_psw = get_text(app.driver, app.session.reset_error_msg)
    with allure.step('Verify error message: Warning: The E-Mail Address was not found in our records, please try again!'):
        assert error_new_psw == 'Wrning: The E-Mail Address was not found in our records, please try again!'
