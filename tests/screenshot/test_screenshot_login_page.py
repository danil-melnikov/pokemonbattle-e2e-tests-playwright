import allure

from pages.login_page import LoginPage


@allure.title("Скриншот всей страницы логина")
def test_screenshot_login_page(page, assert_snapshot):
    login_page = LoginPage(page)

    with allure.step("Открываем страницу логина"):
        login_page.open_page()

    with allure.step("Делаем скриншот всей страницы"):
        full_page_screenshot = page.screenshot(full_page=True, mask=[login_page.version_number])

    with allure.step("Сравниваем с эталоном"):
        assert_snapshot(full_page_screenshot, "login_full_page.png")

@allure.title("Скриншот формы логина")
def test_screenshot_login_from(page, assert_snapshot):
    login_page = LoginPage(page)

    with allure.step("Открываем страницу логина"):
        login_page.open_page()

    with allure.step("Делаем скриншот формы логина"):
        login_form_screenshot = login_page.login_form.screenshot()

    with allure.step("Сравниваем с эталоном"):
        assert_snapshot(login_form_screenshot, "login_form.png")
