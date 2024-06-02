from pages.base_page import BasePage
from faker import Faker
from locators import create_acc_locators as loc


class CreateAccPage(BasePage):
    PAGE_URL = 'customer/account/create/'
    fake = Faker(locale='ru_RU')

    def fill_name_field(self):
        field = self.find(loc.name_field)
        field.send_keys(self.fake.first_name())

    def fill_last_name_field(self):
        field = self.find(loc.last_name_field)
        field.send_keys(self.fake.last_name())

    def fill_email_field(self):
        field = self.find(loc.email_field)
        field.send_keys(self.fake.free_email())

    def fill_same_passwords_field(self):
        pass_field = self.find(loc.password_field)
        confirm_field = self.find(loc.password_confirm_field)
        password = self.fake.password()
        pass_field.send_keys(password)
        confirm_field.send_keys(password)

    def fill_different_passwords(self):
        pass_field = self.find(loc.password_field)
        confirm_field = self.find(loc.password_confirm_field)
        pass_field.send_keys(self.fake.password())
        confirm_field.send_keys(self.fake.password())

    def check_button_is_enable(self):
        button = self.find(loc.create_acc_button)
        assert button.is_enabled()

    def click_create_acc_button(self):
        button = self.find(loc.create_acc_button)
        button.click()

    def check_name_error_is_(self, text):
        name_error = self.find(loc.name_error)
        assert name_error.is_displayed()
        assert name_error.text == text

    def check_last_name_error_is_(self, text):
        last_name_error = self.find(loc.last_name_error)
        assert last_name_error.is_displayed()
        assert last_name_error.text == text

    def check_email_error_is_(self, text):
        email_error = self.find(loc.email_error)
        assert email_error.is_displayed()
        assert email_error.text == text

    def check_pass_error_is_(self, text):
        password_error = self.find(loc.password_error)
        assert password_error.is_displayed()
        assert password_error.text == text

    def check_conf_pass_error_is_(self, text):
        conf_pass_error = self.find(loc.conf_pass_error)
        assert conf_pass_error.is_displayed()
        assert conf_pass_error.text == text

    def check_title_is_(self, text):
        title = self.find(loc.create_acc_title)
        assert title.is_displayed()
        assert title.text == text