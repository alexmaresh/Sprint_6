import pytest
from selenium import webdriver
from settings import TestSettings


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(TestSettings.base_url)
    yield driver
    driver.quit()
