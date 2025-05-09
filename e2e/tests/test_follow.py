from tests.test_article import sign_in_and_write_article


def test_follow_user(app, data):
    app.navbar.click_sign_up()
    app.sign_up_page.submit_form(
        username=data.follow_user_1.username, password=data.follow_user_1.password, email=data.follow_user_1.email
    )
    sign_in_and_write_article(app=app, user=data.follow_user_1, article=data.article_1)
    app.page.evaluate("localStorage.clear()")
    app.page.reload()

    app.navbar.click_sign_up()
    app.sign_up_page.submit_form(
        username=data.follow_user_2.username, password=data.follow_user_2.password, email=data.follow_user_2.email
    )
    app.navbar.click_sign_in()
    app.sign_in_page.submit_form(email=data.follow_user_2.email, password=data.follow_user_2.password)

    app.dashboard_page.click_my_feed()
    assert app.dashboard_page.get_article_count() == 0

    app.dashboard_page.click_global_feed()
    app.dashboard_page.click_article_user(username=data.follow_user_1.username)
    app.profile_page.click_follow_user()
    app.navbar.click_home()
    app.dashboard_page.click_my_feed()
    assert app.dashboard_page.get_article_count() == 1
