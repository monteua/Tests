from selenium.webdriver.common.keys import Keys
from PageObject.ResultPage import ResultPage


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def search(self, param1):
        self.driver.find_element_by_id("lst-ib").send_keys(param1, Keys.ENTER)
        return ResultPage(self.driver)
