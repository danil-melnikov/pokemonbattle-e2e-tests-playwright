import allure
import pytest
from pages.premium_page import PremiumPage
from pages.trainer_page import TrainerPage
from data.api_constants import (
    CARD_NUMBER, CARD_DATE, CARD_CVV, CARD_NAME, SECURE_CODE, PREMIUM_DAYS
)


@pytest.mark.smoke
@pytest.mark.ui
@allure.title("Переход на страницу тренера с главной страницы")
def test_go_to_trainer_from_main(authorized_page):
    trainer_page = TrainerPage(authorized_page)

    with allure.step("Кликаем по ID тренера в шапке"):
        trainer_page.open_from_main()

    with allure.step("Проверяем, что перешли на страницу тренера"):
        trainer_page.should_be_trainer_page()


@pytest.mark.regress
@pytest.mark.ui
@allure.title("Переход со страницы тренера в раздел покупки Премиума")
def test_go_to_premium_from_trainer(authorized_page):
    page = authorized_page
    trainer_page = TrainerPage(page)
    premium_page = PremiumPage(page)

    with allure.step("Переходим на страницу тренера"):
        trainer_page.open_from_main()
        trainer_page.should_be_trainer_page()

    with allure.step("Кликаем по кнопке 'Премиум'"):
        trainer_page.premium_button.click()

    with allure.step("Проверяем, что перешли на страницу Премиума"):
        premium_page.should_be_premium_page()


@pytest.mark.regress
@allure.title("Проверка активности ачивки «Начало большого пути»")
def test_achievement_big_journey_start(authorized_page):
    trainer_page = TrainerPage(authorized_page)

    with allure.step("Переходим на страницу тренера"):
        trainer_page.open_from_main()
        trainer_page.should_be_trainer_page()

    with allure.step("Проверяем, что ачивка видна"):
        trainer_page.should_show_achievement()


@pytest.mark.regress
@pytest.mark.ui
@allure.title("Успешная покупка Премиума")
def test_buy_premium(authorized_page, disable_premium, cancel_premium):
    page = authorized_page
    premium_page = PremiumPage(page)

    with allure.step("Переходим на страницу Премиума"):
        premium_page.open_page()
        premium_page.should_be_premium_page()

    with allure.step("Выбираем количество дней и переходим к оплате"):
        premium_page.select_days(PREMIUM_DAYS)
        premium_page.go_to_payment()

    with allure.step("Заполняем данные карты"):
        premium_page.fill_card_data(CARD_NUMBER, CARD_DATE, CARD_CVV, CARD_NAME)

    with allure.step("Нажимаем 'Оплатить'"):
        premium_page.click_pay()

    with allure.step("Вводим secure code из СМС"):
        premium_page.fill_secure_code(SECURE_CODE)

    with allure.step("Подтверждаем оплату"):
        premium_page.click_pay()

    with allure.step("Проверяем, что покупка прошла успешно"):
        premium_page.should_be_success()


@pytest.mark.regress
@allure.title("Успешная отмена Премиума")
def test_cancel_premium(authorized_page, enable_premium):
    page = authorized_page
    premium_page = PremiumPage(page)

    with allure.step("Переходим на страницу Премиума"):
        premium_page.open_page()
        premium_page.should_be_premium_page()

    with allure.step("Нажимаем 'Отменить Премиум'"):
        premium_page.cancel_premium()

    with allure.step("Подтверждаем отмену"):
        premium_page.cancel_premium()

    with allure.step("Проверяем, что Премиум отменён"):
        premium_page.should_be_cancelled()
