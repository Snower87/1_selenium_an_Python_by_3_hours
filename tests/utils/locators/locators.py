from selenium.webdriver.common.by import By

class BasePageLocators:
    # Константы — обычно пишутся в верхнем регистре
    LOGIN_PAGE= (By.LINK_TEXT, 'Boйти')
    NAVBAR = (By.ID, 'navbarDropdown')
    PROFILE_PAGE= (By.LINK_TEXT, 'Профиль')

class MainPageLocators (BasePageLocators):
    START_PURCHASE = (By.ID, 'start-purchase-link')
    TITLE_STORE_HEADER = (By.CLASS_NAME, 'navbar-brand')
    TITLE_STORE_MAIN = (By.CLASS_NAME, 'mt-5')

class CatalogPageLocators (BasePageLocators):
    CARD_TITLE =  (By.CLASS_NAME, 'card-title')
    CARD_FOOTER = (By.CLASS_NAME, 'card-footer')

class ProfilePageLocators(BasePageLocators):
    CARD_TITLE = (By.CLASS_NAME, 'card-title')
    TRASH = (By.ID, 'trash')
    TRASH_BY_XPATH = (By.XPATH, '//*[@id="trash"]/i')
    EMPTY_CART = (By.TAG_NAME, 'h3')