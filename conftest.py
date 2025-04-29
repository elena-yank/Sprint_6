import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Firefox(options=options)
    yield browser
    if len(browser.window_handles) > 1:
        for handle in browser.window_handles[1:]:
            browser.switch_to.window(handle)
            browser.close()
    if len(browser.window_handles) >= 1:
        browser.switch_to.window(browser.window_handles[0])
    browser.quit()
