from PageObject.HomePage import HomePage


def test_search(driver):
    HomePage(driver).open_browser()
    result = HomePage(driver).search('automated testing info')
    assert 'automated' in result.first_link()


def test_search2(driver):
    HomePage(driver).open_browser()
    result = HomePage(driver).search('Google')
    assert 'Google' in result.first_link()

