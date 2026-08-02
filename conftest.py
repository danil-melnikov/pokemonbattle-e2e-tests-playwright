import os
import subprocess
import pytest

from dotenv import load_dotenv
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.main_page import MainPage


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
        subprocess.call(
            "allure generate --clean --single-file allure-results",
            shell=True
        )


@pytest.fixture
def authorized_page(page):
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.should_be_login_page()
    login_page.login()
    main_page = MainPage(page)
    main_page.should_be_main_page()
    return page
