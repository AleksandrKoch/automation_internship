import os
from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    # Your exact HTML attributes (stable locators)
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[wized="emailInput"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[wized="passwordInput"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a[wized="loginButton"]')

    def open_sign_in(self):
        self.open_url('/sign-in')
        self.wait_until_element_present(*self.EMAIL_INPUT)

    def login(self, email='kocherginalexander@gmail.com', password='TestPassword'):

        email = email or os.getenv("REELLY_EMAIL")
        password = password or os.getenv("REELLY_PASSWORD")

        assert email, "Missing email. Set REELLY_EMAIL env var (recommended)."
        assert password, "Missing password. Set REELLY_PASSWORD env var (recommended)."

        self.wait_until_clickable(*self.EMAIL_INPUT)
        email_el = self.find_element(*self.EMAIL_INPUT)
        email_el.clear()
        self.input_text(email, *self.EMAIL_INPUT)

        self.wait_until_clickable(*self.PASSWORD_INPUT)
        pwd_el = self.find_element(*self.PASSWORD_INPUT)
        pwd_el.clear()
        self.input_text(password, *self.PASSWORD_INPUT)

        self.wait_until_clickable_click(*self.CONTINUE_BTN)

        # After successful login you land on https://soft.reelly.io/
        self.wait_until_url_contains("soft.reelly.io/")
