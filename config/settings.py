from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DRIVER_PATH = r'C:\pythonAQA\cources\1_selenium_an_Python_by_3_hours\WebDriver\chromedriver.exe'
#ROOT_URL = f'{BASE_DIR / "store-template_website" / "index.html"}' # было, стало (см. ниже)
ROOT_URL = f'{BASE_DIR / "store-template_website"}'  # подправили потому что в каждом классе при создании берется своя страница
                                                     # в MainPage: /index.html
                                                     # в CatalogPage: /products.html