import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()
