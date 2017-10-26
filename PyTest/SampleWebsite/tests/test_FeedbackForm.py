from Pages.FeedbackForm import FeedbackForm as Browser


# Test 1. verify that company logo is vertically centered and have position 15px from left edge
def test_company_logo(driver):
    Browser(driver).open_page()
    logo_details = Browser(driver).check_logo()
    assert logo_details[0] == 'center'
    assert logo_details[1] == '15px'


# Test 2. verify that company moto have css attributes: 21 px / Arial / italic / centered inside the header
def test_company_moto(driver):
    Browser(driver).open_page()
    moto_details = Browser(driver).check_moto()
    assert moto_details[0] == '21px'
    assert moto_details[1] == 'Arial'
    assert moto_details[2] == 'italic'
    assert moto_details[3] == 'center'


# Test 3. verify that company name have css attributes: 30 px / Arial / centered inside the header
def test_company_name(driver):
    Browser(driver).open_page()
    name_details = Browser(driver).check_company_name()
    assert name_details[0] == '30px'
    assert name_details[1] == 'Arial'
    assert name_details[2] == 'center'


# Test 4. verify that Mailing List link have css attributes: 21 px / Arial / hover over turns the text yellow.
def test_mailing_list_btn(driver):
    Browser(driver).open_page()
    btn = Browser(driver).check_attr_of_mailing_list()
    assert btn[0] == 'Mailing List'
    assert btn[1] == '21px'
    assert btn[2] == 'Arial'
    assert btn[3] == 'rgba(255, 255, 255, 1)'
    assert btn[4] == 'rgba(255, 255, 0, 1)'


# Test 5. verify that clicking on mailing list button brings pop-up
def test_check_mailing_list_popup(driver):
    Browser(driver).open_page()
    assert Browser(driver).check_mailing_list_popup()


# Test 6. verify that Mailing List headline in pop-up equals Sign Up for Out Newsletter
def test_check_mailing_list_headline(driver):
    Browser(driver).open_page()
    assert Browser(driver).check_mailing_list_headline() == "Sign Up for Out Newsletter"


# Test 7. verify the css attributes of Mailing List headline
def test_check_attr_of_mailing_list_headline(driver):
    Browser(driver).open_page()
    attr = Browser(driver).check_attr_of_mailing_list_headline()

    assert attr[0] == "18px"
    assert attr[1] == "Arial"
    assert attr[2]
