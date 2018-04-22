from pages.HomePage import HomePage as Page

# variables
page_title = "My Store"
opened_url = "http://automationpractice.com/index.php"


def test_page_loaded(driver):
    data = Page(driver).open_url
    print("Page title: " + data["title"])
    assert data["title"] == page_title

    print("Current url: " + data["url"])
    assert data["url"] == opened_url
