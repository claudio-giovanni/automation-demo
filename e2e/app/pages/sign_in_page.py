import re

from playwright.sync_api import Page, expect

from app.components.navbar import Navbar


class SignInPage:
    def __init__(self, page: Page):
        expect(page).to_have_url(re.compile(r"/login"))
        self.page = page
        self._email_input = page.locator("input[placeholder='Email']")
        self._password_input = page.locator("input[placeholder='Password']")
        self._submit_button = page.locator("button:has-text('Sign in')")

    @property
    def navbar(self) -> Navbar:
        return Navbar(page=self.page)

    def submit_form(self, email: str, password: str) -> None:
        self._email_input.fill(email)
        self._password_input.fill(password)
        self._submit_button.click()
