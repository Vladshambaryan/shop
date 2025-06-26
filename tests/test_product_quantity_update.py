import pytest

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
"""with allure.step("Send request post "):"""

"""Изменение количества товара в корзине"""
class TestProductQuantityUpdate:
    # Тестовые данные
    cart_is_empty = "Your shopping cart is empty!"
    continue_shopping_button = "Continue Shopping"
    product_name = "Bamboo Glass Jar"
    quantity = "Quantity: 1"


    """Изменение количества товара в корзине"""

    @pytest.mark.regression
    def test_product_quantity_update(self, page, shop_url):
        # Инициализация страниц
        home_page = HomePage(page)
        cart_page = CartPage(page)
        product_page = ProductPage(page)

        # Открываем магазин
        home_page.navigate(shop_url)
        home_page.verify_products_count(9)
        # Выбираем первый товар
        home_page.click_first_product()
        # Добавить товар в корзину
        product_page.add_to_cart()
        product_page.verify_cart_updated("1")
        # Перейти в корзину
        product_page.click_cart()
        cart_page.verify_text_product_count_in_cart(self.quantity)
        cart_page.click_continue_sopping()
        # Выбирать восьмой товар
        home_page.click_eighth_product()
        product_page.verify_product_name(self.product_name)
        # Изменить количество на 4
        product_page.change_quantity()
        product_page.add_to_cart()
        product_page.verify_cart_updated("5")
        # Проверить, что сумма увеличилась на 4
