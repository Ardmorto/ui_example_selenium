from pages.base_page import BasePage
from locators import sale_locators as loc


class SalePage(BasePage):
    PAGE_URL = 'sale.html'

    def check_title_is_(self, text):
        title = self.find(loc.sale_title)
        assert title.text == text

    def check_wd_button_is_enabled(self):
        button = self.find(loc.shop_wd_button)
        assert button.is_enabled()

    def click_wd_button(self):
        button = self.find(loc.shop_wd_button)
        button.click()

    def check_md_banner_text_is_(self, text):
        banner = self.find(loc.md_banner_text)
        assert banner.text == text

    def check_lg_banner_text_is_(self, text):
        banner = self.find(loc.luma_banner_text)
        assert banner.text == text

    def check_redirect_to_women_sale(self):
        url = self.driver.current_url
        assert url == 'https://magento.softwaretestingboard.com/promotions/women-sale.html'