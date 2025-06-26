from playwright.sync_api import Page
import allure

"""Базовый класс для всех страниц"""
class BasePage:

    def __init__(self, page: Page):
        self.page = page

    """Переход на страницу"""
    def navigate(self, url):
        with allure.step("Переход на страницу"):
            self.page.goto(url)

    """Клик по иконке корзины"""
    def click_cart(self):
        with allure.step("Клик по иконке корзины"):
            self.page.locator(".cart-link").click()


    """Обновить количество товара в таблице"""
    def change_quantity(self):
        with allure.step("Обновить количество товара в таблице"):
            self.page.locator("#quantity").select_option("4")
