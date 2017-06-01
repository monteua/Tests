import unittest
from selenium import webdriver
from PageObject.HomePage import HomePage


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://google.com')
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def testSearch(self):
        home = HomePage(self.driver)
        result = home.search('automated testing info')
        assert 'automated' in result.first_link()

