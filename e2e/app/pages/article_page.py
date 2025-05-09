import re

from playwright.sync_api import Page, expect

from app.components.navbar import Navbar


class ArticlePage:
    def __init__(self, page: Page):
        expect(page).to_have_url(re.compile(r"/article/.*"))
        self.page = page

    @property
    def navbar(self) -> Navbar:
        return Navbar(page=self.page)

    def submit_comment(self, comment: str) -> None:
        self.page.locator("textarea[placeholder='Write a comment...']").fill(comment)
        self.page.locator("button:has-text('Post Comment')").click()

    def click_edit_article_button(self) -> None:
        self.page.locator("button:has-text('Edit Article')").first.click()

    def click_delete_article_button(self) -> None:
        self.page.locator("button:has-text('Delete Article')").first.click()

    def click_delete_latest_comment(self) -> None:
        self.page.locator("app-article-comments").locator("i.ion-trash-a").first.click()

    def get_comment_count(self) -> int:
        return len(self.page.locator(".card").all()) - 1  # Exclude the new comment form
