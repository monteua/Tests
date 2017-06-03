# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

@given('website "{url}"')
def open_page(context, url):
    context.browser.get(url)


@when("website is open")
def is_open(context):
    WebDriverWait(context.browser, 120)
    assert context.browser.title == "Google"

@then('enter the "{text}" into search box')
def enter_text(context, text):

    context.browser.find_element(By.ID, 'lst-ib').send_keys(text)
    time.sleep(3)
    context.browser.find_element(By.ID, "_fZl").click()
