import allure
from pages.trainer_page import TrainerPage


@allure.title("Скриншот карточки тренера")
def test_screenshot_trainer_card(authorized_page, assert_snapshot):
    page = authorized_page
    trainer_page = TrainerPage(page)

    with allure.step("Переходим на страницу тренера"):
        trainer_page.open_page()
        trainer_page.should_be_trainer_page()

    with allure.step("Делаем скриншот карточки тренера"):
        trainer_card_screenshot = trainer_page.take_trainer_card_screenshot()

    with allure.step("Сравниваем с эталоном"):
        assert_snapshot(trainer_card_screenshot, "trainer_card.png")
