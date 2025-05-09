import re

from playwright.sync_api import Page, expect

from app.components.navbar import Navbar


class SignUpPage:
    def __init__(self, page: Page):
        expect(page).to_have_url(re.compile(r"/register"))
        self.page = page
        self._username_input = page.locator("input[placeholder='Username']")
        self._email_input = page.locator("input[placeholder='Email']")
        self._password_input = page.locator("input[placeholder='Password']")
        self._submit_button = page.locator("button:has-text('Sign up')")

    @property
    def navbar(self) -> Navbar:
        return Navbar(page=self.page)

    def submit_form(self, username: str, email: str, password: str):
        self._username_input.fill(username)
        self._email_input.fill(email)
        self._password_input.fill(password)
        self._submit_button.click()
