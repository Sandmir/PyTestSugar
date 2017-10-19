import time
import allure

from library.APIGmail import api_get_gmail
from library.lib_selenium import *


def receive_new_psw():
    GMAIL = api_get_gmail()

    user_id = 'me'
    label_id_one = 'INBOX'
    label_id_two = 'UNREAD'

    unread_msgs = GMAIL.users().messages().list(userId=user_id, labelIds=[label_id_one, label_id_two]).execute()

    mssg_list = unread_msgs['messages']
    m_id = mssg_list[0]['id']
    message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()

    snippet = message['snippet']

    new_psw = snippet.split("Your new password to is: ")[1]
    # save new psw
    file_psw = open('/Privite/Study/Python/PyTestSugar/data/password.txt', 'w')
    file_psw.write(new_psw)
    file_psw.close()


class SessionHelper:
    main_menu_xp = '//div[@class="mdi mdi-menu"]'
    guest_label_xp = '//div[text()="Guest"]'
    main_login_button_xp = '//a[text()="Login"]'

    email_input_xp = '//input[@type="text"]'
    password_input_xp = '//input[@type="password"]'
    login_button_xp = '//div[text()="Login"]'
    logout_button_xp = '//div[text()="Logout"]'

    greeting_xp = '//h1[1]'
    return_button_xp = '//div[text()="Return to homepage"]'

    invalid_cred_xp = "//*[@class='context-info']"
    forgot_psw_xp = "//*[text()='Forgot Password?']"
    forgot_psw_field_xp = "//input[@class='input__input-control']"
    input_forget_psw = "//div[text()='Password']/../input"
    reset_psw = "//*[text()='Reset Password']"
    send_new_psw_message_xp = "//*[text()='A new password has been sent to your EMail address.']"

    reset_error_msg = "//div[@class='context-info']"

    def __init__(self, app):
        self.app = app

    def get_new_psw(self):
        with allure.step('Get valid password'):
            file_psw = open('//Privite/Study/Python/PyTestSugar/Data/password.txt', 'r')
            new_psw = file_psw.readline()
            file_psw.close()
            return new_psw

    def login(self, username = 'testmobile.marina@gmail.com',psw = ''):
        with allure.step('Login step'):
            driver = self.app.driver
            self.app.open_home_page()
            wait_and_click(driver, self.main_menu_xp)
            time.sleep(2)
            wait_and_click(driver, self.main_login_button_xp)
            wait_and_send_keys(driver, self.email_input_xp, username)
            wait_and_send_keys(driver, self.password_input_xp, psw)
            wait_and_click(driver, self.login_button_xp)

    def logout(self):
        with allure.step('Logout step'):
            driver = self.app.driver
            wait_and_click(driver, self.main_menu_xp)
            time.sleep(2)
            wait_and_click(driver, self.logout_button_xp)

    def forget_psw(self, username=''):
        with allure.step('Forget PSW'):
            driver = self.app.driver
            self.app.open_home_page()
            wait_and_click(driver, self.main_menu_xp)
            sleep(2)
            wait_and_click(driver, self.main_login_button_xp)
            sleep(3)
            wait_and_click(driver, self.forgot_psw_xp)
            wait_and_send_keys(driver, self.forgot_psw_field_xp, username)
            wait_and_click(driver, self.reset_psw)
            sleep(3)

    def return_to_home_page(self):
        wait_and_click(self.app.driver, self.return_button_xp)
