from selenium import webdriver

# url
base_url = "http://automationpractice.com/"

# locators
header_banner = "//*[@class='img-responsive']"
phone_number = "shop-phone"
contact_us_loc = "contact-link"
sign_in = "header_user_info"


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
            if param in number.lower():
                return True
            return False

    @property
    def is_contact_us_visible_and_clickable(self):
        button = self.driver.find_element_by_id(contact_us_loc).text
        self.driver.find_element_by_id(contact_us_loc).click()
        return dict(button=button, title=self.driver.title, url=self.driver.current_url)

    @property
    def is_sign_in_visible_and_clickable(self):
        button = self.driver.find_element_by_class_name(sign_in).text
        self.driver.find_element_by_class_name(sign_in).click()
        return dict(button_text=button, title=self.driver.title, url=self.driver.current_url)