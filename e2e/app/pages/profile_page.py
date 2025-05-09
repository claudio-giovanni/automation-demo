import re

from playwright.sync_api import Page, expect

from app.components.navbar import Navbar


class ProfilePage:
    def __init__(self, page: Page):
        expect(page).to_have_url(re.compile(r".*profile.*"))
        self.page = page

    @property
    def navbar(self) -> Navbar:
        return Navbar(page=self.page)

    def click_latest_article(self) -> None:
        self.page.locator(".article-preview").first.click()

    def click_follow_user(self) -> None:
        self.page.locator("i.ion-plus-round").first.click()

    def get_latest_article_title(self) -> str:
        return self.page.locator(".article-preview").first.locator("h1").inner_text()

    def get_empty_articles_message(self) -> str:
        return self.page.locator(".article-preview").inner_text()
