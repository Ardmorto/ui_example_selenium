def test_check_title(ef_catalog_page):
    ef_catalog_page.open_page()
    ef_catalog_page.check_title_is_('Eco Friendly')

def test_number_of_displayed_items(ef_catalog_page):
    ef_catalog_page.open_page()
    ef_catalog_page.check_products_count(12)

def test_ascending_price_sorting(ef_catalog_page):
    ef_catalog_page.open_page()
    ef_catalog_page.click_sort_button()
    ef_catalog_page.select_price_sort()
    ef_catalog_page.wait_until_page_load()
    ef_catalog_page.check_ascending_price_sorting()

def test_descending_price_sorting(ef_catalog_page):
    ef_catalog_page.open_page()
    ef_catalog_page.click_sort_button()
    ef_catalog_page.select_price_sort()
    ef_catalog_page.switch_sort_direction()
    ef_catalog_page.wait_until_page_load()
    ef_catalog_page.check_descending_price_sorting()