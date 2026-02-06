from time import sleep

import pytest

from config.settings import BASE_DIR
from pages.catalog_page import CatalogPage
from pages.profile_page import ProfilePage
from tests.pages.main_page import MainPage
from utils.locators.locators import MainPageLocators


# ---> перенесено в файл conftest.py
#@pytest.fixture()
#def root_url():
#    return f'{BASE_DIR / "store-template_website" / "index.html"}'

@pytest.fixture()
def root_url_after_refactored():
    return f'{BASE_DIR / "store-template_website"}'

def test_browser_are_correct(browser, root_url):
    main_page = MainPage(browser)
    main_page.navigate_to() # сработает navigate_to с base_url + url-"страницы"

    browser.maximize_window()
    browser.get(root_url)

    main_title = main_page.get_title()  # метод из BasePage, который получает текст заголовка страницы
    assert main_title == 'Store'

    main_page.go_to_catalog_page() # метод из MainPage, который ведет на страницу каталога

    catalog_page = CatalogPage(browser)
    catalog_title = catalog_page.get_title()  # метод из BasePage, который получает текст заголовка страницы

    assert catalog_title == 'Store - Каталог'

def test_add_to_cart_and_remove(browser, root_url): # вариант автора
    browser.maximize_window()

    catalog_page = CatalogPage(browser)
    catalog_page.navigate_to()

    card_title = catalog_page.get_title()
    print(card_title)
    catalog_page.add_item_to_cart()
    catalog_page.go_to_profile_page()

    profile_page = ProfilePage(browser)
    added_item_title = profile_page.get_cart_title_item()

    #assert card_title == added_item_title # ---> не работает, тк 'Store - Каталог' != 'Product name'

    #profile_page.remove_item_from_cart() ---> не работает, тк нету локатора с корзиной
    #assert profile_page.get_message_of_empty_cart() == 'Нет добавленных товаров'  ---> не работает, тк нету локатора с корзиной

def test_1_all_about_mainpage(browser, root_url):
    main_page = MainPage(browser)
    catalog_page = CatalogPage(browser)
    main_page.navigate_to() # сработает navigate_to с base_url + url-"страницы"

    browser.maximize_window()
    browser.get(root_url)

    main_title = main_page.get_title()  # метод из BasePage, который получает текст заголовка страницы
    assert main_title == 'Store'

    #1. Проверяем текст 'Store' в header-е страницы
    navbar_title = main_page.find_element(MainPageLocators.TITLE_STORE_HEADER)
    assert navbar_title.text == 'Store'

    # 2. Проверяем текст 'Store' в теле самой страницы
    main_title = main_page.find_element(MainPageLocators.TITLE_STORE_MAIN)
    assert main_title.text == 'Store'

    # 3. Проверяем url открытой страницы main_page
    main_page.check_open_page()

    # 4. Нажимаем на кнопку 'Начать покупки'
    main_page.click_on(MainPageLocators.START_PURCHASE)  # ---> #1 переход на другую страницу: по локатору
    #main_page.go_to_catalog_page()                      # ---> #2 переход на другую страницу: через метод

    sleep(5)