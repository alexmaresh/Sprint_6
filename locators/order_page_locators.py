from selenium.webdriver.common.by import By

class OrderPageLocators:
    #Поля раздела формы Для кого самокат
    name_scooter = (By.CLASS_NAME, 'Order_Header__BZXOb')
    input_name = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    input_surname = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    input_address = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    dropdown_metro_station = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    metro_station_name_rks = (By.XPATH, '//div[text()="Бульвар Рокоссовского"]')
    metro_station_name_skl = (By.XPATH, '//div[text()="Сокол"]')
    input_phone = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    button_next = (By.XPATH, '//button[text()="Далее"]')

    #Поля раздела формы Про аренду
    name_form_about_rent = (By.CLASS_NAME, 'Order_Header__BZXOb')
    calendar_rent_date = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    dropdown_rent_period = (By.CLASS_NAME, 'Dropdown-placeholder')
    one_day_period = (By.XPATH, '//div[text() = "сутки"]')
    six_day_period = (By.XPATH, '//div[text() = "шестеро суток"]')
    color_black=(By.ID, 'black')
    color_grey=(By.ID, 'grey')
    input_comment = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')
    button_order = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]')

    # Поля всплывающего окна заказа
    pop_up_order = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    button_yes_order = (By.XPATH, '//button[text()="Да"]')
    button_status = (By.XPATH, '//button[text()="Посмотреть статус"]')
