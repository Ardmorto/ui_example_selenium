from selenium.webdriver.common.by import By

eco_friendly_title = (By.CSS_SELECTOR, '[class="page-title"]')
sort_button = (By.XPATH, '//select[@id="sorter"][1]')
price_sort = (By.XPATH, '//select[@id="sorter"][1]/child::option[@value="price"]')
name_sort = (By.XPATH, '//select[@id="sorter"][1]/child::option[@value="name"]')
position_sort = (By.XPATH, '//select[@id="sorter"][1]/child::option[@value="position"]')
product_list = (By.CSS_SELECTOR, 'ol[class*="products list"]')
first_item = (By.XPATH, '//li[@class="item product product-item"][1]')
one_item = (By.XPATH, '//li[@class="item product product-item"]')
first_item_cart_button = (By.XPATH, '//li[@class="item product product-item"][1]/descendant::button')
sort_switcher_button = (By.XPATH, '//*[@data-role="direction-switcher"][1]')