from playwright.sync_api import expect
from pages.base_page import BasePage
from data.api_constants import TRAINER_ID


class TrainerPage(BasePage):
    URL = f"{BasePage.STANDARD_URL}/trainer/{TRAINER_ID}"

    @property
    def achievement_beginning(self):
        return self.page.locator("#beginning > img")

    def open_from_main(self, page):
        page.get_by_role("link", name=f"ID {TRAINER_ID} логотип").click()

    def should_be_trainer_page(self):
        expect(self.page).to_have_url(self.URL)

    def should_show_achievement(self):
        expect(self.achievement_beginning).to_be_visible()
