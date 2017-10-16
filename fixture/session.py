import time

class SessionHelper:
    main_menu_xp = '//div[@class="mdi mdi-menu"]'
    guest_label_xp = '//div[text()="Guest"]'
    main_login_button_xp = '//a[text()="Login"]'

    email_input_xp = '//input[@type="text"]'
    password_input_xp = '//input[@type="password"]'
    login_button_xp = '//div[text()="Login"]'
    greeting_xp = '//h1[1]'
    return_button_xp = '//div[text()="Return to homepage"]'

    def __init__(self,app):
        self.app = app

    def login(self,username, psw):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_xpath(self.main_menu_xp).click()
        time.sleep(2)
        driver.find_element_by_xpath(self.main_login_button_xp).click()
        driver.find_element_by_xpath(self.email_input_xp).send_keys(username)
        driver.find_element_by_xpath(self.password_input_xp).send_keys(psw)
        driver.find_element_by_xpath(self.login_button_xp).click()


    def logout(self):
        pass
