import allure
import pytest
from model.credit_cart import VisaCart, Mastercard, MastercardDebit, AmericanExpress, Discover, DinersClub, JCB
from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def credit_cart_valid(app, cart):
    quantity = 2
    app.session.login(psw=app.session.get_new_psw())
    app.session.return_to_home_page()
    if app.shopingCart.cart_empty:
        app.shopingCart.select_first_item_to_cart()
        sleep(2)
        with allure.step('Add %s items to the Cart' % quantity):
            app.shopingCart.add_quantity(quantity)
    app.payment.start_checkout()
    app.payment.submit_checkout()

    app.payment.fill_in_payment_info(cart)
    sleep(3)
    wait_and_click(app.driver, app.payment.complete_order)
    with allure.step('Complete order: %s' % cart.type):
        assert text_is_present(app.driver, app.payment.order_added), "Payment: %s - fail!! " % cart.type


def test_visa(app):
    credit_cart_valid(app, VisaCart())


def test_mastercard(app):
    credit_cart_valid(app, Mastercard())


def test_MastercardDebit(app):
    credit_cart_valid(app, MastercardDebit())


def test_AmericanExpress(app):
    credit_cart_valid(app, AmericanExpress())


def test_Discover(app):
    credit_cart_valid(app, Discover())


def test_DinersClub(app):
    credit_cart_valid(app, DinersClub())


def test_JCB(app):
    credit_cart_valid(app, JCB())
