from selenium import webdriver
import pytest


BROWSER = {'chrome': webdriver.Chrome,
           'firefox': webdriver.Firefox,
           'safari': webdriver.Safari
           }


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture
def driver(request):
    browser = request.config.getoption('browser')
    _driver = BROWSER[browser]()
    _driver.implicitly_wait(20)
    request.addfinalizer(_driver.quit)
    return _driver
