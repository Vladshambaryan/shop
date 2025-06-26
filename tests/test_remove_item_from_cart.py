import pytest

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


"""Негативные сценарии для магазина"""
class TestRemoveItemFromCart:

    # Тестовые данные
    cart_is_empty = "Your shopping cart is empty!"

    """Удаление товара из корзины"""
    @pytest.mark.regression
    def test_remove_item_from_cart(self, page, shop_url):
        # Инициализация страниц
        home_page = HomePage(page)
        product_page = ProductPage(page)
        cart_page = CartPage(page)
        # Открываем магазин
        home_page.navigate(shop_url)
        home_page.verify_products_count(9)
        # Добавляем товар
        home_page.click_first_product()
        product_page.add_to_cart()
        product_page.verify_cart_updated("1")
        product_page.click_cart()
        # Реализуйте удаление товара
        cart_page.remove_first_item()
        # идем в корзину
        home_page.click_cart()
        cart_page.verify_empty_cart_message(self.cart_is_empty) # Проверяем, что корзина пуста

