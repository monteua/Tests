from pages.HomePage import HomePage as Page
import pytest
# variables
page_title = "my store"
opened_url = "http://automationpractice.com/index.php"
phone_number_text = "call us now: 0123-456-789"


# Test 1: verify if page fully loads with correct title and desired url opened
def test_page_loaded(driver):
    data = Page(driver).open_url
    print("Page title: " + data["title"])
    assert data["title"].lower() == page_title

    print("Current url: " + data["url"])
    assert data["url"].lower() == opened_url


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


# Test 4: verify availability of Contact us button and if correct page opens after click
def test_contact_us_button(driver):
    Page(driver).open_url
    contact_us = Page(driver).is_contact_us_visible_and_clickable

    assert "contact us" in contact_us["button"].lower()
    print("Contact us button located")
    assert "contact us" in contact_us["title"].lower()
    print("Contact page opened, current url: " + contact_us["url"])


# Test 5: verify availability of Sign In button and page
def test_sign_in_button(driver):
    Page(driver).open_url
    sign_in = Page(driver).is_sign_in_visible_and_clickable

    assert "sign in" in sign_in["button_text"].lower()
    print("Sign In button located")
    assert "login" in sign_in["title"].lower()
    print("Login page opened, current url: " + sign_in["url"])

