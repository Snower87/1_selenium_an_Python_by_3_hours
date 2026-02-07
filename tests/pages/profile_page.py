from pathlib import Path

from config.settings import ROOT_URL
from tests.pages.base_page import  BasePage
from tests.utils.locators.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def __init__(self, driver, base_url=ROOT_URL):
        super(ProfilePage, self).__init__(driver, base_url =ROOT_URL)
        #self.base_url = f'{base_url}/index.html'
        path = Path(base_url) / 'users/profile.html' # users/profile.html
        self.base_url = path.as_uri()  # например, 'file:///C:/.../profile.html'

    def check_open_page(self):
        active_url = self.driver.current_url
        assert active_url == self.base_url

    def get_cart_title_item(self):
        return self.find_element(ProfilePageLocators.CARD_TITLE).text

    def remove_item_from_cart(self):
        self.wait_until_visibility_of_element_located(ProfilePageLocators.TRASH_BY_XPATH)
        self.click_on(ProfilePageLocators.TRASH)

    def get_message_of_empty_cart(self):
        return self.find_element(ProfilePageLocators.EMPTY_CART).text