from config.settings import ROOT_URL
from tests.pages.base_page import BasePage

from tests.utils.locators.locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver, base_url=ROOT_URL):
        super(MainPage, self).__init__(driver, base_url =ROOT_URL)
        self.base_url = f'{base_url}/index.html'

    def go_to_catalog_page(self):
        self.click_on(MainPageLocators.START_PURCHASE)