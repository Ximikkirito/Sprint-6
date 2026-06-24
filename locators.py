from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIE_BUTTON = (
        By.ID,
        'rcc-confirm-button'
    )

    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']"
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Button_Middle') and text()='Заказать']"
    )

    SCOOTER_LOGO = (
        By.XPATH,
        "//a[contains(@class,'Header_LogoScooter')]"
    )

    YANDEX_LOGO = (
        By.XPATH,
        "//a[contains(@class,'Header_LogoYandex')]"
    )

    FAQ_QUESTION_1 = (By.ID, "accordion__heading-24")
    FAQ_ANSWER_1 = (By.ID, "accordion__panel-24")

    FAQ_QUESTION_2 = (By.ID, "accordion__heading-25")
    FAQ_ANSWER_2 = (By.ID, "accordion__panel-25")

    FAQ_QUESTION_3 = (By.ID, "accordion__heading-26")
    FAQ_ANSWER_3 = (By.ID, "accordion__panel-26")

    FAQ_QUESTION_4 = (By.ID, "accordion__heading-27")
    FAQ_ANSWER_4 = (By.ID, "accordion__panel-27")

    FAQ_QUESTION_5 = (By.ID, "accordion__heading-28")
    FAQ_ANSWER_5 = (By.ID, "accordion__panel-28")

    FAQ_QUESTION_6 = (By.ID, "accordion__heading-29")
    FAQ_ANSWER_6 = (By.ID, "accordion__panel-29")

    FAQ_QUESTION_7 = (By.ID, "accordion__heading-30")
    FAQ_ANSWER_7 = (By.ID, "accordion__panel-30")

    FAQ_QUESTION_8 = (By.ID, "accordion__heading-31")
    FAQ_ANSWER_8 = (By.ID, "accordion__panel-31")


class OrderPageLocators:

    NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Адрес')]"
    )

    METRO_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Станция метро']"
    )

    PHONE_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Телефон')]"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    DATE_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Когда привезти')]"
    )

    RENT_DROPDOWN = (
        By.CLASS_NAME,
        "Dropdown-control"
    )

    RENT_OPTION = (
        By.XPATH,
        "//div[text()='трое суток']"
    )

    BLACK_CHECKBOX = (
        By.ID,
        "black"
    )

    GREY_CHECKBOX = (
        By.ID,
        "grey"
    )

    COMMENT_INPUT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать']"
    )

    YES_BUTTON = (
        By.XPATH,
        "//button[text()='Да']"
    )

    SUCCESS_ORDER_MODAL = (
        By.XPATH,
        "//*[contains(text(),'Заказ оформлен')]"
    )


class DzenPageLocators:

    DZEN_URL = "dzen.ru"