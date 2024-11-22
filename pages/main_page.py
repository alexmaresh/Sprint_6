from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators as locs


class MainPage(BasePage):
    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self, button):
        self.scroll(button)
        self.find_element_delay(button)
        self.click_element_delay(button)

    @staticmethod
    def format_selector(tple, num):
        selector_type, selector_string = tple
        formatted_selector = selector_string.format(num)
        return (selector_type, formatted_selector)

    @allure.step("Получение текста ответа")
    def get_answer_text(self, num):
        formatted_q = self.format_selector(locs.question, num)
        formatted_a = self.format_selector(locs.answer, num)
        self.scroll(formatted_q)
        self.click_element_delay(formatted_q)
        answer = self.find_element_delay(formatted_a).text
        return answer

    @allure.step('Проверка открытия страницы "Самокат"')
    def check_scooter_page(self):
        current_url = self.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Клик на логотип Яндекса")
    def click_logo_yandex(self):
        self.click_element_delay(locs.logo_scooter)

    @allure.step('Переход на страницу "Дзен"')
    def go_to_window(self):
        self.switch_to_window()

    @allure.step('Проверка открытия страницы "Дзен"')
    def check_go_to_dzen(self):
        self.find_element_delay(locs.dzen_news)
        current_url = self.get_current_url()
        assert (
            current_url == "https://dzen.ru/?yredirect=true"
        ), 'Главная страница "Дзен" не открылась'
