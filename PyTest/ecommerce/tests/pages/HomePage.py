from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


# url
base_url = "http://automationpractice.com/"

# locators
header_banner = "//*[@class='img-responsive']"



class HomePage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def open_url(self):
        self.driver.get(base_url)
        return dict(title=self.driver.title, url=self.driver.current_url)

    



