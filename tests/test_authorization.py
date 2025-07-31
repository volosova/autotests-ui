import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [("user.name@gmail.com", "password"),("user.name@gmail.com", "  "),("  ", "password")], ids=["Invalid email and password", "Invalid email and empty password", "Empty email and invalid password"])
def test_wrong_email_or_password_authorization(email: str, password: str):

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill(email)

        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill(password)

        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")