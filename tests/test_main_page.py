import allure
import pytest
from test_data.main_page_data import MainPageData as data
from pages.main_page import MainPage


@allure.feature("FAQ")
class TestMainPageFAQ:
    @allure.title("Тест вопросов и ответов в разделе «Вопросы о важном»")
    @allure.description("Клик по вопросу -> открывается ответ")
    @pytest.mark.parametrize(
        "num, expected_text",
        [
            (0, data.answer_cost),
            (1, data.answer_more_scooters),
            (2, data.answer_rent_time),
            (3, data.answer_today),
            (4, data.answer_changes),
            (5, data.answer_charger),
            (6, data.answer_cancel),
            (7, data.answer_mkad),
        ],
    )
    def test_faq(self, driver, num, expected_text):
        main_page = MainPage(driver)
        answer_text = main_page.get_answer_text(num)
        assert answer_text == expected_text
