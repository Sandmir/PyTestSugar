from appium import webdriver

import pytest

from fixture.session import SessionHelper


class Application:

    def __init__(self):
        capabilities = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '7.0',
            'browserName': 'Chrome'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(20)
        self.session = SessionHelper(self)

    def open_home_page(self):
        base_url = 'http://test.sugaringfactory.com/'
        self.driver.get(base_url)

    def destroy(self):
        self.driver.quit()