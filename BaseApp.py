from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://yandex.ru/"

    def find_element(self, locator,time=10):
        try:
            return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")
        except NoSuchElementException:
            return False

    def find_elements(self, locator,time=10):
        try:
            return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")
        except NoSuchElementException:
            return False

    def go_to_site(self):
        return self.driver.get(self.url)