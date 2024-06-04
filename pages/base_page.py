from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import allure


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com/'
    PAGE_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open the page')
    def open_page(self):
        if self.PAGE_URL:
            self.driver.get(f'{self.BASE_URL}{self.PAGE_URL}')
        else:
            raise NotImplementedError('Unable to open the page')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Waiting until page is load')
    def wait_until_page_load(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
