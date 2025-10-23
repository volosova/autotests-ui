from playwright.sync_api import expect
from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

    def fill(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def check_visible(self, email, password):
        expect(self.email_input).to_have_value(email)
        expect(self.password_input).to_have_value(password)
