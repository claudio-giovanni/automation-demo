import os
import random
import string
from dataclasses import dataclass
from typing import Iterator

import pytest
from playwright.sync_api import sync_playwright

from app import Conduit

browser_headless = os.getenv("BROWSER_HEADLESS", "").lower() == "true"
browser_debug = os.getenv("BROWSER_DEBUG", "").lower() == "true"
browser_slow_mo = int(os.getenv("BROWSER_SLOW_MO", 0))
app_url = os.getenv("APP_URL")


@pytest.fixture(autouse=True)
def app() -> Conduit:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=browser_headless, slow_mo=browser_slow_mo, timeout=2_000)
        page = browser.new_page()
        yield Conduit(page=page)
        if browser_debug:
            page.wait_for_timeout(10_000)
        browser.close()


def _random_string(length: int = 10) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


class User:
    def __init__(self):
        self.username = f"name-{_random_string()}"
        self.email = f"{_random_string()}@test.com"
        self.password = _random_string()


class Article:
    def __init__(self):
        self.title = f"title {_random_string()}"
        self.subtitle = f"subtitle {_random_string()}"
        self.body = f"body {_random_string(length=100)}"
        self.tags = [_random_string() for _ in range(2)]


@dataclass
class MockData:
    login_user: User
    article_user: User
    follow_user_1: User
    follow_user_2: User
    article_1: Article
    article_2: Article


@pytest.fixture(autouse=True, scope="session")
def data() -> MockData:
    yield MockData(
        login_user=User(),
        article_user=User(),
        article_1=Article(),
        article_2=Article(),
        follow_user_1=User(),
        follow_user_2=User(),
    )
