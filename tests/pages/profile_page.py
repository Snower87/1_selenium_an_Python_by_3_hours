from tests.pages.base_page import  BasePage
from tests.utils.locators.locators import ProfilePageLocators

class ProfilePage(BasePage):
    def get_cart_title_item(self):
        return self.find_element(ProfilePageLocators.CARD_TITLE).text

    def remove_item_from_cart(self):
        self.wait_until_visibility_of_element_located(ProfilePageLocators.TRASH_BY_XPATH)
        self.click_on(ProfilePageLocators.TRASH)

    def get_message_of_empty_cart(self):
        return self.find_element(ProfilePageLocators.EMPTY_CART).text