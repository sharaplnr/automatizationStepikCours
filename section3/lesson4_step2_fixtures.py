from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/'

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print('\nstart browser for test suite..')
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print('\nquit browser for test suite..')
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')