import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA


class TestOrder:

    @allure.title(
        'Оформление заказа через верхнюю кнопку'
    )
    @pytest.mark.parametrize(
        'name,surname,address,metro,phone,date,comment',
        ORDER_DATA
    )
    def test_order_from_top_button(
            self,
            driver,
            name,
            surname,
            address,
            metro,
            phone,
            date,
            comment
    ):
        main_page = MainPage(driver)

        main_page.accept_cookie()
        main_page.click_top_order_button()

        order_page = OrderPage(driver)

        order_page.fill_first_step(
            name,
            surname,
            address,
            metro,
            phone
        )

        order_page.fill_second_step(
            date,
            comment
        )

        order_page.create_order()

        assert order_page.order_successful()

    @allure.title(
        'Оформление заказа через нижнюю кнопку'
    )
    @pytest.mark.parametrize(
        'name,surname,address,metro,phone,date,comment',
        ORDER_DATA
    )
    def test_order_from_bottom_button(
            self,
            driver,
            name,
            surname,
            address,
            metro,
            phone,
            date,
            comment
    ):
        main_page = MainPage(driver)

        main_page.accept_cookie()
        main_page.click_bottom_order_button()

        order_page = OrderPage(driver)

        order_page.fill_first_step(
            name,
            surname,
            address,
            metro,
            phone
        )

        order_page.fill_second_step(
            date,
            comment
        )

        order_page.create_order()

        assert order_page.order_successful()