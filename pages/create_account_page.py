from pages.base_page import BasePage
from faker import Faker
from locators import create_acc_locators as loc
import allure


class CreateAccPage(BasePage):
    PAGE_URL = 'customer/account/create/'
    fake = Faker(locale='ru_RU')

    @allure.step('Filling the name field')
    def fill_name_field(self):
        field = self.find(loc.name_field)
        field.send_keys(self.fake.first_name())

    @allure.step('Filling the last name field')
    def fill_last_name_field(self):
        field = self.find(loc.last_name_field)
        field.send_keys(self.fake.last_name())

    @allure.step('Filling the emsil field')
    def fill_email_field(self):
        field = self.find(loc.email_field)
        field.send_keys(self.fake.free_email())

    @allure.step('Filling password ans confirmation fields with same password')
    def fill_same_passwords_field(self):
        pass_field = self.find(loc.password_field)
        confirm_field = self.find(loc.password_confirm_field)
        password = self.fake.password()
        pass_field.send_keys(password)
        confirm_field.send_keys(password)

    @allure.step('Filling password and confirmation fields with different passwords')
    def fill_different_passwords(self):
        pass_field = self.find(loc.password_field)
        confirm_field = self.find(loc.password_confirm_field)
        pass_field.send_keys(self.fake.password())
        confirm_field.send_keys(self.fake.password())

    @allure.step('Checking that creating button is enabled')
    def check_button_is_enable(self):
        button = self.find(loc.create_acc_button)
        assert button.is_enabled()

    @allure.step('Click create button')
    def click_create_acc_button(self):
        button = self.find(loc.create_acc_button)
        button.click()

    @allure.step('Check name error')
    def check_name_error_is_(self, text):
        name_error = self.find(loc.name_error)
        assert name_error.is_displayed()
        assert name_error.text == text

    @allure.step('Check last name error')
    def check_last_name_error_is_(self, text):
        last_name_error = self.find(loc.last_name_error)
        assert last_name_error.is_displayed()
        assert last_name_error.text == text

    @allure.step('Check email error')
    def check_email_error_is_(self, text):
        email_error = self.find(loc.email_error)
        assert email_error.is_displayed()
        assert email_error.text == text

    @allure.step('Check password error')
    def check_pass_error_is_(self, text):
        password_error = self.find(loc.password_error)
        assert password_error.is_displayed()
        assert password_error.text == text

    @allure.step('Check confirmation password error')
    def check_conf_pass_error_is_(self, text):
        conf_pass_error = self.find(loc.conf_pass_error)
        assert conf_pass_error.is_displayed()
        assert conf_pass_error.text == text

    @allure.step('Сhecking the title on the page')
    def check_title_is_(self, text):
        title = self.find(loc.create_acc_title)
        assert title.is_displayed()
        assert title.text == text