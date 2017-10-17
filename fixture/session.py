import time
import allure
from library.lib_selenium import *

class SessionHelper:
    main_menu_xp = '//div[@class="mdi mdi-menu"]'
    guest_label_xp = '//div[text()="Guest"]'
    main_login_button_xp = '//a[text()="Login"]'

    email_input_xp = '//input[@type="text"]'
    password_input_xp = '//input[@type="password"]'
    login_button_xp = '//div[text()="Login"]'
    greeting_xp = '//h1[1]'
    return_button_xp = '//div[text()="Return to homepage"]'

    invalid_cred_xp = "//*[@class='context-info']"
    forgot_psw_xp = "//*[text()='Forgot Password?']"
    forgot_psw_field_xp = "//input[@class='input__input-control']"
    input_forget_psw = "//div[text()='Password']/../input"
    reset_psw = "//*[text()='Reset Password']"
    send_new_psw_message_xp = "//*[text()='A new password has been sent to your EMail address.']"

    reset_psw_error = "//*[text()='Warning: The E-Mail Address was not found in our records, please try again!']"

    def __init__(self,app):
        self.app = app

    def login(self,username, psw):
        with allure.step('Login step'):
            driver = self.app.driver
            self.app.open_home_page()
            wait_and_click(driver, self.main_menu_xp)
            time.sleep(2)
            wait_and_click(driver, self.main_login_button_xp)
            wait_and_send_keys(driver, self.email_input_xp,username)
            wait_and_send_keys(driver, self.password_input_xp, psw)
            wait_and_click(driver, self.login_button_xp)

    def logout(self):
        pass
