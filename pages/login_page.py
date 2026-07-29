import os

import allure
from dotenv import load_dotenv
from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = f"{BasePage.STANDARD_URL}/login"

    @property
    def email_input(self):
        return self.page.get_by_role("textbox", name="Почта")

    @property
    def password_input(self):
        return self.page.get_by_role("textbox", name="Пароль")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Войти")

    @property
    def version_label(self):
        return self.page.get_by_text("Версия")

    @property
    def version_number(self):
        return self.page.locator(".style_1_caption_16_500")

    def open_page(self):
        self.page.goto(self.URL)

    def login(self, email=None, password=None):
        if email is None or password is None:
            load_dotenv()
        self.email_input.fill(email or os.getenv("LOGIN"))
        self.password_input.fill(password or os.getenv("PASSWORD"))
        self.login_button.click()

    def should_be_login_page(self):
        expect(self.page).to_have_url(self.URL)

    def should_show_version(self):
            with self.page.expect_response(lambda r: "/v2/get_options" in r.url):
                    self.open_page()
                    expect(self.version_label).to_be_visible()

    def should_be_version(self, version: str):
            with self.page.expect_response(lambda r: "/v2/get_options" in r.url and r.status == 200):
                    self.open_page()
                    expect(self.version_number).to_contain_text(version)
