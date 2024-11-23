import allure
from locators.main_page_locators import MainPageLocators as locs
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("По клику на логотип переход на страницу")
class TestClickToLogo:
    @allure.title("Переход на Самокат")
    @allure.description("Клик по лого -> переход на главную")
    def test_go_to_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button(locs.top_button_order)
        order_page = OrderPage(driver)
        order_page.click_logo_scooter()
        main_page.check_scooter_page()

    @allure.title("Переход на Дзен")
    @allure.description("Клик по лого -> в новом окне открылась страница Дзен")
    def test_go_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        main_page.switch_to_window()
        main_page.check_go_to_dzen()
