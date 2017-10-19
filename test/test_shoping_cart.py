import allure
import pytest

from library.lib_assert import Assert
from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_add_firs_item_to_cart(app):
    quantity = 2
    app.session.login(psw=app.session.get_new_psw())
    app.session.return_to_home_page()
    if not app.shopingCart.cart_empty:
        app.shopingCart.remove_all_items_from_shopping_cart()
    with allure.step('Select first item'):
        app.shopingCart.select_first_item_to_cart()
    sleep(2)
    # original_price  = app.shopingCart.get_original_price()
    with allure.step('Add %s items to the Cart' % quantity):
          app.shopingCart.add_quantity(quantity)
    with allure.step('Get quantity from the Cart'):
          cart_info = app.shopingCart.get_cart_info(type ='qn')
    with allure.step('Verify quantity = %s' %quantity):
         assert quantity == cart_info, "Quantity doesn't match!!"
    app.session.logout()


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_prices_match(app):
    quantity = 1
    app.session.login(psw=app.session.get_new_psw())
    app.session.return_to_home_page()
    if not app.shopingCart.cart_empty:
        app.shopingCart.remove_all_items_from_shopping_cart()
    with allure.step('Select first item'):
        app.shopingCart.select_first_item_to_cart()
    sleep(2)
    original_price  = app.shopingCart.get_original_price()
    with allure.step('Add %s items to the Cart' % quantity):
          app.shopingCart.add_quantity(quantity)
    with allure.step('Get price from the Cart'):
          cart_info = app.shopingCart.get_cart_info()
    with allure.step('Verify prices: original price = cart price'):
         assert original_price == cart_info, "Prices doesn't match!!"
    app.session.logout()

