import pytest
from playwright.sync_api import expect, Playwright, Page

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_contain_text('Courses')

        empty_results_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_results_icon).to_be_visible()

        empty_results_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(empty_results_header).to_be_visible()
        expect(empty_results_header).to_contain_text('There is no results')

        empty_results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_results_text).to_be_visible()
        expect(empty_results_text).to_contain_text('Results from the load test pipeline will be displayed here')