import pytest

from app import Conduit
from tests.conftest import Article, User


def sign_in_and_write_article(app: Conduit, user: User, article: Article) -> None:
    app.navbar.click_sign_in()
    app.sign_in_page.submit_form(email=user.email, password=user.password)
    app.dashboard_page.navbar.click_new_article()
    app.new_article_page.submit_form(
        title=article.title, subtitle=article.subtitle, body=article.body, tags=article.tags
    )
    app.navbar.click_profile()


@pytest.mark.dependency()
def test_write_article(app, data):
    app.dashboard_page.navbar.click_sign_up()
    app.sign_up_page.submit_form(
        username=data.article_user.username, password=data.article_user.password, email=data.article_user.email
    )
    sign_in_and_write_article(app=app, user=data.article_user, article=data.article_1)
    assert data.article_1.title == app.profile_page.get_latest_article_title()


@pytest.mark.dependency(depends=["test_write_article"])
def test_edit_article(app, data):
    app.navbar.click_sign_in()
    app.sign_in_page.submit_form(email=data.article_user.email, password=data.article_user.password)
    app.navbar.click_profile()
    app.profile_page.click_latest_article()
    app.article_page.click_edit_article_button()
    app.new_article_page.submit_form(
        title=data.article_2.title, subtitle=data.article_2.subtitle, body=data.article_2.body, tags=data.article_2.tags
    )
    app.navbar.click_profile()
    assert app.profile_page.get_latest_article_title() == data.article_2.title


@pytest.mark.dependency(depends=["test_edit_article"])
def test_comment_on_article(app, data):
    app.navbar.click_sign_in()
    app.sign_in_page.submit_form(email=data.article_user.email, password=data.article_user.password)
    app.navbar.click_profile()
    app.profile_page.click_latest_article()
    app.article_page.submit_comment(comment="comment 1")
    app.article_page.submit_comment(comment="comment 2")
    app.article_page.submit_comment(comment="comment 3")

    assert app.article_page.get_comment_count() == 3


@pytest.mark.dependency(depends=["test_comment_on_article"])
def test_delete_comment_on_article(app, data):
    app.navbar.click_sign_in()
    app.sign_in_page.submit_form(email=data.article_user.email, password=data.article_user.password)
    app.navbar.click_profile()
    app.profile_page.click_latest_article()
    assert app.article_page.get_comment_count() == 3
    app.article_page.click_delete_latest_comment()
    assert app.article_page.get_comment_count() == 2


@pytest.mark.dependency(depends=["test_delete_comment_on_article"])
def test_delete_article(app, data):
    app.navbar.click_sign_in()
    app.sign_in_page.submit_form(email=data.article_user.email, password=data.article_user.password)
    app.navbar.click_profile()
    app.profile_page.click_latest_article()
    app.article_page.click_delete_article_button()
    app.dashboard_page.navbar.click_profile()
    app.profile_page.click_latest_article()
    assert app.profile_page.get_empty_articles_message() == "No articles are here... yet."
