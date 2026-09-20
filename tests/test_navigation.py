import allure

from data import URL
from pages.main_page import MainPage


class TestNavigation:

    @allure.title(
        'Переход на главную страницу по логотипу Самокат'
    )
    def test_scooter_logo_redirect(
            self,
            driver
    ):
        page = MainPage(driver)

        page.accept_cookie()

        page.click_top_order_button()

        page.click_scooter_logo()

        assert driver.current_url == URL

    @allure.title(
        'Переход на Дзен по логотипу Яндекс'
    )
    def test_yandex_logo_redirect(
            self,
            driver
    ):
        page = MainPage(driver)

        page.accept_cookie()

        page.click_yandex_logo()

        page.switch_to_new_tab()

        assert 'dzen' in driver.current_url