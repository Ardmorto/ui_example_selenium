from pages.base_page import BasePage
from locators import profile_locators as loc
import allure

class ProfilePage(BasePage):
    PAGE_URL = 'customer/account/'

    @allure.step('Check registration message on the page')
    def check_reg_succes(self):
        reg_message = self.find(loc.registration_thank)
        assert reg_message.is_displayed()