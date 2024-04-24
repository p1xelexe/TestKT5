from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from random import randint
import time


class BasePage:
    def __init__(self, driver, wait=10):
        self.driver = driver
        self.logger = driver.logger
        self.wait = WebDriverWait(self.driver, wait)
        self.class_name = self.__class__.__name__

    def is_tuple(self, element_locator):
        if isinstance(element_locator, tuple):
            return self.driver.find_element(*element_locator)
        else:
            return self.driver.find_element(element_locator)

    def tab(self):
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        self.logger.info("Press 'TAB'")
        time.sleep(1)
        return self

    def escape(self):
        return ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def enter(self):
        return ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    @staticmethod
    def random(arr):
        return randint(0, len(arr) - 1)

    @staticmethod
    def last(arr):
        return len(arr) - 1

    def click(self, element_locator):
        try:
            element = self.is_tuple(element_locator)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()
        except Exception as e:
            print(f"Error: {e}")

    def write(self, element_locator, value):
        element = self.is_tuple(element_locator)
        element.clear()

        result_text = value[randint(0, len(value) - 1)] if isinstance(value, list) else value

        for letter in result_text:
            time.sleep(0.1)
            element.send_keys(letter)

    def Pinput(self, element, value):
        try:
            self.click(element)
            self.write(element, value)
        except Exception as e:
            print(f"An error occurred: {e}")

    def downArrow(self):
        ActionChains(self.driver).send_keys(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).perform()
        self.logger.info("Press 'Down'")
        time.sleep(0.2)
        return self
