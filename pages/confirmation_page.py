import allure

from pages.base_page import BasePage
from playwright.sync_api import expect


"""Page Object для страницы подтверждения заказа"""
class ConfirmationPage(BasePage):

    # Локаторы
    SUCCESS_MESSAGE = "h3:has-text('Your order is complete!')"
    TOTAL_PAID = ".padding-y-24 .text-right"
    CONTINUE_SHOPPING_BUTTON = "a.cymbal-button-primary:has-text('Continue Shopping')"

    """Проверить успешное оформление заказа"""
    def verify_order_complete(self):
        with allure.step("Проверить успешное оформление заказа"):
            expect(self.page.locator(self.SUCCESS_MESSAGE)).to_be_visible()

    """Проверить итоговую сумму"""
    def verify_total_paid(self, product_amount):
        with allure.step("Проверить итоговую сумму"):
            expect(self.page.locator(self.TOTAL_PAID).last).to_have_text(product_amount)

    """Проверить наличие кнопки продолжения покупок"""
    def verify_continue_shopping_button(self):
        with allure.step("Проверить наличие кнопки продолжения покупок"):
            expect(self.page.locator(self.CONTINUE_SHOPPING_BUTTON)).to_be_visible()
            expect(self.page.locator(self.CONTINUE_SHOPPING_BUTTON)).to_be_enabled()

