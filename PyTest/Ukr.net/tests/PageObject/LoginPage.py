from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# locators
url = 'https://mail.ukr.net/desktop/login?lang=en'
login_loc = "login"
password_loc = "password"
submit_loc = "//*[@id='login-form']//button"
incorrect_data_loc = 'login__error show'

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(url)

    def enter_data(self, login, password):
        self.driver.find_element(By.ID, login_loc).send_keys(login)
        self.driver.find_element(By.ID, password_loc).send_keys(password)
        self.driver.find_element(By.XPATH, submit_loc).click()
        time.sleep(2)

    def error_displayed(self):
        try:
            text = self.driver.find_element(By.CLASS_NAME, 'login__error').text
            return [True, text]
        except NoSuchElementException:
            return False

