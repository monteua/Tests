from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
# locators
url = 'https://oauth.ukr.net/registration?lang=en'

# By.XPATH
mailboxName_loc = '//*[contains(@class, "field-login")]'
password_loc = '//*[contains(@class, "field-password")]'
password_confirm_loc = '//*[contains(@class, "field-password2")]'
# errors locators
name_taken = '//p[@data-lang="login_dropdown_login_error_title"]'
invalid_password_loc = '//div[@data-lang="password_complexity_error"]'
mismatch_password_loc = '//div[@data-lang="password_error"]'


class RegistrationPage(object):

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(url)

    def fill_mailbox_name(self, username):
        # element have a dynamic id and name
        self.driver.find_element(By.XPATH, mailboxName_loc).send_keys(username, Keys.TAB)
        try:
            time.sleep(2)
            error = self.driver.find_element(By.XPATH, name_taken).text
            if "Unfortunately" in error:
                return False
            else:
                return True
        except NoSuchElementException:
            return True

    def fill_password_field(self, password):
        self.driver.find_element(By.XPATH, password_loc).send_keys(password, Keys.TAB)
        try:
            time.sleep(2)
            error = self.driver.find_element(By.XPATH, invalid_password_loc).text
            if len(str(error)) > 2:
                return False
        except NoSuchElementException:
            return True

    def fill_confirm_password_field(self, password):
        self.driver.find_element(By.XPATH, password_confirm_loc).send_keys(password, Keys.TAB)
        try:
            time.sleep(2)
            error = self.driver.find_element(By.XPATH, mismatch_password_loc).text
            if len(str(error)) > 2:
                return False
        except NoSuchElementException:
            return True

