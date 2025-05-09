from playwright.sync_api import Page


class Navbar:
    def __init__(self, page: Page):
        self.page = page

    def click_sign_up(self):
        self.page.locator("text=Sign up").click()

    def click_sign_in(self):
        self.page.locator("text=Sign in").click()

    def click_home(self):
        self.page.locator("text=Home").click()

    def click_new_article(self):
        self.page.locator("text=New Article").click()

    def click_profile(self):
        self.page.locator(".user-pic").click()
