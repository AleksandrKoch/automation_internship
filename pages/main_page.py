from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    # different button for now
    CONNECT_DEVELOPER_BTN = (By.CSS_SELECTOR, "a[data-sentry-component='MenuFooterBanner']")

    def open_main(self):
        self.open_url('/')
        self.wait_until_url_contains("soft.reelly.io/")

    def click_connect_developer(self):
        self.wait_until_clickable_click(*self.CONNECT_DEVELOPER_BTN)

    def click_connect_developer_and_wait_new_tab(self, expected_windows_count=2):
        self.click_connect_developer()
        self.wait_until_windows_count_is(expected_windows_count)

    def switch_to_new_tab(self):
        self.switch_to_newest_tab()
