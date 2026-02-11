from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.developer_page import DeveloperPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.developer_page = DeveloperPage(driver)
