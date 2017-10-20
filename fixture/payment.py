import time
import allure

from library.APIGmail import api_get_gmail
from library.lib_selenium import *


class PaymentHelper:
    checkout_now_button = '//div[text()="Checkout now"]'
    checkout_button = '//div[text()="Checkout"]'
    accept_checkbox = '//input[@type="checkbox"]'
    confirm_button = '//div[text()="Confirm Order"]'

    cart_owner_field = '//div[text()="Card Owner"]/../input'
    cart_number_field = '//div[text()="Card Number"]/../input'
    mount_select = '//div[text()="Expiry Month"]/../select'
    year_select = '//div[text()="Expiry Year"]/../select'
    cvv_field = '//div[text()="Card Security Code (CVV2)"]/../input'

    complete_order = '//div[text()="Complete Order"]'

    error_number = "(TESTMODE) The credit cart number is invalid."
    error_owner = "Invalid card owner name"

    order_added = "Order was successfully added."

    def __init__(self, app):
        self.app = app

    def start_checkout(self):
        with allure.step('Click Checkout button'):
            wait_and_click(self.app.driver, self.checkout_button)
            wait_and_click(self.app.driver, self.checkout_now_button)

    def submit_checkout(self):
        sleep(3)
        self.app.driver.find_element_by_xpath('//input[@type="checkbox"]').click()
        wait_and_click(self.app.driver, self.confirm_button)

    def fill_in_payment_info(self, cart):
        with allure.step('Fill in the Credit cart info'):
            driver = self.app.driver
            wait_and_send_keys(driver, self.cart_owner_field, cart.owner)
            wait_and_send_keys(driver, self.cart_number_field, cart.number)
            wait_and_select(driver, self.mount_select, cart.month)
            wait_and_select(driver, self.year_select, cart.year)
            wait_and_send_keys(driver, self.cvv_field, cart.cvv)
