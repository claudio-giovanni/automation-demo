import pytest


@pytest.mark.dependency()
def test_sign_up_and_login(app, data):
    app.dashboard_page.navbar.click_sign_up()
    app.sign_up_page.submit_form(
        username=data.login_user.username, password=data.login_user.password, email=data.login_user.email
    )
    app.sign_in_page.submit_form(email=data.login_user.email, password=data.login_user.password)
    assert app.dashboard_page


@pytest.mark.dependency(depends=["test_sign_up_and_login"])
def test_sign_up_and_login_wrong_password(app, data):
    app.dashboard_page.navbar.click_sign_in()
    app.sign_in_page.submit_form(email=data.login_user.email, password="WRONG_PASSWORD")
    assert app.get_error_message() == "Invalid email or password"
