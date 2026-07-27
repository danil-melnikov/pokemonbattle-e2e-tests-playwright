import os

import allure
import pytest
import requests

from config.api_config import BASE_URL, BASE_URL_LAVKA
from helpers.api_helpers import ApiSession


@pytest.fixture(scope="session")
def api_session():
    with allure.step("Создаём сессию"):
        with requests.Session() as session:
            session.headers.update({
             "trainer_token": os.getenv("POKEMONBATTLE_TOKEN")
            })
            yield ApiSession(session)


@pytest.fixture()
def cancel_premium(api_session):
    yield
    with allure.step("Отменяем Premium после теста"):
        response = api_session.post(BASE_URL_LAVKA + "/cancel_premium")
        if response.status_code == 200:
            allure.attach("Premium отменён", name="Cleanup", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(f"Статус: {response.status_code}", name="Cleanup error",
                          attachment_type=allure.attachment_type.TEXT)


@pytest.fixture()
def disable_premium(api_session):
    response = api_session.get(BASE_URL + "/me")
    body = response.json()["data"][0]

    if body.get("premium_active"):
        response = api_session.post(BASE_URL_LAVKA + "/cancel_premium")
        assert response.status_code == 200

    yield


@pytest.fixture()
def enable_premium(api_session):
    with allure.step("Проверяем статус Premium"):
        response = api_session.get(BASE_URL + "/me")
        body = response.json()["data"][0]

    if not body.get("is_premium"):
        with allure.step("Включаем Premium через API"):
            response = api_session.post(BASE_URL_LAVKA + "/payments", json={
                "order_type": "premium",
                "details": {
                    "days": 30,
                    "card_number": "4111111111111111",
                    "card_name": "Morgan Freeman",
                    "card_actual": "12/27",
                    "card_cvv": "125",
                    "secure_code": "56456"
                }
            })
            assert response.status_code == 200, f"Не удалось включить Premium: {response.text}"

    yield