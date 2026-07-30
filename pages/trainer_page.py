from playwright.sync_api import expect
from pages.base_page import BasePage
from data.api_constants import TRAINER_ID


class TrainerPage(BasePage):
    URL = f"{BasePage.STANDARD_URL}/trainer/{TRAINER_ID}"

    @property
    def achievement_beginning(self):
        return self.page.locator("#beginning > img")

    @property
    def achievements(self):
        return self.page.locator(".achievements")

    @property
    def trainer_stats(self):
        return self.page.locator(".single_page_body_content_inner_box")

    @property
    def pokemon_stats(self):
        return self.page.locator('//span[text()="Покеболы"]/following-sibling::*')

    @property
    def level_stats(self):
        return self.page.locator('//span[text()="Уровень"]/following-sibling::*')

    @property
    def sliders(self):
        return self.page.locator(".single_page_body_content_inner_top_list_attr_one_slide")

    def open_page(self):
        self.page.goto(self.URL)

    def open_from_main(self, page):
        page.get_by_role("link", name=f"ID {TRAINER_ID} логотип").click()

    def should_be_trainer_page(self):
        expect(self.page).to_have_url(self.URL)

    def should_show_achievement(self):
        expect(self.achievement_beginning).to_be_visible()

    def take_trainer_card_screenshot(self):
        return self.trainer_stats.screenshot(
            mask=[
                self.pokemon_stats,
                self.level_stats,
                self.achievements,
                self.sliders,
            ]
        )
