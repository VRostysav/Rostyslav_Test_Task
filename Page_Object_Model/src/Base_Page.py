import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 7

    def wait_end_get_element_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element_text = element.text
        return element_text

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout). \
                until(EC.visibility_of_element_located(locator)).click()
        except StaleElementReferenceException:
            time.sleep(3)
            WebDriverWait(self.driver, timeout). \
                until(EC.visibility_of_element_located(locator)).click()

    def scroll_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()

    def move_to_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()



