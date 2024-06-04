from pages.base_page import BasePage
from locators import sale_locators as loc
import allure


class SalePage(BasePage):
    PAGE_URL = 'sale.html'

    @allure.step('Check title on the page')
    def check_title_is_(self, text):
        title = self.find(loc.sale_title)
        assert title.text == text

    @allure.step('Checking that the wd button is available')
    def check_wd_button_is_enabled(self):
        button = self.find(loc.shop_wd_button)
        assert button.is_enabled()

    @allure.step('Click the wd button')
    def click_wd_button(self):
        button = self.find(loc.shop_wd_button)
        button.click()

    @allure.step('Check displayed text on the md banner')
    def check_md_banner_text_is_(self, text):
        banner = self.find(loc.md_banner_text)
        assert banner.text == text

    @allure.step('Check displayed text on the lg banner')
    def check_lg_banner_text_is_(self, text):
        banner = self.find(loc.luma_banner_text)
        assert banner.text == text

    @allure.step('Checking link clicks')
    def check_redirect_to_women_sale(self):
        url = self.driver.current_url
        assert url == 'https://magento.softwaretestingboard.com/promotions/women-sale.html'