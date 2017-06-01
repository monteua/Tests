class ResultPage(object):

    def __init__(self, driver):
        self.driver = driver

    def first_link(self):
        return self.driver.find_element_by_xpath("//*[@id='rso']//a[1]").text
