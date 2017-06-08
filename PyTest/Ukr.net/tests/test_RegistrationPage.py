from PageObject.RegistrationPage import RegistrationPage as RP
from random import randint

username_valid = 'mega_test_data' + str(randint(1000, 100000))
username_valid2 = 'mega_test_data' + str(randint(1000, 100000))
username_valid3 = 'mega_test_data' + str(randint(1000, 100000))
username_valid4 = 'mega_test_data' + str(randint(1000, 100000))
password_valid = 'xQf33Xmp'


# enter the valid email, no issue should occur
def test_enter_valid_username(driver):
    RP(driver).open_page()
    result = RP(driver).fill_mailbox_name(username_valid)
    assert result


# enter the already taken username
def test_enter_taken_username(driver):
    RP(driver).open_page()
    result = RP(driver).fill_mailbox_name("test")
    assert not result


# in order to have access to the password field, first we must enter valid username
# valid username + valid password
def test_enter_val_pass(driver):
    RP(driver).open_page()
    RP(driver).fill_mailbox_name(username_valid2)

    password_result = RP(driver).fill_password_field(password_valid)
    assert password_result


# valid username + valid password + valid password confirmation
def test_enter_val_pass_val_conf(driver):
    RP(driver).open_page()
    RP(driver).fill_mailbox_name(username_valid3)
    RP(driver).fill_password_field(password_valid)

    password_result = RP(driver).fill_confirm_password_field(password_valid)
    assert password_result


# valid username + invalid password
def test_enter_invalid_password(driver):
    RP(driver).open_page()
    RP(driver).fill_mailbox_name(username_valid4)
    field1 = RP(driver).fill_password_field("x")
    assert not field1





