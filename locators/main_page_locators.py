from selenium.webdriver.common.by import By


class MainPageLocators:
    top_button_order = (
        By.XPATH,
        '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]',
    )
    bottom_button_order = (
        By.XPATH,
        '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]',
    )

    question = (By.ID, "accordion__heading-{}")
    answer = (By.XPATH, "//div[@id='accordion__panel-{}']/p")

    logo_scooter = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    logo_dzen = (By.CLASS_NAME, "desktop-base-header__logo-tA")

    dzen_news = (
        By.XPATH,
        '//div[@data-testid="floor-title-text" and text()="Новости"]',
    )
