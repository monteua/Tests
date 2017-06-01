from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SteamHome(object):

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):
        self.driver.get("https://steamcommunity.com/login/home/?goto=")

    def enter_credentials(self, login, password):
        self.driver.find_element_by_id("steamAccountName").send_keys(login)
        self.driver.find_element_by_id("steamPassword").send_keys(password, Keys.ENTER)

    def pass_steam_guard(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of(self.driver.find_element_by_id("blotter_statuspost_textarea")))

    def open_trade_url(self):
        self.driver.get("https://steamcommunity.com/tradeoffer/new/?partner=81735615&token=lhNyIIkQ")
        time.sleep(2)
        self.driver.execute_script("javascript: TradePageSelectInventory(UserYou, 753, 0);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(20)

    def log_off(self):
        self.driver.execute_script("javascript: Logout();")