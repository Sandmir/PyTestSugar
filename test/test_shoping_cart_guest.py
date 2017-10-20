import allure
import pytest

from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_prices_match_guest(appGuest):
    quantity = 1
    appGuest.open_home_page()
    if not appGuest.shopingCart.cart_empty:
        appGuest.shopingCart.remove_all_items_from_shopping_cart()

    with allure.step('Select first item'):
        appGuest.shopingCart.select_first_item_to_cart()
    sleep(2)
    original_price  = appGuest.shopingCart.get_original_price()
    with allure.step('Add %s items to the Cart' % quantity):
        appGuest.shopingCart.add_quantity(quantity)
    with allure.step('Get price from the Cart'):
          cart_info = appGuest.shopingCart.get_cart_info()
    with allure.step('Verify prices: original price = cart price'):
         assert original_price == cart_info, "Prices doesn't match!!"


def test_add_firs_item_to_cart_guest(appGuest):
    quantity = 2
    appGuest.open_home_page()
    if not appGuest.shopingCart.cart_empty:
        appGuest.shopingCart.remove_all_items_from_shopping_cart()
    with allure.step('Select first item'):
        appGuest.shopingCart.select_first_item_to_cart()
    sleep(2)
    with allure.step('Add %s items to the Cart' % quantity):
        appGuest.shopingCart.add_quantity(quantity)
    with allure.step('Get quantity from the Cart'):
          cart_info = appGuest.shopingCart.get_cart_info(type ='qn')
    with allure.step('Verify quantity = %s' %quantity):
         assert quantity == cart_info, "Quantity doesn't match!!"
