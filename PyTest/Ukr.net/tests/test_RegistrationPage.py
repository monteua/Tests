from PageObject.RegistrationPage import RegistrationPage as RP

username_valid = 'testdata466'


# enter the valid email, no issue should occur
def test_enter_valid_username(driver):
    RP(driver).open_page()
    result = RP(driver).fill_mailbox_name(username_valid)
    assert not result
