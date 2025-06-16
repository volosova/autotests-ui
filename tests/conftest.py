import pytest
from playwright.sync_api import sync_playwright,Playwright, Page

@pytest.fixture
def chromium_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
        