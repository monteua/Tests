from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


#page URL
base_url = "CLASSIFIED"
# page locators
page_logo = "logo"
company_moto = "//*[@class='col-xs-8 align-center']//p"
company_name = "//*[@class='col-xs-8 align-center']//h1"
mailing_list = "//*[@class='pointer']//span"
mailing_list_popup = "modal-content"
mailing_list_headline = "myModalLabel"


class FeedbackForm(object):
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(base_url)

    # checking the position of the company logo
    def check_logo(self):
        logo = self.driver.find_element(By.CLASS_NAME, page_logo)
        logo_position = [logo.value_of_css_property("text-align"), logo.value_of_css_property("padding-left")]
        return logo_position

    # checking the css attributes of company moto
    def check_moto(self):
        moto = self.driver.find_element(By.XPATH, company_moto)

        font_size = moto.value_of_css_property("font-size")
        font_name = moto.value_of_css_property("font-family").split(",")[0]
        font_style = moto.value_of_css_property("font-style")
        text_centered = moto.value_of_css_property("text-align")

        return [font_size, font_name, font_style, text_centered]

    # checking the css attributes of company name
    def check_company_name(self):
        name = self.driver.find_element(By.XPATH, company_name)

        font_size = name.value_of_css_property("font-size")
        font_name = name.value_of_css_property("font-family").split(",")[0]
        text_centered = name.value_of_css_property("text-align")

        return [font_size, font_name, text_centered]

    # checking the css attributes of mailing list button
    def check_attr_of_mailing_list(self):
        mailing_list_btn = self.driver.find_element(By.XPATH, mailing_list)

        btn_text = mailing_list_btn.text
        font_size = mailing_list_btn.value_of_css_property("font-size")
        font_name = mailing_list_btn.value_of_css_property("font-family").split(",")[0]

        #move the mouse pointer to see if text turns yellow
        start_color = mailing_list_btn.value_of_css_property("color")
        ActionChains(self.driver).move_to_element(mailing_list_btn).perform()
        color_changed = mailing_list_btn.value_of_css_property("color")

        return [btn_text, font_size, font_name, start_color, color_changed]

    # checking if the Mailing List button opens pop-up
    def check_mailing_list_popup(self):
        mailing_list_btn = self.driver.find_element(By.XPATH, mailing_list)
        mailing_list_btn.click()

        try:
            pop_up = self.driver.find_element(By.CLASS_NAME, mailing_list_popup)
            if pop_up.is_displayed:
                return True
            else:
                return False
        except NoSuchElementException:
            return False


    # checking if the headline in mailing list matches desired one
    def check_mailing_list_headline(self):
        mailing_list_btn = self.driver.find_element(By.XPATH, mailing_list)
        mailing_list_btn.click()

        return self.driver.find_element(By.ID, mailing_list_headline)

    # checking the attributes ofthe mailing list headline
    def check_attr_of_mailing_list_headline(self):
        mailing_list_btn = self.driver.find_element(By.XPATH, mailing_list)
        mailing_list_btn.click()

        headline = self.driver.find_element(By.ID, mailing_list_headline)

        size = headline.value_of_css_property("font-size")
        font_family = headline.value_of_css_property("font-family").split(",")[0]
        is_centered = headline.value_of_css_property("text-align")

        if is_centered == "center":
            return [size, font_family, True]
        return [size, font_family, False]
