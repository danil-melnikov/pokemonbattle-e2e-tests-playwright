import allure
import pytest
from pages.premium_page import PremiumPage
from data.api_constants import (
    PREMIUM_DAYS,
    CARD_NUMBER, CARD_DATE, CARD_CVV, CARD_NAME,
    INVALID_CARD_NUMBER, INVALID_CARD_DATE,
)


@allure.title("Скриншот формы оплаты: {description}")
@pytest.mark.parametrize("description, setup_func", [
    ("Пустая форма", None),
    ("Заполненная форма", "fill_valid"),
    ("Неверный номер карты", "fill_invalid_number"),
    ("Неверный срок карты", "fill_invalid_date"),
])
def test_screenshot_payment_form(authorized_page, assert_snapshot, description, setup_func):
    page = authorized_page
    premium_page = PremiumPage(page)

    with allure.step("Переходим на страницу Премиума"):
        premium_page.open_page()
        premium_page.should_be_premium_page()

    with allure.step("Переходим к оплате"):
        premium_page.set_days(PREMIUM_DAYS)
        premium_page.go_to_payment()

    with allure.step(f"Подготавливаем форму: {description}"):
        if setup_func == "fill_valid":
            premium_page.fill_card_data(CARD_NUMBER, CARD_DATE, CARD_CVV, CARD_NAME)
        elif setup_func == "fill_invalid_number":
            premium_page.fill_card_number(INVALID_CARD_NUMBER)
            premium_page.wait_for_card_number_error_visible()
        elif setup_func == "fill_invalid_date":
            premium_page.fill_card_date(INVALID_CARD_DATE)
            premium_page.wait_for_card_date_error_visible()

    with allure.step("Делаем скриншот формы оплаты"):
        screenshot = premium_page.take_payment_form_screenshot()

    with allure.step("Сравниваем с эталоном"):
        safe_name = description.replace(" ", "_")
        assert_snapshot(screenshot, f"payment_form_{safe_name}.png")
