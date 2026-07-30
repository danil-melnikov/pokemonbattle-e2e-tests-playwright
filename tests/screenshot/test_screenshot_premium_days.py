import allure
import pytest
from pages.premium_page import PremiumPage


@allure.title("Скриншот блока ввода дней Премиума: {days} дней")
@pytest.mark.parametrize("days", [
    "15",
    "90",
    "270",
    "400",
])
def test_screenshot_premium_days(authorized_page, assert_snapshot, days):
    page = authorized_page
    premium_page = PremiumPage(page)

    with allure.step("Переходим на страницу Премиума"):
        premium_page.open_page()
        premium_page.should_be_premium_page()

    with allure.step(f"Вводим {days} дней"):
        premium_page.set_days(days)

    with allure.step("Ждём появления стоимости"):
        premium_page.wait_for_cost_visible()

    with allure.step("Делаем скриншот блока оплаты"):
        screenshot = premium_page.take_payment_block_screenshot()

    with allure.step("Сравниваем с эталоном"):
        assert_snapshot(screenshot, f"premium_days_{days}.png")
