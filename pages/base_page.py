from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com/'
    PAGE_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.PAGE_URL:
            self.driver.get(f'{self.BASE_URL}{self.PAGE_URL}')
        else:
            raise NotImplementedError('Unable to open the page')