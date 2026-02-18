from selenium.webdriver.common.by import By
from pages.base_page import Page


class DeveloperPage(Page):
    # different locator for now as button is missing
    JOIN_WAITLIST_BTN = (By.XPATH, "//div[contains(normalize-space(.),'What’s New in Reelly 2.5')]")

    def verify_join_waitlist_visible(self):
        self.wait_until_element_present(*self.JOIN_WAITLIST_BTN)
