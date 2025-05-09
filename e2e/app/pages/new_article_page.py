import re

from playwright.sync_api import Page, expect

from app.components.navbar import Navbar


class NewArticlePage:
    def __init__(self, page: Page):
        expect(page).to_have_url(re.compile(r"/editor.*"))
        self.page = page
        self._title_input = page.locator("input[placeholder='Article Title']")
        self._subtitle_input = page.locator("""input[placeholder="What's this article about?"]""")
        self._body_input = page.locator("textarea[placeholder='Write your article (in markdown)']")
        self._tags_input = page.locator("input[placeholder='Enter tags']")
        self._publish_button = page.locator("button:has-text('Publish Article')")

    @property
    def navbar(self) -> Navbar:
        return Navbar(page=self.page)

    def get_success_message(self) -> str:
        return self.page.locator(".success-messages").first.inner_text()

    def submit_form(self, title: str, subtitle: str, body: str, tags: list[str]) -> None:
        self._title_input.fill(title)
        self._subtitle_input.fill(subtitle)
        self._body_input.fill(body)
        for tag in tags:
            self._tags_input.fill(tag)
            self._tags_input.press("Enter")
        self._publish_button.click()
