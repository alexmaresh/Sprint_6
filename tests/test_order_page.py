import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from test_data.order_page_data import OrderPageData
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature('Доставка самоката')

class TestOrderPage:
    @allure.title('Тест заказа доставки')
    @pytest.mark.parametrize(
        'button_order, user_data, metro_station, rent_data, period, color',
        [
            [MainPageLocators.top_button_order, OrderPageData.user_data_1, OrderPageLocators.metro_station_name_rks,
            OrderPageData.rent_data_1, OrderPageLocators.one_day_period, OrderPageLocators.color_black],
            [MainPageLocators.bottom_button_order, OrderPageData.user_data_2, OrderPageLocators.metro_station_name_skl,
             OrderPageData.rent_data_2, OrderPageLocators.six_day_period, OrderPageLocators.color_grey]
        ]
    )
    def test_order_scooter(self, driver, button_order, user_data, metro_station, rent_data,
                            period, color):
        main_page = MainPage(driver)
        main_page.click_order_button(button_order)
        order_page = OrderPage(driver)
        order_page.fill_scooter_form(*user_data, metro_station)
        order_page.click_next_button()
        order_page.fill_rent_form(*rent_data, period, color)
        order_page.click_order_button()
        order_page.waiting_popup()
        order_page.click_yes_button()
        order_page.check_success_window()
