from selenium.webdriver.common.by import By

class MainPageLocators:
    top_button_order = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    bottom_button_order = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')