from selenium.webdriver.common.by import By
from pages.base_page import Page


class DeveloperPage(Page):
    # different locator for now as button is missing
    JOIN_WAITLIST_BTN = (By.XPATH, "//a[.//div[normalize-space()='See How Transparency Works']]")

    def verify_join_waitlist_visible(self):
        self.wait_until_element_present(*self.JOIN_WAITLIST_BTN)
