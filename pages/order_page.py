import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators import OrderPageLocators

class OrderPage(BasePage):

```
@allure.step('Заполнить форму Для кого самокат')
def fill_first_step(
        self,
        name,
        surname,
        address,
        metro,
        phone
):
    self.send_keys(
        OrderPageLocators.NAME_INPUT,
        name
    )

    self.send_keys(
        OrderPageLocators.SURNAME_INPUT,
        surname
    )

    self.send_keys(
        OrderPageLocators.ADDRESS_INPUT,
        address
    )

    self.send_keys(
        OrderPageLocators.METRO_INPUT,
        metro
    )

    self.driver.find_element(
        By.XPATH,
        f"//div[contains(text(),'{metro}')]"
    ).click()

    self.send_keys(
        OrderPageLocators.PHONE_INPUT,
        phone
    )

    self.click_element(
        OrderPageLocators.NEXT_BUTTON
    )

@allure.step('Заполнить форму Про аренду')
def fill_second_step(
        self,
        date,
        comment
):
    self.send_keys(
        OrderPageLocators.DATE_INPUT,
        date
    )

    self.click_element(
        OrderPageLocators.RENT_DROPDOWN
    )

    self.click_element(
        OrderPageLocators.RENT_OPTION
    )

    self.click_element(
        OrderPageLocators.BLACK_CHECKBOX
    )

    self.send_keys(
        OrderPageLocators.COMMENT_INPUT,
        comment
    )

@allure.step('Подтвердить оформление заказа')
def create_order(self):
    self.click_element(
        OrderPageLocators.ORDER_BUTTON
    )

    self.click_element(
        OrderPageLocators.YES_BUTTON
    )

@allure.step('Проверить успешное создание заказа')
def order_successful(self):
    return self.wait_visibility(
        OrderPageLocators.SUCCESS_ORDER_MODAL
    ).is_displayed()
```

}
