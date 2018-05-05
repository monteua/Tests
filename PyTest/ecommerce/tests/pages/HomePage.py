from selenium import webdriver
import pytest
# url
base_url = "http://automationpractice.com/"

# locators
header_banner = "//*[@class='img-responsive']"
phone_number = "shop-phone"



class HomePage(object):
    def __init__(self, driver):
        ':type driver: webdriver.Chrome'
        self.driver = driver

    @property
    def open_url(self):
        self.driver.get(base_url)
        return dict(title=self.driver.title, url=self.driver.current_url)

    def is_banner_visible(self):
        banner = self.driver.find_element_by_xpath(header_banner)
        if banner.is_displayed():
            return True
        return False

    def is_header_phone_number_visible(self, param):
        number = self.driver.find_element_by_class_name(phone_number).text
        if number:
            if param in number:
                return True
            return False
