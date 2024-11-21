from pages.base_page import BasePage
import pytest
import allure

class MainPage(BasePage):

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self, button):
        self.scroll(button)
        self.find_element_delay(button)
        self.click_element_delay(button)
