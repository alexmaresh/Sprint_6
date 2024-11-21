from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5

    def find_element_delay(self, locator):
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element_delay(self, locator):
        WebDriverWait(self.driver,self.timeout).until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, keys):
        self.find_element_delay(locator).send_keys(keys)

    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
