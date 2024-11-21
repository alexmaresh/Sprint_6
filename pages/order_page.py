import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Появление формы "Для кого самокат"')
    def waiting_scooter_form(self):
        self.find_element_delay(OrderPageLocators.name_scooter)

    @allure.step('Заполнение формы: поле "Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.input_name, name)

    @allure.step('Заполнение формы: поле "Фамилия"')
    def set_surname(self, surname):
        self.send_keys(OrderPageLocators.input_surname, surname)

    @allure.step('Заполнение формы: поле "Адрес"')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.input_address, address)

    @allure.step('Выбор станции метро в дропдауне')
    def select_metro_station(self, metro_station):
        self.click_element_delay(OrderPageLocators.dropdown_metro_station)
        self.scroll(metro_station)
        self.find_element_delay(metro_station)
        self.click_element_delay(metro_station)

    @allure.step('Заполнение формы: поле "Телефон"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.input_phone, phone)

    @allure.step('Заполнение формы "Для кого самокат" целиком')
    def fill_scooter_form(self, name, surname, address, phone, metro_station):
        self.waiting_scooter_form()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.select_metro_station(metro_station)
        self.set_phone(phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_element_delay(OrderPageLocators.button_next)

    @allure.step('Появление формы "Про аренду"')
    def waiting_rent_form(self):
        self.find_element_delay(OrderPageLocators.name_form_about_rent)

    @allure.step('Заполнение формы: поле "Дата"')
    def set_date(self, date):
        self.send_keys(OrderPageLocators.calendar_rent_date, date)
        self.send_keys(OrderPageLocators.calendar_rent_date, Keys.ENTER)

    @allure.step('Заполнение формы: выбор срока аренды')
    def set_rent_period(self, rent_period):
        self.click_element_delay(OrderPageLocators.dropdown_rent_period)
        self.click_element_delay(rent_period)

    @allure.step('Заполнение формы: выбор цвета самоката')
    def set_color(self, color):
        self.click_element_delay(color)

    @allure.step('Заполнение формы: комментарий для курьера')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.input_comment, comment)

    @allure.step('Заполнение формы "Про аренду" целиком')
    def fill_rent_form(self, date, comment, rent_period, color):
        self.waiting_rent_form()
        self.set_date(date)
        self.set_rent_period(rent_period)
        self.set_color(color)
        self.set_comment(comment)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.click_element_delay(OrderPageLocators.button_order)

    @allure.step('Появление попапа "Хотите оформить заказ?"')
    def waiting_popup(self):
        self.find_element_delay(OrderPageLocators.pop_up_order)

    @allure.step('Клик на кнопку "Да" в попапе')
    def click_yes_button(self):
        self.click_element_delay(OrderPageLocators.button_yes_order)

    @allure.step('Проверка появления окна с кнопкой "Посмотреть статус"')
    def check_success_window(self):
        success_window = self.find_element_delay(OrderPageLocators.button_status)
        assert success_window, 'Окно с кнопкой "Посмотреть статус" не появилось'





