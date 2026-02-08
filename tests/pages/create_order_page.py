from pathlib import Path

from config.settings import ROOT_URL
from pages.base_page import BasePage


class CreateOrderPage(BasePage):
    def __init__(self, driver, base_url=ROOT_URL):
        super(CreateOrderPage, self).__init__(driver, base_url=base_url)
        #self.base_url = f'{base_url}/products.html'
        path = Path(base_url) / 'orders/order-create.html'
        self.base_url = path.as_uri()

    def check_open_page(self):
        actual_url = self.driver.current_url
        assert actual_url == self.base_url