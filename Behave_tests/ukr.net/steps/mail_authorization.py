# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


@when("website is loaded")
def is_open(context):
    WebDriverWait(context.browser, 120)
    if "ukr.net" in context.browser.title:
        print("Found ukr.net")
    else:
        print("\nFound:", context.browser.title)


@then('enter the credentials into field e-mail: {e_mail} password: {passw}')
def enter_data(context, e_mail, passw):
    time.sleep(2)
    context.browser.find_element(By.ID, 'login').send_keys(e_mail)
    context.browser.find_element(By.ID, 'password').send_keys(passw)

    context.browser.find_element(By.XPATH, '//button').click()
    time.sleep(2)
    assert "Inbox" in context.browser.title
    search = context.browser.find_element(By.CLASS_NAME, 'show-adv-search')
    assert search.text == 'advanced search'
    time.sleep(1)