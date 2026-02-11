from selenium.webdriver.common.by import By
from pages.base_page import Page


class DeveloperPage(Page):
    JOIN_WAITLIST_BTN = (By.CSS_SELECTOR, "a.join-button")

    def verify_join_waitlist_visible(self):
        self.wait_until_element_present(*self.JOIN_WAITLIST_BTN)
