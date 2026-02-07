from config.settings import ROOT_URL
from tests.pages.base_page import BasePage
from pathlib import Path

from tests.utils.locators.locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver, base_url=ROOT_URL):
        super(MainPage, self).__init__(driver, base_url =ROOT_URL)
        #self.base_url = f'{base_url}/index.html'
        path = Path(base_url) / 'index.html'
        self.base_url = path.as_uri()  # например, 'file:///C:/.../index.html'

    def go_to_catalog_page(self):
        self.click_on(MainPageLocators.START_PURCHASE)

    def check_open_page(self):
        actual_url = self.driver.current_url
        assert actual_url == self.base_url

    def check_text_catalog(self):
        catalog_title = self.find_element(MainPageLocators.CATALOG_HEADER)
        assert catalog_title == 'Каталог'

    def check_text_login(self):
        login_title = self.find_element(MainPageLocators.LOGIN_PAGE).text
        assert login_title == 'Войти'