import pytest
import allure
from locators.order_page_locators import OrderPageLocators as o_locs
from locators.main_page_locators import MainPageLocators as m_locs
from test_data.order_page_data import OrderPageData as data
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Доставка самоката")
class TestOrderPage:
    @allure.title("Тест заказа доставки")
    @allure.description(
        "Клик на Заказать -> форма с данными клиента, заполняется данными -> "
        "клик на Далее -> форма с данными аренды -> подтверждение заказа"
    )
    @pytest.mark.parametrize(
        "button_order, user_data, metro_station, rent_data, period, color",
        [
            [
                m_locs.top_button_order,
                data.user_data_1,
                o_locs.metro_station_name_rks,
                data.rent_data_1,
                o_locs.one_day_period,
                o_locs.color_black,
            ],
            [
                m_locs.bottom_button_order,
                data.user_data_2,
                o_locs.metro_station_name_skl,
                data.rent_data_2,
                o_locs.six_day_period,
                o_locs.color_grey,
            ],
        ],
    )
    def test_order_scooter(
        self, driver, button_order, user_data, metro_station, rent_data, period, color
    ):
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
