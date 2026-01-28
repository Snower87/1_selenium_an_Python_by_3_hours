import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from config.settings import DRIVER_PATH, BASE_DIR

@pytest.fixture()
def root_url():
    return f'{BASE_DIR / "store-template_website" / "index.html"}'

@pytest.fixture(scope="function")
def browser():
    # создание объекта WebDriver
    driver = webdriver.Chrome()
    yield driver
    # освобождение ресурсов
    driver.quit()

def test_browser_are_correct(browser, root_url):
    #service = Service(executable_path=DRIVER_PATH) # можно убрать
    #browser = webdriver.Chrome(service=service)
    browser.maximize_window()

    time.sleep(2)
    browser.get(root_url)

    # 1. Проверяет название на главной странице
    time.sleep(2)
    main_title = browser.find_element(By.CLASS_NAME, 'navbar-brand')
    assert main_title.text == 'Store'

    # 2. Переходим на страницу "Начать покупки"
    time.sleep(2)
    purchase_link = browser.find_element(By.ID, 'start-purchase-link')
    purchase_link.click()

    # 3. Проверяет название после перехода в магазин
    time.sleep(2)
    product_title = browser.find_element(By.CLASS_NAME, 'my-4')
    assert product_title.text == 'Store'

    # освобождение ресурсов
    browser.quit()

def test_add_and_empty_basket(browser, root_url): # мой вариант
    # Настройки, запуск браузера
    # 1. Выставляет размер браузера в полный экран
    browser.maximize_window()
    # 2. Переходим, открываем страницу
    browser.get(root_url)

    # 1. Пользователь переходит на главную страницу с каталогом с товарами. Нажимая кнопку "Покупки"
    time.sleep(2)
    btn_start_purchase = browser.find_element(By.ID, 'start-purchase-btn')
    btn_start_purchase.click()

    # 2. Добавляет товар в корзину первый товар из каталога
    time.sleep(2)
    # Ищу все теги перед добавление в корзину
    """
    <div class="card-body">
             <h4 class="card-title">
                  <a href="#">Худи черного цвета с монограммами adidas Originals</a>
             </h4>
             <h5>6 090,00 руб.</h5>
             <p class="card-text">Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.</p>
    </div>
    """
    # 2.1) ищем блок по имени класса "card-body"
    card_body = browser.find_element(By.CLASS_NAME, 'card-body')
    # 2.2) собираем нужные элементы внутри блока
    title = card_body.find_element(By.TAG_NAME, "h4").text
    assert title == "Худи черного цвета с монограммами adidas Originals"
    link_text = card_body.find_element(By.TAG_NAME, "a").text
    assert  link_text == "Худи черного цвета с монограммами adidas Originals"
    price = card_body.find_element(By.TAG_NAME, "h5").text
    assert price == "6 090,00 руб."
    description = card_body.find_element(By.CLASS_NAME, "card-text").text
    assert  description == "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни."

    # 3. Добавить в корзину. Нажав на кнопку "Отправить корзину"
    time.sleep(2)
    first_btn_add_to_cart = browser.find_element(By.CLASS_NAME, "btn-outline-success")
    first_btn_add_to_cart.click()

    # 3. Переходим в корзину
    time.sleep(2)
    # 3.1) Получаем тогл выпадающей стрелки
    dropdown_menu = browser.find_element(By.CLASS_NAME, "dropdown-toggle")
    dropdown_menu.click()
    # 3.2) Получаем список строк выпадающего меню
    dropdown_menu_show = browser.find_element(By.CLASS_NAME, "dropdown-menu")
    items_dropdown_menu_show = dropdown_menu_show.find_elements(By.TAG_NAME, "li")
    # 3.3) Проверяет первый элемент меню: "Профиль"
    assert items_dropdown_menu_show[0].text == "Профиль"
    # и переходим в него
    items_dropdown_menu_show[0].click()

    # 4. Очищает корзину, но кнопки такой нету )
    #browser.find_element(By.CLASS_NAME, 'fa-trash').click()
    #message = browser.find_element(By.TAG_NAME, "h3").text
    #assert message == "Нет добавленных товаров"
    time.sleep(2)

