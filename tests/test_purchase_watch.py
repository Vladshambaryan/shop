import pytest

from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage


"""Тесты покупки товара"""
class TestPurchaseFlowWatch:

    # Тестовые данные
    product_name = "Watch"
    product_price = "$109.99"
    total_price = "$118.98"

    """Полный флоу покупки товара"""
    @pytest.mark.regression
    def test_complete_purchase_watch(self, page, shop_url):
        # Инициализация страниц
        home_page = HomePage(page)
        product_page = ProductPage(page)
        cart_page = CartPage(page)
        confirmation_page = ConfirmationPage(page)

        # Шаг 1: Открываем главную страницу
        home_page.navigate(shop_url)
        home_page.verify_products_count(9)
        # Шаг 2: Выбираем второй товар
        home_page.click_third_product()
        # Шаг 3: Проверяем страницу товара
        product_page.verify_product_name(self.product_name)
        product_page.verify_product_price(self.product_price)
        product_page.verify_recommendations_count(4)
        # Шаг 4: Добавляем в корзину
        product_page.add_to_cart()
        product_page.verify_cart_updated("1")
        # Шаг 5: Переходим в корзину
        product_page.click_cart()
        # Шаг 6: Проверяем корзину и оформляем заказ
        cart_page.verify_product_in_cart(self.product_name)
        cart_page.verify_total_price(self.total_price)
        cart_page.place_order()
        # Шаг 7: Проверяем подтверждение заказа
        confirmation_page.verify_order_complete()
        confirmation_page.verify_total_paid(self.total_price)
        confirmation_page.verify_continue_shopping_button()
