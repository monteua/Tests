from PageObject.SteamActions import SteamHome
from accounts import accounts

accounts_list = accounts()


def test_send_trade(driver):
    for login in accounts_list:
        if login == 'monte_ua13':
            password = ""
        else:
            password = ""

        SteamHome(driver).open_browser()
        SteamHome(driver).enter_credentials(login, password)
        SteamHome(driver).pass_steam_guard()
        SteamHome(driver).open_trade_url()
        SteamHome(driver).log_off()
