import allure
import pytest
from playwright.sync_api import expect

@pytest.mark.regress
@allure.title("Проверка запроса")
def test_get_options_call(page):
    with allure.step("Начинаем перехват запроса"):
        with page.expect_response(lambda r: "/v2/get_options" in r.url):
            with allure.step("Открываем страницу"):
                page.goto("https://pokemonbattle.ru/")

    with allure.step("Проверяем, что страница загрузилась"):
        expect(page.get_by_text("Версия")).to_be_visible()

@pytest.mark.regress
@allure.title("Проверка ответа (статус 200 и версия)")
def test_get_options_version_reply(page):
    with allure.step("Начинаем перехват ответа"):
        with page.expect_response(lambda r: "/v2/get_options" in r.url and r.status == 200):
            with allure.step("Открываем страницу"):
                page.goto("https://pokemonbattle.ru/")

    with allure.step("Проверяем версию на странице"):
        expect(page.locator(".style_1_caption_16_500")).to_contain_text("4.7.0")
