from playwright.sync_api import expect
from pages.base_page import BasePage


class MainPage(BasePage):

    URL = BasePage.STANDARD_URL

    @property
    def trainer_badge(self):
        return self.page.get_by_role("link", name="ID 64834 логотип")

    def should_be_main_page(self):
        expect(self.page).to_have_url(f"{self.URL}/")
