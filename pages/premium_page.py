from playwright.sync_api import expect

from data.api_constants import PREMIUM_DAYS
from pages.base_page import BasePage


class PremiumPage(BasePage):
    URL = f"{BasePage.STANDARD_URL}/premium"

    @property
    def days_input(self):
        return self.page.get_by_placeholder(" ")

    @property
    def go_to_payment_button(self):
        return self.page.get_by_role("button", name="Перейти к оплате")

    @property
    def card_number_input(self):
        return self.page.get_by_role("textbox", name="0000 0000 0000")

    @property
    def card_date_input(self):
        return self.page.get_by_role("textbox", name="/00")

    @property
    def card_cvv_input(self):
        return self.page.get_by_role("textbox", name="000", exact=True)

    @property
    def card_name_input(self):
        return self.page.get_by_role("textbox", name="GERMAN DOLNIKOV")

    @property
    def pay_button(self):
        return self.page.get_by_role("button", name="Оплатить")

    @property
    def secure_code_input(self):
        return self.page.get_by_role("textbox", name="00000")

    @property
    def success_heading(self):
        return self.page.get_by_role("heading", name="Покупка прошла успешно")

    @property
    def cancel_button(self):
        return self.page.get_by_role("button", name="Отменить подписку")

    @property
    def cancelled_message(self):
        return self.page.get_by_text("Вы отменили подписку :(")

    @property
    def premium_cost(self):
        return self.page.locator(".k_skidka_premium")

    @property
    def payment_block(self):
        return self.page.locator(".auth__wrap.k_input_premium")

    @property
    def payment_form(self):
        return self.page.locator(".payment_form_card_form")

    @property
    def card_error_message(self):
        return self.page.get_by_text("Неверный номер карты")

    @property
    def card_date_error(self):
        return self.page.get_by_text("Неверный срок")

    def open_page(self):
        self.page.goto(self.URL)

    def should_be_premium_page(self):
        expect(self.page).to_have_url(self.URL)

    def select_days(self, days: str = "30"):
        self.days_input.fill(days)

    def go_to_payment(self):
        self.go_to_payment_button.click()

    def fill_card_data(self, number: str, date: str, cvv: str, name: str):
        self.card_number_input.type(number)
        self.card_date_input.type(date)
        self.card_cvv_input.type(cvv)
        self.card_name_input.type(name)

    def click_pay(self):
        self.pay_button.click()

    def fill_secure_code(self, code: str):
        self.secure_code_input.fill(code)

    def should_be_success(self):
        expect(self.success_heading).to_be_visible()

    def cancel_premium(self):
        self.cancel_button.click()

    def should_be_cancelled(self):
        expect(self.cancelled_message).to_be_visible()

    def set_days(self, days: str):
        self.days_input.click()
        self.days_input.fill(days)
        self.page.locator(".k_page_main_premium").click()

    def wait_for_cost_visible(self):
        expect(self.premium_cost).to_have_attribute("style", "")

    def take_payment_block_screenshot(self):
        return self.payment_block.screenshot()

    def fill_card_number(self, number: str):
        self.card_number_input.click()
        self.card_number_input.type(number)
        self.page.locator(".payment_form_card_form").click()

    def fill_card_date(self, date: str):
        self.card_date_input.click()
        self.card_date_input.type(date)
        self.page.locator(".payment_form_card_form").click()

    def wait_for_card_number_error_visible(self):
        expect(self.card_error_message).to_be_visible()

    def wait_for_card_date_error_visible(self):
        expect(self.card_date_error).to_be_visible()

    def take_payment_form_screenshot(self):
        return self.payment_form.screenshot()
