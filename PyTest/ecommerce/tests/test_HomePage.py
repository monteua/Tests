from pages.HomePage import HomePage as Page
import pytest
# variables
page_title = "My Store"
opened_url = "http://automationpractice.com/index.php"
phone_number_text = "Call us now: 0123-456-789"


# Test 1: verify if page fully loads with correct title and desired url opened
def test_page_loaded(driver):
    data = Page(driver).open_url
    print("Page title: " + data["title"])
    assert data["title"] == page_title

    print("Current url: " + data["url"])
    assert data["url"] == opened_url


# Test 2: verify that sale banner in header is displayed
def test_banner_displayed(driver):
    Page(driver).open_url
    banner = Page(driver).is_banner_visible
    assert banner
    print("Banner is visible")


# Test 3: verify that phone number displayed in header menu
@pytest.mark.parametrize('param', [phone_number_text])
def test_phone_number_in_header(driver, param):
    Page(driver).open_url
    phone_number = Page(driver).is_header_phone_number_visible(param)
    assert phone_number
    print("Phone number displayed correctly")


