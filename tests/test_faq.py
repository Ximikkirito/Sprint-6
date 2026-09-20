import pytest
import allure

from pages.main_page import MainPage
from data import FAQ_DATA


class TestFAQ:

    @allure.title('Проверка текста ответа в FAQ')
    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_text',
        FAQ_DATA
    )
    def test_faq_answers(
            self,
            driver,
            question_locator,
            answer_locator,
            expected_text
    ):
        page = MainPage(driver)

        page.accept_cookie()

        page.click_question(question_locator)

        actual_text = page.get_answer_text(
            answer_locator
        )

        assert expected_text in actual_text