import allure
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from pages.base_page import BasePage


"""Page Object для главной страницы магазина"""
class HomePage(BasePage):

    # Локаторы
    PRODUCT_CARDS = ".hot-product-card"
    PRODUCT_LINK = ".hot-product-card-img-overlay"


    """Проверить количество товаров на странице"""
    def verify_products_count(self, product_count: int = 9):
        with allure.step("Проверить количество товаров на странице"):
            expect(self.page.locator(self.PRODUCT_CARDS)).to_have_count(product_count)

    """Кликнуть на первый товар"""
    def click_first_product(self):
        with allure.step("Кликнуть на первый товар"):
            self.page.locator(self.PRODUCT_LINK).first.click()

    """Кликнуть на второй товар"""
    def click_second_product(self):
        with allure.step("Кликнуть на второй товар"):
            self.page.locator(self.PRODUCT_LINK).nth(1).click()
            self.page.locator(self.PRODUCT_LINK)

    """Кликнуть на третий товар"""
    def click_third_product(self):
        with allure.step("Кликнуть на третий товар"):
            self.page.locator(self.PRODUCT_LINK).nth(2).click()

    """Кликнуть на четвертый товар"""
    def click_fourth_product(self):
        with allure.step("Кликнуть на четвертый товар"):
            self.page.locator(self.PRODUCT_LINK).nth(3).click()

    """Кликнуть на пятый товар"""
    def click_fifth_product(self):
        with allure.step("Кликнуть на пятый товар"):
            self.page.locator(self.PRODUCT_LINK).nth(4).click()

    """Кликнуть на шестой товар"""
    def click_sixth_product(self):
        with allure.step("Кликнуть на шестой товар"):
            self.page.locator(self.PRODUCT_LINK).nth(5).click()

    """Кликнуть на седьмой товар"""
    def click_seventh_product(self):
        with allure.step("Кликнуть на седьмой товар"):
            self.page.locator(self.PRODUCT_LINK).nth(6).click()

    """Кликнуть на восьмой товар"""
    def click_eighth_product(self):
        with allure.step("Кликнуть на восьмой товар"):
            self.page.locator(self.PRODUCT_LINK).nth(7).click()

    """Кликнуть на девятый товар"""
    def click_ninth_product(self):
        with allure.step("Кликнуть на девятый товар"):
            self.page.locator(self.PRODUCT_LINK).nth(8).click()
