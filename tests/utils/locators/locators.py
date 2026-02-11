from selenium.webdriver.common.by import By

class BasePageLocators:
    # Константы — обычно пишутся в верхнем регистре
    LOGIN_PAGE= (By.LINK_TEXT, 'Boйти ')
    NAVBAR = (By.ID, 'navbarDropdown')
    #PROFILE_PAGE= (By.LINK_TEXT, 'Профиль') # не работает

class MainPageLocators (BasePageLocators):
    START_PURCHASE = (By.ID, 'start-purchase-link')
    TITLE_STORE_HEADER = (By.CLASS_NAME, 'navbar-brand')
    TITLE_STORE_MAIN = (By.CLASS_NAME, 'mt-5')
    CATALOG_HEADER = (By.PARTIAL_LINK_TEXT, 'Каталог')
    LOGIN_PAGE = (By.XPATH, "//a[@href='users/login.html']")

class MenuLocators (BasePageLocators):
    PROFILE_PAGE = (By.XPATH, "//a[contains(text(),'Профиль')]")
    ORDER_PAGE = (By.XPATH, "//a[contains(text(),'Заказы')]")
    ADMIN_PANEL = (By.XPATH, "//a[contains(text(),'Админ-панель')]")
    EXIT_ACTION = (By.XPATH, "//a[contains(text(),'Выйти')]")

class CatalogPageLocators (BasePageLocators):
    CARD_TITLE =  (By.CLASS_NAME, 'card-title')
    CARD_DESCRIPTION = (By.CLASS_NAME, 'card-title')
    COUNT_PRODUCTS_IN_BASKET = (By.NAME, 'basketID')
    CARD_FOOTER = (By.CLASS_NAME, 'card-footer')
    BUTTON_CREATE_ORDER = (By.XPATH, "//a[contains(@href,'/orders/order-create.html')]")

class ProfilePageLocators(BasePageLocators):
    CARD_TITLE = (By.CLASS_NAME, 'card-title')
    CARD_FOOTER = (By.CLASS_NAME, 'card-footer')
    TRASH = (By.ID, 'trash')
    TRASH_BY_XPATH = (By.XPATH, '//*[@id="trash"]/i')
    EMPTY_CART = (By.TAG_NAME, 'h3')
    INPUT_NAME = (By.ID, 'inputFirstName')
    INPUT_LASTNAME = (By.ID, 'inputLastName')
    LOGIN_USER = (By.ID, 'inputUsername')
    EMAIL_USER = (By.ID, 'inputEmailAddress')
    CREATE_ORDER = (By.XPATH, "//a[contains(@href,'/orders/order-create.html')]")

class CreateOrderPageLocators(BasePageLocators):
    CARD_TITLE = (By.XPATH, "//div[@class='py-5 text-center']")
    BASKET_TITLE = (By.XPATH, "//span[@class='text-primary']")
    INPUT_FIRSTNAME = (By.ID, "firstName")
    INPUT_LASTNAME = (By.ID, "lastName")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_ADDRESS_REAL = (By.ID, "address")
    LIST_PRODUCT = (By.CLASS_NAME, 'list-group mb-3')

class OrdersPageLocators(BasePageLocators):
    TABLE_LOCATOR = (By.XPATH, ".//table[@class='table']")
    TAG_COLUMNS = (By.XPATH, ".//th[@scope='col']")