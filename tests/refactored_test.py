from time import sleep

import pytest
from selenium.webdriver.common.by import By

from config.settings import BASE_DIR
from pages.catalog_page import CatalogPage
from pages.profile_page import ProfilePage
from tests.pages.main_page import MainPage
from utils.locators.locators import MainPageLocators, BasePageLocators, MenuLocators


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

# (07.02.2026, #1h)
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

# (07.02.2026, #1.5h)
def test_2_check_open_urllink_catalogPage(browser, root_url):
    # 1 Создаем объект main_page, настраиваем браузер
    main_page = MainPage(browser)
    browser.maximize_window()
    # 2 Переходим на url main_page
    main_page.navigate_to()
    # 3 Проверяем, что открыта страница 'index.html'
    main_page.check_open_page()
    # 4 Проверяем, что в главной странице есть текстовая ссылка 'Каталог' вверху
    # Вариант №1 (поиск):
    #main_page.check_text_catalog()
    # Вариант №2 (поиск):
    text_catalog = main_page.find_element(MainPageLocators.CATALOG_HEADER).text
    assert text_catalog == 'Каталог'
    # 5 Проверяем, что в главной странице есть текстовая ссылка 'Войти' вверху
    # Вариант №1
    main_page.check_text_login()
    # Вариант №2
    #text_login = main_page.find_element(MainPageLocators.LOGIN_PAGE).text
    #assert  text_login == 'Войти'
    # 6 Кликаем на dropdown, чтобы появился выпадающий список
    main_page.find_element(BasePageLocators.NAVBAR).click()
    # 7 Проверяем все текстовые пункты меню

    text_profile = main_page.find_element(MenuLocators.PROFILE_PAGE).text
    assert text_profile == 'Профиль'
    text_profile = main_page.find_element(MenuLocators.ORDER_PAGE).text
    assert text_profile == 'Заказы'
    text_profile = main_page.find_element(MenuLocators.ADMIN_PANEL).text
    assert text_profile == 'Админ-панель'
    text_profile = main_page.find_element(MenuLocators.EXIT_ACTION).text
    assert text_profile == 'Выйти'

# (07.02.2026, #10m)
def test_3_chek_following_the_link_catalog(browser, root_url):
    # 1 Открытие главной страницы (/index.html) и настройка браузера
    main_page = MainPage(browser)
    catalog_page = CatalogPage(browser)
    main_page.navigate_to()
    browser.maximize_window()

    # 2 Проверка перехода на страницу каталога после нажатия на кнопку 'Начать покупки'
    main_page.click_on(MainPageLocators.START_PURCHASE)
    sleep(2)
    catalog_page.check_open_page()

    # 3 Имитируем нажатие кнопки <back> (возврат на предыдущую страницу)
    browser.back()

    # 4 Переходим по ссылке вверху справа и проверяем адрес открытой страницы (url-страницы)
    sleep(2)
    main_page.click_on(MainPageLocators.CATALOG_HEADER)
    sleep(2)
    catalog_page.check_open_page()
