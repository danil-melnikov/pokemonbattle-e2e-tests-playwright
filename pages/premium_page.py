from playwright.sync_api import expect
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
