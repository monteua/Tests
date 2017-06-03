# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

@given('website "{url}"')
def open_page(context, url):
    context.browser.get(url)

