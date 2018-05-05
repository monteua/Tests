import pytest
from selenium import webdriver

BROWSER = {'chrome': webdriver.Chrome,
           'edge': webdriver.Edge
           }


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture
def driver(request):
    # @type driver: selenium.webdriver
    browser = request.config.getoption('browser')
    driver = BROWSER[browser]()
    driver.implicitly_wait(20)
    request.addfinalizer(driver.quit)

    return driver


