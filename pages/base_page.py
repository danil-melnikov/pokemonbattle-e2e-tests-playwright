from playwright.sync_api import Page

class BasePage:
    STANDARD_URL = "https://pokemonbattle.ru"

    def __init__(self, page: Page, timeout: int = 5000):
        self.page = page
        self.timeout = timeout
