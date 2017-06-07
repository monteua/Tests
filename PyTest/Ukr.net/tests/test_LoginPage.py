from PageObject.LoginPage import LoginPage

login_valid = 'login_valid'
password_valid = 'password_valid'
login_invalid = 'login_invalid'
password_invalid = 'password_invalid'


# valid login and password for registered user
def test_enter_valid_data(driver):
    LoginPage(driver).open_page()
    LoginPage(driver).enter_data(login_valid, password_valid)
    assert (LoginPage(driver).error_displayed()) == False


# valid login and password for unregistered user
def test_enter_invalid_data(driver):
    LoginPage(driver).open_page()
    LoginPage(driver).enter_data(login_invalid, password_invalid)
    error = LoginPage(driver).error_displayed()
    if error[0]:
        assert "Login or password is incorrect." in error[1]


# blank login and data
def test_blank_data(driver):
    LoginPage(driver).open_page()
    LoginPage(driver).enter_data("", "")
    error = LoginPage(driver).error_displayed()
    if error[0]:
        assert "Login or password is incorrect." in error[1]
