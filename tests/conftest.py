import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture
def chromium_page():
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
        