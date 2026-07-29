import allure
import pytest

from pages.login_page import LoginPage


@pytest.mark.regress
@allure.title("Проверка запроса")
def test_get_options_call(page):
    with allure.step("Открываем страницу"):
        login_page = LoginPage(page)

    with allure.step("Проверяем, что страница загрузилась"):
        login_page.should_show_version()


@pytest.mark.regress
@allure.title("Проверка ответа (статус 200 и версия)")
def test_get_options_version_reply(page):
    with allure.step("Открываем страницу"):
        login_page = LoginPage(page)

    with allure.step("Проверяем версию на странице"):
        login_page.should_be_version("4.7.0")
