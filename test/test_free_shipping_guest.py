import allure
import pytest
from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_prices_match_guest(appGuest):
    quantity = 1
    cost_of_goods_exp = 0

    appGuest.open_home_page()
    if not appGuest.shopingCart.cart_empty:
        appGuest.shopingCart.remove_all_items_from_shopping_cart()

    with allure.step('Select all items with Free Shipping'):
        goods = appGuest.shopingCart.select_items_free_ship()
        q_goods = len(goods)
        for i in range(q_goods):
            sleep(1)
            goods[i].click()
            sleep(1)
            original_price = appGuest.shopingCart.get_original_price()
            # print("item's price = ",original_price)
            appGuest.shopingCart.add_quantity(quantity)
            sleep(1)
            cost_of_goods_exp += float(original_price)
            if appGuest.shopingCart.multiselect_kit:
                with allure.step('Add kit into the Cart'):
                    sleep(1)
                    item_count = appGuest.shopingCart.get_size_of_kit()
                    appGuest.shopingCart.multi_item_add(str(item_count))
            # print("price in the cart = ", appGuest.shopingCart.get_cart_info())
            appGuest.driver.back()
            goods = appGuest.shopingCart.select_items_free_ship()
        cart_info = appGuest.shopingCart.get_cart_info()
        # print("cost exp:",cart_info)
        cost_of_goods_exp = round(cost_of_goods_exp, 2)
        # print("cost act:", cost_of_goods_exp)
        with allure.step('Verify that expected cost = actual cost'):
            assert cost_of_goods_exp == float(cart_info), "Cost doesn't match!!"
