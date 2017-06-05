from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# locators
url = 'https://oauth.ukr.net/registration?lang=en'

# By.XPATH
mailboxName_loc = '//*[contains(@class, "field-login")]'
name_taken = '//p[1]'




class RegistrationPage(object):

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(url)

    def fill_mailbox_name(self, username):
        # element have a dynamic id and name
        self.driver.find_element(By.XPATH, mailboxName_loc).send_keys(username)

    def mailbox_name_not_taken(self):
        try:
            error = self.driver.find_element(By.XPATH, name_taken).text
            if 'Unfortunately, someone already got that mailbox' in error:
                return False
        except NoSuchElementException:
            return True
