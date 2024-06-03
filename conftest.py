from selenium import webdriver
import pytest
from pages.create_account_page import CreateAccPage
from pages.eco_friendly_catalog_page import EFCatalogPage
from pages.sale_page import SalePage
from pages.profile_page import ProfilePage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.close()

@pytest.fixture()
def create_acc_page(driver):
    return CreateAccPage(driver)

@pytest.fixture()
def ef_catalog_page(driver):
    return EFCatalogPage(driver)

@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)

@pytest.fixture()
def profile_page(driver):
    return ProfilePage(driver)