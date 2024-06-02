from pages.base_page import BasePage
from locators import profile_locators as loc

class ProfilePage(BasePage):
    PAGE_URL = 'customer/account/'

    def check_reg_succes(self):
        reg_message = self.find(loc.registration_thank)
        assert reg_message.is_displayed()