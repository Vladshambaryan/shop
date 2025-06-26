import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage


"""Негативные сценарии для магазина"""
class TestCannotCheckoutEmptyCart:

    # Тестовые данные
    cart_is_empty = "Your shopping cart is empty!"
    continue_shopping_button = "Continue Shopping"

    """Нельзя оформить заказ с пустой корзиной"""
    @pytest.mark.regression
    def test_cannot_checkout_empty_cart(self, page, shop_url):
        # Инициализация страниц
        home_page = HomePage(page)
        cart_page = CartPage(page)
        # Открываем магазин
        home_page.navigate(shop_url)
        home_page.verify_products_count(9)
        # идем в корзину (без добавления товаров)
        home_page.click_cart()
        cart_page.verify_empty_cart_message(self.cart_is_empty) # Проверяем, что корзина пуста
        cart_page.verify_no_checkout_button() # Проверяем, что нет кнопки оформления заказа
