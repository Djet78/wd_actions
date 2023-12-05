from typing import Self, Union

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BaseComp:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_el(self, xpath: str, timeout: int = 1, _all=False, message: str = '') -> Union[WebElement, list[WebElement]]:
        if not _all:
            return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(By.XPATH, xpath), message=message)
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(By.XPATH, xpath), message=message)

    def is_visible(self, xpath: str, timeout: int = 1) -> bool:
        el = self.find_el(xpath, timeout)
        return el.is_displayed()

    def click(self, xpath: str, timeout: int = 1) -> Self:
        el = self.find_el(xpath, timeout)
        el.click()
        return self

    def input_text(self, xpath: str, text: str, timeout: int = 1) -> Self:
        el = self.find_el(xpath, timeout)
        el.send_keys(text)
        return self

    def get_text(self, xpath: str, timeout: int = 1) -> str:
        el = self.find_el(xpath, timeout)
        return el.get_attribute('value')

    def clear_text(self, xpath: str, timeout: int = 1) -> Self:
        el = self.find_el(xpath, timeout)
        el.clear()
        return self

    def wd_scroll_to(self, xpath) -> Self:
        el = self.find_el(xpath, 1)
        ActionChains(self.driver).move_to_element(el).perform()
        return self

    def js_scroll_to(self, xpath) -> Self:
        self.driver.execute_script(f"""
            let el = document.evaluate('{xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            el.scrollIntoView();
        """)
        return self
