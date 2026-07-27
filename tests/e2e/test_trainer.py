import allure
import pytest

from playwright.sync_api import expect
from data.api_constants import TRAINER_ID, SITE_URL, PREMIUM_URL
from data.api_constants import (
    TRAINER_ID, SITE_URL, PREMIUM_URL,
    CARD_NUMBER, CARD_DATE, CARD_CVV, CARD_NAME, SECURE_CODE, PREMIUM_DAYS
)


@pytest.mark.smoke
@allure.title("Переход на страницу тренера с главной страницы")
def test_go_to_trainer_from_main(authorized_page):
    page = authorized_page

    with allure.step("Кликаем по ID тренера в шапке"):
        page.get_by_role("link", name=f"ID {TRAINER_ID} логотип").click()

    with allure.step("Ждём перехода на страницу тренера"):
        page.wait_for_url(f"{SITE_URL}/trainer/{TRAINER_ID}")

    with allure.step("Проверяем, что перешли на страницу тренера"):
        expect(page).to_have_url(f"{SITE_URL}/trainer/{TRAINER_ID}")


@pytest.mark.regress
@allure.title("Переход со страницы тренера в раздел покупки Премиума")
def test_go_to_premium_from_trainer(authorized_page):
    page = authorized_page

    with allure.step("Переходим на страницу тренера"):
        page.get_by_role("link", name=f"ID {TRAINER_ID} логотип").click()
        expect(page).to_have_url(f"{SITE_URL}/trainer/{TRAINER_ID}")

    with allure.step("Кликаем по кнопке 'Премиум'"):
        page.get_by_text("Pokemon Premium").click()

    with allure.step("Проверяем, что перешли на страницу Премиума"):
        expect(page).to_have_url(PREMIUM_URL)


@pytest.mark.regress
@allure.title("Проверка активности ачивки «Начало большого пути»")
def test_achievement_big_journey_start(authorized_page):
    page = authorized_page

    with allure.step("Переходим на страницу тренера"):
        page.get_by_role("link", name=f"ID {TRAINER_ID} логотип").click()
        expect(page).to_have_url(f"{SITE_URL}/trainer/{TRAINER_ID}")

    with allure.step("Проверяем, что ачивка видна"):
        expect(page.locator("#beginning > img")).to_be_visible()


@pytest.mark.regress
@allure.title("Успешная покупка Премиума")
def test_buy_premium(authorized_page, disable_premium, cancel_premium):
    page = authorized_page

    with allure.step("Переходим на страницу Премиума"):
        page.goto(PREMIUM_URL)
        page.wait_for_url(PREMIUM_URL)

    with allure.step("Выбираем количество дней (30) и переходим к оплате"):
        page.get_by_placeholder(" ").fill(PREMIUM_DAYS)
        page.get_by_role("button", name="Перейти к оплате").click()

    with allure.step("Заполняем данные карты"):
        page.get_by_role("textbox", name="0000 0000 0000").fill(CARD_NUMBER)
        page.get_by_role("textbox", name="/00").fill(CARD_DATE)
        page.get_by_role("textbox", name="000", exact=True).fill(CARD_CVV)
        page.get_by_role("textbox", name="GERMAN DOLNIKOV").fill(CARD_NAME)

    with allure.step("Нажимаем 'Оплатить"):
        page.get_by_role("button", name="Оплатить").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Оплатить").click()

    with allure.step("Вводим secure code из СМС"):
        page.get_by_role("textbox", name="00000").fill(SECURE_CODE)

    with allure.step("Подтверждаем оплату"):
        page.get_by_role("button", name="Оплатить").click()

    with allure.step("Проверяем, что покупка прошла успешно"):
        expect(page.get_by_role("heading", name="Покупка прошла успешно")).to_be_visible()


@pytest.mark.regress
@allure.title("Успешная отмена Премиума")
def test_cancel_premium(authorized_page, enable_premium):
    page = authorized_page

    with allure.step("Переходим на страницу Премиума"):
        page.goto(PREMIUM_URL)
        page.wait_for_url(PREMIUM_URL)

    with allure.step("Нажимаем 'Отменить Премиум'"):
        page.get_by_role("button", name="Отменить подписку").click()

    with allure.step("Подтверждаем отмену"):
        page.get_by_role("button", name="Отменить подписку").click()

    with allure.step("Проверяем, что Премиум отменён"):
        expect(page.get_by_text("Вы отменили подписку :(")).to_be_visible()