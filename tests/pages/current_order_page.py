from pathlib import Path

from config.settings import ROOT_URL
from pages.base_page import BasePage


class CurrentOrderPage(BasePage):
    def __init__(self, driver, base_url=ROOT_URL):
        super(CurrentOrderPage, self).__init__(driver, base_url=base_url)
        path = Path(base_url) / 'orders/order.html'
        self.base_url = path.as_uri()  # например, 'file:///C:/.../orders/order.html'

    def check_open_page(self):
        actual_url = self.driver.current_url
        assert actual_url == self.base_url