import os
import subprocess
import pytest

from dotenv import load_dotenv
from playwright.sync_api import expect


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "slow_mo": int(os.getenv("SLOW_MO", 0)),
    }


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1440, "height": 900}
    }


@pytest.fixture
def page(page):
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    return page


@pytest.fixture(scope="session", autouse=True)
def _set_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-id")

pytest_plugins = ["fixtures.api_fixtures"]


def pytest_addoption(parser):
    parser.addoption(
        "--html-report",
        action="store_true",
        default=False,
        help="Сгенерировать отчёт в формате HTML в директорию allure-report",
    )


def pytest_sessionfinish(session):
    if session.config.getoption("--html-report"):
        subprocess.call([
            "allure",
            "generate",
            "--clean",
            "--single-file",
            "allure-results"
        ])


@pytest.fixture
def authorized_page(page):
    page.goto("https://pokemonbattle.ru/")
    page.wait_for_url("https://pokemonbattle.ru/login")
    page.get_by_role("textbox", name="Почта").fill(os.getenv("LOGIN"))
    page.get_by_role("textbox", name="Пароль").fill(os.getenv("PASSWORD"))
    page.get_by_role("button", name="Войти").click()
    expect(page.get_by_role("link", name="ID 64834 логотип")).to_be_visible()
    page.wait_for_url("https://pokemonbattle.ru/")
    return page
