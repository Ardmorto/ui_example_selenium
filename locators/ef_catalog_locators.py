from selenium.webdriver.common.by import By

eco_friendly_title = (By.CSS_SELECTOR, '[class="page-title"]')
sort_button = (By.XPATH, '//select[@id="sorter"][1]')
price_sort = (By.XPATH, '//select[@id="sorter"][1]/child::option[@value="price"]')
name_sort = (By.XPATH, '//select[@id="sorter"][1]/child::option[@value="name"]')
position_sort = (By.XPATH, '//select[@id="sorter"][1]/child::option[@value="position"]')
product_list = (By.CSS_SELECTOR, 'ol[class*="products list"]') #попробовать size()
first_item = (By.XPATH, '//li[@class="item product product-item"][1]')
first_item_cart_button = (By.XPATH, '//li[@class="item product product-item"][1]/descendant::button')