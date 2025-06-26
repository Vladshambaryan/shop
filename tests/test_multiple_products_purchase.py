import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


"""Негативные сценарии для магазина"""
class TestMultipleProductsPurchase:

    # Тестовые данные
    cart_is_empty = "Your shopping cart is empty!"
    continue_shopping_button = "Continue Shopping"
    product_price = "$157.96"


    """Покупка нескольких товаров"""
    @pytest.mark.regression
    def test_multiple_products_purchase(self, page, shop_url):
        # Инициализация страниц
        home_page = HomePage(page)
        product_page = ProductPage(page)
        cart_page = CartPage(page)
        # 1: Открываем главную страницу
        home_page.navigate(shop_url)
        home_page.verify_products_count(9)
        # 1. Добавить первый товар
        home_page.click_first_product()
        product_page.add_to_cart()
        # 2. Вернуться в каталог
        cart_page.click_continue_sopping()
        home_page.verify_products_count(9)
        # 3. Добавить второй товар
        home_page.click_second_product()
        product_page.add_to_cart()
        # 4. Вернуться в каталог
        cart_page.click_continue_sopping()
        home_page.verify_products_count(9)
        # 5. Добавить третий товар
        home_page.click_third_product()
        product_page.add_to_cart()
        cart_page.click_continue_sopping()
        # 6. Перейти в корзину
        cart_page.click_cart()
        # 7. Проверить количество товаров (3)
        cart_page.verify_product_count_in_cart()
        # 8. Проверить общую сумму
        cart_page.verify_total_price(self.product_price)
