from selenium.webdriver.common.by import By

from config.settings import ROOT_URL
from pages.base_page import BasePage
from utils.locators.locators import CatalogPageLocators, BasePageLocators

class CatalogPage(BasePage):
    def __init__(self, driver, base_url=ROOT_URL):
        super(CatalogPage, self).__init__(driver, base_url=base_url)
        self.base_url = f'{base_url}/products.html'

    def get_card_title(self):
        return self.find_element(CatalogPageLocators.CARD_TITLE).text

    def add_item_to_cart(self):
        card_footer = self.find_element(CatalogPageLocators.CARD_FOOTER)
        card_footer.find_element(By.CLASS_NAME, 'btn-outline-success').click()

    def go_to_profile_page(self):
        self.click_on(BasePageLocators.NAVBAR)
        self.click_on(BasePageLocators.PROFILE_PAGE)
