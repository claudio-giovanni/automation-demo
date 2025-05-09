from playwright.sync_api import Page

from app.components.navbar import Navbar
from app.pages import ArticlePage, DashboardPage, NewArticlePage, ProfilePage, SignInPage, SignUpPage


class Conduit:

    def __init__(self, page: Page):
        self.page = page
        page.goto("http://localhost:4200")

    @property
    def navbar(self) -> Navbar:
        return Navbar(page=self.page)

    @property
    def new_article_page(self) -> NewArticlePage:
        return NewArticlePage(page=self.page)

    @property
    def article_page(self) -> ArticlePage:
        return ArticlePage(page=self.page)

    @property
    def dashboard_page(self) -> DashboardPage:
        return DashboardPage(page=self.page)

    @property
    def sign_up_page(self) -> SignUpPage:
        return SignUpPage(page=self.page)

    @property
    def profile_page(self) -> ProfilePage:
        return ProfilePage(page=self.page)

    @property
    def sign_in_page(self) -> SignInPage:
        return SignInPage(page=self.page)

    def get_error_message(self) -> str:
        return self.page.locator(".error-messages").first.inner_text()

    def get_success_message(self) -> str:
        return self.page.locator(".success-messages").first.inner_text()
