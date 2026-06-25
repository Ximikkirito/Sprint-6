import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    @allure.step('Инициализация страницы')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Нажать на элемент')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Заполнить поле значением: {text}')
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    @allure.step('Дождаться отображения элемента')
    def wait_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(
            self.driver.window_handles[1]
        )