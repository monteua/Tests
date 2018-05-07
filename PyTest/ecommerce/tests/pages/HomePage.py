from selenium import webdriver
from selenium.webdriver.common.by import By

# url
base_url = "http://automationpractice.com/"

class HomePage(object):
    def __init__(self, driver):
        ':type driver: webdriver.Chrome'
        self.driver = driver

    locator_dictionary = {
        "header_banner": (By.XPATH, "//*[@class='img-responsive']"),
        "phone_number": (By.CLASS_NAME, "shop-phone"),
        "contact_us_loc": (By.ID, "contact-link"),
        "sign_in": (By.CLASS_NAME, "header_user_info"),
        "header_logo": (By.XPATH, "//*[@id='header_logo']"),
        "header_logo_link": (By.XPATH, "//*[@id='header_logo']/a"),
        "search_box": (By.ID, "search_query_top"),
        "search_button": (By.XPATH, "//*[@class='btn btn-default button-search']")
    }

    @property
    def open_url(self):
        self.driver.get(base_url)
        return dict(title=self.driver.title, url=self.driver.current_url)

    def is_banner_visible(self):
        banner = self.driver.find_element(*self.locator_dictionary['header_banner'])
        if banner.is_displayed():
            return True
        return False

    def is_header_phone_number_visible(self, param):
        number = self.driver.find_element(*self.locator_dictionary['phone_number'])
        number = number.text
        if number:
            if param in number.lower():
                return True
            return False

    @property
    def is_contact_us_visible_and_clickable(self):
        button = self.driver.find_element(*self.locator_dictionary['contact_us_loc']).text
        self.driver.find_element(*self.locator_dictionary['contact_us_loc']).click()
        return dict(button=button, title=self.driver.title, url=self.driver.current_url)

    @property
    def is_sign_in_visible_and_clickable(self):
        button = self.driver.find_element(*self.locator_dictionary['sign_in']).text
        self.driver.find_element(*self.locator_dictionary['sign_in']).click()
        return dict(button_text=button, title=self.driver.title, url=self.driver.current_url)

    @property
    def is_logo_displayed_and_links_to_homepage(self):
        logo = self.driver.find_element(*self.locator_dictionary['header_logo'])
        logo_displayed = logo.is_displayed()
        logo_link = self.driver.find_element(*self.locator_dictionary['header_logo_link']).get_attribute('href')
        logo.click()
        return dict(logo_visible=logo_displayed, logo_link=logo_link, current_url=self.driver.current_url)

    @property
    def is_search_displayed_and_working(self, prompt):
        search_box = self.driver.find_element(*self.locator_dictionary['search_box'])
        search_button = self.driver.find_element(*self.locator_dictionary['seach_button'])
        ghost_text = search_box.get_attribute('placeholder')

        search_box.send_keys(prompt)
        search_button.click()

        return dict(search_box_visible=search_box.is_displayed(), ghost_text=ghost_text,
                    title=self.driver.title, current_url=self.driver.current_url)
