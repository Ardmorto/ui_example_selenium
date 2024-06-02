from selenium.webdriver.common.by import By

create_acc_title = (By.CSS_SELECTOR, '.page-title')
name_field = (By.ID, 'firstname')
last_name_field = (By.ID, 'lastname')
email_field = (By.ID, 'email_address')
password_field = (By.ID, 'password')
password_confirm_field = (By.ID, 'password-confirmation')
create_acc_button = (By.CSS_SELECTOR, 'button[title="Create an Account"]')
name_error = (By.ID, 'firstname-error')
last_name_error = (By.ID, 'lastname-error')
email_error = (By.ID, 'email_address-error')
password_error = (By.ID, 'password-error')
conf_pass_error = (By.ID, 'password-confirmation-error')