from selenium.webdriver.common.by import By

sale_title = (By.CSS_SELECTOR, 'h1')
shop_wd_button = (By.CSS_SELECTOR, '[class="more button"]')
wd_banner_text = (By.XPATH, '//*[contains(text(), "Pristine")]')
shop_md_link = (By.XPATH, '//*[contains(text(), "Shop Men")]')
md_banner_text = (By.XPATH, '//*[contains(text(), "Men’s Bargains")]')
shop_luma_link = (By.XPATH, '//*[contains(text(), "Shop Luma")]')
luma_banner_text = (By.XPATH, '//*[contains(text(), "Gear Steals")]')