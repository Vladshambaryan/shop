import allure
from playwright.sync_api import sync_playwright
from pages.base_page import BasePage
from playwright.sync_api import expect


"""Page Object для страницы товара"""
class ProductPage(BasePage):

    # Локаторы
    PRODUCT_NAME = ".product-wrapper h2"
    PRODUCT_PRICE = ".product-price"
    ADD_TO_CART_BUTTON = 'button:has-text("Add To Cart")'
    RECOMMENDATIONS_TITLE = "h2:has-text('You May Also Like')"
    RECOMMENDATION_ITEMS = ".recommendations .row .col-md-3"
    CART_UPDATE = ".cart-size-circle"


    """Проверить название товара"""
    def verify_product_name(self, product_name):
        with allure.step("Проверить название товара"):
            expect(self.page.locator(self.PRODUCT_NAME)).to_have_text(product_name)

    """Проверить цену товара"""
    def verify_product_price(self, product_price):
        with allure.step("Проверить цену товара"):
            expect(self.page.locator(self.PRODUCT_PRICE)).to_have_text(product_price)

    """Проверить количество рекомендаций"""
    def verify_recommendations_count(self, product_count: int = 4):
        with allure.step("Проверить количество рекомендаций"):
            expect(self.page.locator(self.RECOMMENDATION_ITEMS)).to_have_count(product_count)

    """Добавить товар в корзину"""
    def add_to_cart(self):
        with allure.step("Добавить товар в корзину"):
            self.page.locator(self.ADD_TO_CART_BUTTON).click()

    """Проверить что счетчик корзины обновился"""
    def verify_cart_updated(self, product_count: str = "1"):
        with allure.step("Проверить что счетчик корзины обновился"):
            expect(self.page.locator(self.CART_UPDATE)).to_have_text(product_count)
