from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):

    chrome_options = Options()
    #steam inventory helper
    chrome_options.add_extension(
        'C:/Users/VadymStavskyi/AppData/Local/Google/Chrome/User Data/Default/Extensions/'
        'cmeakgjggjdlcpncigglobpjbkabhmjl/1.10.9.5_0.crx')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver