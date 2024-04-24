from PageObjects.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from conf import *
import time


class ProductPage(BasePage):
    MAIN_PICTURE = (By.XPATH, "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]")
    BUTTON_HOME = (By.LINK_TEXT, "Интернет магазин Opencart")
    BUTTON_FAVORITE = (By.XPATH, "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]")
    BUTTON_BUY = (By.CSS_SELECTOR, "#button-cart")
    BUTTON_NEXT_REVIEW = (By.CSS_SELECTOR, "#button-review")
    INPUT_COUNT = (By.CSS_SELECTOR, "#input-quantity")
    BUTTON_DESCRIPTION = (By.LINK_TEXT, "Описание")
    BUTTON_CHARACTERISTICS = (By.LINK_TEXT, "Характеристики")
    BUTTON_REVIEW = (By.PARTIAL_LINK_TEXT, "Отзывов (")
    INPUT_NAME_REVIEW = (By.CSS_SELECTOR, "#input-name")
    INPUT_REVIEW = (By.CSS_SELECTOR, "#input-review")
    SELECT_COLOR = (By.CSS_SELECTOR, "#input-option226")
    SELECT_OPTION_COLOR = (By.XPATH, "//option[contains(text(),'Blue')]")

    BUTTON_REVIEW_MARK = [2, 3, 4, 5, 6]
    BUTTON_REVIEW_MARK = [
        (By.CSS_SELECTOR, review_cs.format(mark))
        for mark in BUTTON_REVIEW_MARK
    ]

    def kaka(self, count: int):
        action_chains = ActionChains(self.driver)

        for _ in range(count):
            action_chains.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
            time.sleep(1)

        time.sleep(1)
