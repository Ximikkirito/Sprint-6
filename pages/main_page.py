import allure

from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Принять cookies')
    def accept_cookie(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_bottom_order_button(self):
        self.scroll_to_element(
            MainPageLocators.BOTTOM_ORDER_BUTTON
        )
        self.click_element(
            MainPageLocators.BOTTOM_ORDER_BUTTON
        )

    @allure.step('Открыть вопрос FAQ')
    def click_question(self, question_locator):
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step('Нажать логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_element(
            MainPageLocators.SCOOTER_LOGO
        )

    @allure.step('Нажать логотип Яндекса')
    def click_yandex_logo(self):
        self.click_element(
            MainPageLocators.YANDEX_LOGO
        )