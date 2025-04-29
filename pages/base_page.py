from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_and_click_visible_text(self, xpath_template, value):
        locator = (xpath_template[0], xpath_template[1].format(value))
        self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def switch_to_new_tab(self, timeout=10):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_url_change('about:blank')

    def wait_for_url_change(self, old_url):
        self.wait.until(lambda d: d.current_url != old_url)

    def wait_for_url_contains(self, text):
        self.wait.until(lambda d: text in d.current_url.lower())


    def get_current_url(self):
        return self.wait.until(lambda d: d.current_url)

    def check_url_contains(self, expected_part):
        current_url = self.get_current_url()
        return expected_part in current_url