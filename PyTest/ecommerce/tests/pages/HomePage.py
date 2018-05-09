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
        "search_button": (By.XPATH, "//*[@class='btn btn-default button-search']"),
        "shopping_card": (By.CLASS_NAME, "shopping_cart")
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

    def is_search_displayed_and_working(self, prompt):
        search_box = self.driver.find_element(*self.locator_dictionary['search_box'])
        search_button = self.driver.find_element(*self.locator_dictionary['search_button'])
        assert search_box.is_displayed()
        print("Search box is found")

        ghost_text = search_box.get_attribute('placeholder')
        assert 'search' in ghost_text.lower()
        print("Ghosted text is present in search bar")

        search_box.send_keys(prompt)
        search_button.click()

        assert 'search' in self.driver.title.lower()
        print("Search page opened")
        assert prompt in self.driver.current_url

    def is_shopping_card_displayed(self):
        shopping_card = self.driver.find_element(*self.locator_dictionary['shopping_card'])
        assert shopping_card.is_displayed()
        print("Shopping card is displayed.")
        assert "Cart (empty)".lower() in shopping_card.text().lower()
        print(shopping_card.text(), "is displayed")

        shopping_card.click()
        assert self.driver.current_url != base_url
        print("After click on shopping cart, shopping cart page was opened")
        print("New url: " + self.driver.current_url)
