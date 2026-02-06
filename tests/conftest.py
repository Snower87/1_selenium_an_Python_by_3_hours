
import json
import pytest

from selenium import webdriver

from config.settings import BASE_DIR

@pytest.fixture()
def root_url():
    return f'{BASE_DIR / "store-template_website" / "index.html"}'

def get_config_file_path():
    return BASE_DIR / 'config' / 'test_config.json'

@pytest.fixture()
def config(scope='session'):
    with open(get_config_file_path()) as config_file:
        config = json.load(config_file)
    return config

def set_options(opts, config):
    if 'mode' in config:
        if config['mode'] == 'Headless':
            opts.add_argument('--headless= new')

@pytest.fixture()
def browser(config):
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        set_options(opts, config)
        driver = webdriver.Chrome(options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        set_options(opts, config)
        driver = webdriver.Firefox(options=opts)
    else:
        raise Exception('ERR: Unknown browser type.')

    yield driver

    driver.quit()
