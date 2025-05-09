import re

from playwright.sync_api import Page, expect

from app.components.navbar import Navbar


class DashboardPage:
    def __init__(self, page: Page):
        expect(page).to_have_url(re.compile(r"/"))
        self.page = page

    @property
    def navbar(self) -> Navbar:
        return Navbar(page=self.page)

    def get_latest_article_title(self) -> str:
        return self.page.locator(".article-preview").first.locator("h1").inner_text()

    def click_article_user(self, username: str) -> None:
        self.page.locator(f"a[href='#/profile/{username}']").first.click()

    def click_my_feed(self) -> None:
        self.page.locator("a:has-text('My Feed')").first.click()

    def click_global_feed(self) -> None:
        self.page.locator("a:has-text('Global Feed')").first.click()

    def get_article_count(self) -> int:
        if self.page.locator(".article-preview").inner_text() == "No articles are here... yet.":
            return 0
        return len(self.page.locator(".article-preview").all())
