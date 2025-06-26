import allure
from playwright.sync_api import sync_playwright
from pages.base_page import BasePage
from playwright.sync_api import expect


"""Page Object для страницы корзины"""
class CartPage(BasePage):

    # Локаторы
    CART_TITLE = "h3:has-text('Cart')"
    PRODUCT_NAME = ".cart-summary-item-row h4"
    TOTAL_PRICE = ".cart-summary-total-row .text-right"
    PLACE_ORDER_BUTTON = "button:has-text('Place Order')"
    CART_IS_EMPTY = "h3"
    CART = ".logo"
    CONTINUE_SHOPPING = ".cymbal-button-primary"
    REMOVE = ".cymbal-button-secondary"
    QUANTITY = ".col"
    PRODUCT_IN_CART = ".cart-size-circle"


    """Проверить что товар в корзине"""
    def verify_product_in_cart(self, product_name):
        with allure.step("Проверить что товар в корзине"):
            expect(self.page.locator(self.PRODUCT_NAME)).to_have_text(product_name)

    """Проверить итоговую сумму"""
    def verify_total_price(self, product_price):
        with allure.step("Проверить итоговую сумму"):
            expect(self.page.locator(self.TOTAL_PRICE)).to_have_text(product_price)

    """Оформить заказ"""
    def place_order(self):
        with allure.step("Оформить заказ"):
            self.page.locator(self.PLACE_ORDER_BUTTON).click()

    """Проверить что корзина пуста"""
    def verify_empty_cart_message(self, cart_is_empty):
        with allure.step("Проверить что корзина пуста"):
            expect(self.page.locator(self.CART)).to_be_visible()
            expect(self.page.locator(self.CART_IS_EMPTY)).to_have_text(cart_is_empty)

    """Проверяем, что кнопки Place Order нет на странице"""
    def verify_no_checkout_button(self):
        with allure.step("Проверяем, что кнопки Place Order нет на странице"):
            expect(self.page.locator(self.PLACE_ORDER_BUTTON)).not_to_be_visible()
            expect(self.page.locator(self.CONTINUE_SHOPPING)).to_be_visible()

    """Проверить количество товара в корзине"""
    def verify_text_product_count_in_cart(self, product_count: str = "Quantity: 3"):
        with allure.step("Проверить количество товара в корзине"):
            locator = self.page.locator(self.QUANTITY).nth(2)
            expect(locator).to_be_visible()
            expect(locator).to_have_text(product_count)

    """Удаление товара"""
    def remove_first_item(self):
        with allure.step("Удаление товара"):
            self.page.locator(self.REMOVE).click()

    """Клик продолжить покупки"""
    def click_continue_sopping(self):
        with allure.step("Клик продолжить покупки"):
            self.page.locator(self.CONTINUE_SHOPPING).first.click()

    """Проверка количества товара"""
    def verify_product_count_in_cart(self, product_count: str = "3"):
        with allure.step("Проверка количества товара"):
            expect(self.page.locator(self.PRODUCT_IN_CART)).to_have_text(product_count)

