from selenium.webdriver.common.by import By

create_acc_header_loc = (By.CSS_SELECTOR, 'h1')
name_field = (By.ID, 'firstname')
last_name_field = (By.ID, 'lastname')
email_field = (By.NAME, 'email')
password_field = (By.NAME, 'password')
password_confirm_field = (By.NAME, 'password_confirmation')
create_acc_button = (By.CSS_SELECTOR, '.submit')
name_error = (By.ID, 'firstname-error')
last_name_error = (By.ID, 'lastname-error')
email_error = (By.ID, 'email_address-error')
password_error = (By.ID, 'password-error')
conf_pass_error = (By.ID, 'password-confirmation-error')